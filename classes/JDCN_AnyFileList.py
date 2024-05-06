import os

from .shared import FILE_EXTENSIONS

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
                "deep_search": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "INT",)
    RETURN_NAMES = ("PathList", "NameList", "Total")
    OUTPUT_IS_LIST = (True, True, False)
    OUTPUT_NODE = True
    FUNCTION = "make_list"

    CATEGORY = "🔵 JDCN 🔵"

    def make_list(self, folder_path, filter_by, extension, deep_search):

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

            return (file_paths, file_names, total)

        except Exception as e:
            print(f"An error occurred: {e}")
            return ([], [], 0)


N_CLASS_MAPPINGS = {
    "JDCN_AnyFileList": JDCN_AnyFileList,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_AnyFileList": "JDCN_AnyFileList",
}
