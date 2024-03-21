import os
import glob
import torch
import numpy as np
from PIL import Image, ImageSequence


def get_files_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Folder does not exist.")
        return []
    files = glob.glob(os.path.join(folder_path, "*"))
    return files


def pilToImage(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


class JDCN_AnyFileList:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        FileExtensions = [
            "*",
            # Image Files
            ".jpg", ".jpeg", ".png", ".gif", ".tiff", ".bmp", ".webp", ".svg", ".raw", ".cr2", ".nef",

            # Video Files
            ".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm", ".3gp",

            # Text Files
            ".txt", ".csv", ".json", ".xml", ".md", ".pdf", ".html", ".htm", ".rtf", ".tex", ".yaml", ".yml"
        ]

        return {
            "required": {
                "folder_path": ("STRING", {
                    "multiline": False,
                    "default": "undefined"
                }),
                "extension": (FileExtensions,),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "INT",)
    RETURN_NAMES = ("FileNames", "FileNamesPath", "FileCount",)
    OUTPUT_IS_LIST = (True, True, False)
    OUTPUT_NODE = True
    FUNCTION = "make_list"

    def make_list(self, folder_path, extension):

        if not os.path.exists(folder_path):
            print(f"The folder '{folder_path}' does not exist.")
            return ([""], [""], 0)

        file_names = []
        file_paths = []
        file_count = 0

        if extension != '*':
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    if file.endswith(extension):
                        file_name, file_extension = os.path.splitext(file)
                        file_names.append(file_name)
                        file_paths.append(os.path.join(root, file))
        else:
            files = get_files_in_folder(folder_path)
            for file in files:
                file_name, file_extension = os.path.splitext(file)
                file_names.append(file_name)
                file_paths.append(file)

        file_count = len(file_paths)

        if file_count == 0:
            print(
                f"The folder '{folder_path}' does not contain '{extension}' files.")
            file_paths.append("No file found!")

        return (file_names, file_paths, file_count,)


N_CLASS_MAPPINGS = {
    "JDCN_AnyFileList": JDCN_AnyFileList,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_AnyFileList": "JDCN_AnyFileList",
}
