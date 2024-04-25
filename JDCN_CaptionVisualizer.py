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

def generate_wordcloud_and_network_graph(input_dir, output_dir):
    files = [f for f in os.listdir(input_dir) if isfile(join(input_dir, f))]

    word_counter = Counter()
    tag_cooccurrences = Counter()

    for file in files:
        with open(join(input_dir, file), 'r') as f:
            tags = f.read().strip().split(',')
            word_counter.update(tags)
            for tag1 in tags:
                for tag2 in tags:
                    if tag1 != tag2:
                        tag_cooccurrences[(tag1, tag2)] += 1

    wordcloud = WordCloud(width=1920, height=1080, background_color='white').generate_from_frequencies(word_counter)

    plt.figure(figsize=(16, 9))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    output_wordcloud_file = join(output_dir, 'wordcloud.png')
    plt.savefig(output_wordcloud_file, bbox_inches='tight', pad_inches=0)  # Adjust bounding box to remove white space
    plt.close()

    print("Word cloud saved as", output_wordcloud_file)

    G = nx.Graph()

    for (tag1, tag2), weight in tag_cooccurrences.items():
        G.add_edge(tag1, tag2, weight=weight)

    plt.figure(figsize=(16, 9))

    # Use an alternative layout algorithm (e.g., spectral layout)
    pos = nx.spectral_layout(G)

    nx.draw(G, pos, with_labels=True, font_size=10, node_color='skyblue', node_size=2000, edge_color='gray', linewidths=1, font_weight='bold')
    edge_labels = {(tag1, tag2): weight for (tag1, tag2), weight in tag_cooccurrences.items()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    # Adjust figure margins to minimize white space
    plt.margins(0)

    output_network_graph_file = join(output_dir, 'network_graph.png')
    plt.savefig(output_network_graph_file, bbox_inches='tight', pad_inches=0)  # Adjust bounding box to remove white space
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


class JDCN_CaptionVisualizer:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "TagsDirectory": ("STRING", {"default": "directory path"}),
            },
        }

    RETURN_TYPES = ("IMAGE", "IMAGE")
    RETURN_NAMES = ("WordCloud", "NetworkGraph")
    FUNCTION = "Visualize"
    OUTPUT_NODE = True
    CATEGORY = "JDCN Dataset Tools"

    def Visualize(self, TagsDirectory):

        try:

            visualize_path = os.path.join(TagsDirectory, "visualize")
            os.makedirs(visualize_path, exist_ok=True)

            wc, ng = generate_wordcloud_and_network_graph(TagsDirectory, visualize_path)

            wc = load_image(wc)
            ng = load_image(ng)

        except Exception as e:
            print(f"Error saving: {e}")

        return (wc, ng)


N_CLASS_MAPPINGS = {
    "JDCN_CaptionVisualizer": JDCN_CaptionVisualizer,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_CaptionVisualizer": "JDCN_CaptionVisualizer",
}
