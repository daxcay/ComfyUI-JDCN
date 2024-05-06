import os
import glob
import random

from .shared import FILE_EXTENSIONS

def extract_file_names(file_paths):
    """
    Extract file names without extensions from a list of file paths.

    Parameters:
    - file_paths: A list of file paths.

    Returns:
    - A list of file names without extensions.
    """
    file_names = []

    for file_path in file_paths:
        base_name, _ = os.path.splitext(os.path.basename(file_path))
        file_names.append(base_name)

    return file_names

def get_files_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Folder does not exist.")
        return []
    files = glob.glob(os.path.join(folder_path, "*"))
    return files


def getSubDirectories(folder_path):
    try:
        root, dirs, _ = next(os.walk(folder_path))
        return dirs
    except StopIteration:
        return []


def randomly_select_files(file_paths, seed, number_of_files):
    random.seed(seed)
    if number_of_files > len(file_paths):
        raise ValueError(
            "Number of files requested exceeds the number of files available.")
    selected_files = random.sample(file_paths, number_of_files)

    return selected_files


class JDCN_AnyFileListRandom:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        FilterBy = [
            "*",
            "images",
            "audio",
            "video",
            "text",
            "tensors",
            "folder"
        ]

        FileExtensions = ["*"]
        FileExtensions.extend(FILE_EXTENSIONS["tensors"])
        FileExtensions.extend(FILE_EXTENSIONS["images"])
        FileExtensions.extend(FILE_EXTENSIONS["audio"])
        FileExtensions.extend(FILE_EXTENSIONS["video"])
        FileExtensions.extend(FILE_EXTENSIONS["text"])

        return {
            "required": {
                "folder_path": ("STRING", {
                    "multiline": False,
                    "default": "undefined"
                }),
                "filter_by": (FilterBy,),
                "extension": (FileExtensions,),
                "random_seed": ("INT", {"default": 1, "min": 1, "max": 0xffffffffffffffff}),
                "seed_change": (['fixed', 'increment', 'decrement', 'random'],),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 9999}),
                "deep_search": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "INT",)
    RETURN_NAMES = ("PathList", "PathNames", "Total")
    OUTPUT_IS_LIST = (True, True, False)
    OUTPUT_NODE = True
    FUNCTION = "make_list"

    CATEGORY = "🔵 JDCN 🔵"

    def make_list(self, folder_path, filter_by, extension, random_seed, seed_change, batch_size, deep_search):

        try:
            if not os.path.exists(folder_path):
                print(f"The folder '{folder_path}' does not exist.")
                return ([], [], 0)

            file_paths = []
            file_names = []
            total = 0

            if deep_search:
                for root, dirs, files in os.walk(folder_path):
                    if filter_by == "folder":
                        for directory in dirs:
                            file_paths.append(os.path.join(root, directory))
                            file_names.append(directory)
                            total += 1
                    else:
                        for file in files:
                            file_name, file_extension = os.path.splitext(file)
                            if filter_by == "*" or file_extension in FILE_EXTENSIONS[filter_by]:
                                if extension == "*" or file.endswith(extension):
                                    file_paths.append(os.path.join(root, file))
                                    file_names.append(file_name)
                                    total += 1
            else:
                if filter_by == "folder":
                    for directory in os.listdir(folder_path):
                        if os.path.isdir(os.path.join(folder_path, directory)):
                            file_paths.append(os.path.join(folder_path, directory))
                            file_names.append(directory)
                            total += 1
                else:
                    for file in os.listdir(folder_path):
                        if os.path.isfile(os.path.join(folder_path, file)):
                            file_name, file_extension = os.path.splitext(file)
                            if filter_by == "*" or file_extension in FILE_EXTENSIONS[filter_by]:
                                if extension == "*" or file.endswith(extension):
                                    file_paths.append(os.path.join(folder_path, file))
                                    file_names.append(file_name)
                                    total += 1

            file_paths = randomly_select_files(file_paths, random_seed, batch_size)

            return (file_paths, file_names, total)

        except Exception as e:
            print(f"An error occurred: {e}")
            return ([], [], 0)

N_CLASS_MAPPINGS = {
    "JDCN_AnyFileListRandom": JDCN_AnyFileListRandom,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_AnyFileListRandom": "JDCN_AnyFileListRandom",
}
