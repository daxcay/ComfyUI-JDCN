import os
import torch
import numpy as np
from PIL import Image, ImageSequence
import os
from os.path import isfile, join
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import networkx as nx
from collections import Counter


def generate_wordcloud_and_network_graph(file_paths, output_dir, top_n_wordcloud=100, top_n_network=100):
    word_counter = Counter()
    tag_cooccurrences = Counter()

    for file_path in file_paths:
        with open(file_path, 'r') as f:
            tags = f.read().strip().split(',')
            word_counter.update(tags)
            for tag1 in tags:
                for tag2 in tags:
                    if tag1 != tag2:
                        tag_cooccurrences[(tag1, tag2)] += 1

    # Word cloud generation
    top_wordcloud_tags = dict(word_counter.most_common(top_n_wordcloud))
    wordcloud = WordCloud(width=1920, height=1080,
                          background_color='white').generate_from_frequencies(top_wordcloud_tags)

    plt.figure(figsize=(16, 9))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    output_wordcloud_file = join(output_dir, 'wordcloud.png')
    plt.savefig(output_wordcloud_file, bbox_inches='tight', pad_inches=0)
    plt.close()

    print("Word cloud saved as", output_wordcloud_file)

    # Network graph generation
    G = nx.Graph()

    top_tags = [tag for tag, _ in word_counter.most_common(top_n_network)]

    for (tag1, tag2), weight in tag_cooccurrences.items():
        if tag1 in top_tags and tag2 in top_tags:
            G.add_edge(tag1, tag2, weight=weight)

    plt.figure(figsize=(16, 9))
    pos = nx.kamada_kawai_layout(G)

    nx.draw(G, pos, with_labels=True, font_size=10, node_color='skyblue',
            node_size=2000, edge_color='gray', linewidths=1, font_weight='bold')
    edge_labels = {(tag1, tag2): weight for (
        tag1, tag2), weight in tag_cooccurrences.items() if tag1 in top_tags and tag2 in top_tags}
    nx.draw_networkx_edge_labels(
        G, pos, edge_labels=edge_labels, font_color='red')

    plt.margins(0)

    output_network_graph_file = join(output_dir, 'network_graph.png')
    plt.savefig(output_network_graph_file, bbox_inches='tight', pad_inches=0)
    plt.close()

    print("Network graph saved as", output_network_graph_file)

    return output_wordcloud_file, output_network_graph_file


def pilToImage(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


def load_image(image_path):

    try:
        img = Image.open(image_path)
        image = img.convert("RGB")
        loaded_image = pilToImage(image)
    except Exception as e:
        print(f"Error loading image from '{image_path}': {e}")

    return loaded_image


def create_empty_image(width=100, height=100, color=(255, 255, 255)):
    try:
        empty_image = Image.new("RGB", (width, height), color)
    except Exception as e:
        print(f"Error creating empty image: {e}")
        empty_image = None

    return empty_image


class JDCN_CaptionVisualizer:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "TextFilePathList": ("STRING", {"forceInput": True}),
                "WordCloudTop": ("INT", {"default": 1, "min": 1, "max": 9999}),
                "NetworkGraphTop": ("INT", {"default": 1, "min": 1, "max": 9999})
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Images",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "Visualize"
    OUTPUT_NODE = True
    CATEGORY = "JDCN Dataset Tools"

    def Visualize(self, TextFilePathList, WordCloudTop, NetworkGraphTop):

        try:

            directory_path = os.path.dirname(TextFilePathList[0])
            visualize_path = os.path.join(directory_path, "visualize")
            os.makedirs(visualize_path, exist_ok=True)
            wc, ng = generate_wordcloud_and_network_graph(
                TextFilePathList, visualize_path, WordCloudTop[0], NetworkGraphTop[0])
            return ([wc, ng],)

        except Exception as e:
            print(f"Error saving: {e}")

        return (["", ""],)


N_CLASS_MAPPINGS = {
    "JDCN_CaptionVisualizer": JDCN_CaptionVisualizer,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_CaptionVisualizer": "JDCN_CaptionVisualizer",
}
