import os
import torch
import numpy as np
from PIL import Image, ImageSequence
from .shared import FILE_EXTENSIONS

def extract_file_name(file_path):
    base_name, _ = os.path.splitext(os.path.basename(file_path)) 
    return base_name

def extract_file_names(file_paths, skip, load):
    file_names = []

    start_index = skip
    end_index = skip + load

    if start_index == end_index:
        subset_file_paths = file_paths[start_index:len(file_paths)]
    else:
        subset_file_paths = file_paths[start_index:end_index]
    
    for file_path in subset_file_paths:
        file_names.append(extract_file_name(file_path))
    return file_names

def extract_file_paths(file_paths, skip, load):
    
    start_index = skip
    end_index = skip + load

    if start_index == end_index:
        subset_file_paths = file_paths[start_index:len(file_paths)]
    else:
        subset_file_paths = file_paths[start_index:end_index]

    return subset_file_paths


def get_files_by_extension(directory_path, extension):
    try:
        if not os.path.exists(directory_path):
            return []
        file_paths = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(root, file)
                    file_paths.append(file_path)
        return file_paths

    except Exception as e:
        print(f"Error: {e}")
        return []

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

def read_image_files(file_paths, skip, load):

    try:
        start_index = skip
        end_index = skip + load

        if start_index == end_index:
            subset_file_paths = file_paths[start_index:len(file_paths)]
        else:
            subset_file_paths = file_paths[start_index:end_index]

        # print(f"Processing: start index: {start_index}, end index: {end_index}, paths: {subset_file_paths}")

        images = []
        for file_path in subset_file_paths:
            try:
                image = load_image(file_path)
                images.append(image)
            except Exception as e:
                print(f"Error loading latent from file {file_path}: {e}")
        return images
    except Exception as e:
        print(f"Error: {e}")
        return []


class JDCN_BatchImageLoadFromDir:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "Directory": ("STRING", {"default": "directory path"}),
                "Load_Cap": ("INT", {"default": 1, "min": 1, "max": 9999}),
                "Skip_Frame": ("INT", {"default": 0, "min": 0, "max": 9999}),
            },
        }
    
    # INPUT_IS_LIST = True
    RETURN_TYPES = ("IMAGE", "STRING", "STRING", "INT", "INT", "INT")
    RETURN_NAMES = ("Images", "Image_Names", "Image_Paths", "Load_Cap", "Skip_Frame", "Count")
    FUNCTION = "doit"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True, True, True, False, False, False)
    CATEGORY = "🔵 JDCN 🔵"

    def doit(self, Directory, Load_Cap, Skip_Frame):

        file_paths = []
        
        for ext in FILE_EXTENSIONS['images']:
            tmi = get_files_by_extension(Directory, ext)
            file_paths.extend(tmi)

        if (len(file_paths) == 0):
            return ([], [], [], [])
        else:
            latents = read_image_files(file_paths, Skip_Frame, Load_Cap)
            file_names = extract_file_names(file_paths, Skip_Frame, Load_Cap)
            file_paths = extract_file_paths(file_paths, Skip_Frame, Load_Cap)

        return (latents, file_names, file_paths, Load_Cap, Skip_Frame, len(file_names))


N_CLASS_MAPPINGS = {
    "JDCN_BatchImageLoadFromDir": JDCN_BatchImageLoadFromDir,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_BatchImageLoadFromDir": "JDCN_BatchImageLoadFromDir",
}
