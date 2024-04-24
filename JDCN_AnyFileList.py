import os
import glob

from .shared import FILE_EXTENSIONS

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


class JDCN_AnyFileList:

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
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "INT",)
    RETURN_NAMES = ("PathList", "NameList", "Total")
    OUTPUT_IS_LIST = (True, True, False)
    OUTPUT_NODE = True
    FUNCTION = "make_list"

    CATEGORY = "JDCN"

    def make_list(self, folder_path, filter_by, extension):

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

        path_names = []
        path_list = []
        total = 0

        if search_mode == 1:

            dirs = [folder for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]
            for dir_name in dirs:
                full_path = os.path.join(folder_path, dir_name)
                path_names.append(dir_name)
                path_list.append(full_path)
                total = total + 1

            return (path_list, path_names, total,)

        elif search_mode == 2:

            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_name, file_extension = os.path.splitext(file)
                    if file_extension in FILE_EXTENSIONS[filter_by]:
                        if extension_search_mode == 2:
                            if file.endswith(extension):
                                path_names.append(file_name)
                                path_list.append(os.path.join(root, file))
                                total = total+1
                        else:
                            path_names.append(file_name)
                            path_list.append(os.path.join(root, file))
                            total = total+1

            return (path_list, path_names, total,)

        elif search_mode == 3:

            dirs = [folder for folder in os.listdir(folder_path)]
            for dir_name in dirs:
                full_path = os.path.join(folder_path, dir_name)
                if extension_search_mode == 2:
                    if dir_name.endswith(extension):
                        path_names.append(dir_name)
                        path_list.append(full_path)
                        total = total+1
                else:
                    path_names.append(dir_name)
                    path_list.append(full_path)
                    total = total+1

            return (path_list, path_names, total,)


N_CLASS_MAPPINGS = {
    "JDCN_AnyFileList": JDCN_AnyFileList,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_AnyFileList": "JDCN_AnyFileList",
}
