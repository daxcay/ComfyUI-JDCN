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
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "INT",)
    RETURN_NAMES = ("PathList", "PathNames", "Total")
    OUTPUT_IS_LIST = (True, True, False)
    OUTPUT_NODE = True
    FUNCTION = "make_list"

    CATEGORY = "🔵 JDCN 🔵"

    def make_list(self, folder_path, filter_by, extension, random_seed, seed_change, batch_size):

        if not os.path.exists(folder_path):
            print(f"The folder '{folder_path}' does not exist.")
            return ([""], [""], 0)

        search_mode = 0
        extension_search_mode = 0

        if filter_by == "folder":
            search_mode = 1
        elif filter_by == "*":
            search_mode = 3
        else:
            search_mode = 2

        if extension == "*":
            extension_search_mode = 1
        else:
            extension_search_mode = 2

        path_list = []

        if search_mode == 1:

            dirs = [folder for folder in os.listdir(
                folder_path) if os.path.isdir(os.path.join(folder_path, folder))]
            for dir_name in dirs:
                full_path = os.path.join(folder_path, dir_name)
                path_list.append(full_path)

        elif search_mode == 2:

            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_name, file_extension = os.path.splitext(file)
                    if file_extension in FILE_EXTENSIONS[filter_by]:
                        if extension_search_mode == 2:
                            if file.endswith(extension):
                                path_list.append(os.path.join(root, file))
                        else:
                            path_list.append(os.path.join(root, file))

        elif search_mode == 3:

            dirs = [folder for folder in os.listdir(folder_path)]
            for dir_name in dirs:
                full_path = os.path.join(folder_path, dir_name)
                if extension_search_mode == 2:
                    if dir_name.endswith(extension):
                        path_list.append(full_path)
                else:
                    path_list.append(full_path)

        try:
            path_list = randomly_select_files(
                path_list, random_seed, batch_size)
        except Exception as e:
            print(e)

        path_names = extract_file_names(path_list)

        return (path_list, path_names, batch_size,)


N_CLASS_MAPPINGS = {
    "JDCN_AnyFileListRandom": JDCN_AnyFileListRandom,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_AnyFileListRandom": "JDCN_AnyFileListRandom",
}
