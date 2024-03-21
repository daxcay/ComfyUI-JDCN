import re
import os
import shutil


def move_image(source_path, destination_dir):
    try:
        filename = os.path.basename(source_path)
        destination_path = os.path.join(destination_dir, filename)
        shutil.move(source_path, destination_path)
        # print(f"Image moved from '{source_path}' to '{destination_path}'")
    except Exception as e:
        print("")
        # print(f"Error: {e}")


def extract_paths_from_string(input_string):
    pattern = r"'((?:[A-Za-z]:)?(?:\\|\\\\)(?:[\w\s\d\-]+(?:\\|\\\\))*[\w\s\d\-]+\.(?:png|mp4|mov|webm|webp|gif))'"
    matches = re.findall(pattern, input_string)
    return matches


class JDCN_VHSFileMover:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "FileNames": ("STRING", {"forceInput": True}),
                "OutputDirectory": ("STRING", {"default": "directory path"}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("FilePaths",)
    OUTPUT_IS_LIST = (True,)
    OUTPUT_NODE = True
    FUNCTION = "make_list"

    def make_list(self, FileNames, OutputDirectory):

        if len(FileNames[0]) == 0:
            print("Empty FileName string")
            return ("",)

        file_paths = extract_paths_from_string(FileNames[0])

        if len(file_paths) > 0:
            for file in file_paths:
                move_image(file, OutputDirectory[0])

        return (file_paths,)


N_CLASS_MAPPINGS = {
    "JDCN_VHSFileMover": JDCN_VHSFileMover,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_VHSFileMover": "JDCN_VHSFileMover",
}
