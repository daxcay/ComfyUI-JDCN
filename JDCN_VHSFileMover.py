import re
import os
import shutil

def move_it(source_path, destination_dir):
    try:
        filename = os.path.basename(source_path)
        destination_path = os.path.join(destination_dir, filename)        
        if os.path.exists(destination_path):
            base, ext = os.path.splitext(filename)
            i = 1
            while True:
                new_filename = f"{base}_{i}{ext}"
                new_destination_path = os.path.join(destination_dir, new_filename)
                if not os.path.exists(new_destination_path):
                    destination_path = new_destination_path
                    break
                i += 1        
        shutil.move(source_path, destination_path)
        print(f"Image moved from '{source_path}' to '{destination_path}'")
    except Exception as e:
        print(f"Error: {e}")

class JDCN_VHSFileMover:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "FileNames": ("VHS_FILENAMES", {}),
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

        file_paths = FileNames[0][1]

        if len(file_paths) > 0:
            for file in file_paths:
                move_it(file, OutputDirectory[0])

        return (file_paths,)


N_CLASS_MAPPINGS = {
    "JDCN_VHSFileMover": JDCN_VHSFileMover,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_VHSFileMover": "JDCN_VHSFileMover",
}
