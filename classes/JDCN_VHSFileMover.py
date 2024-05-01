import os
import shutil

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")

def move_it(source_path, destination_dir, overwrite=False):
    try:
        create_folder_if_not_exists(destination_dir)

        filename = os.path.basename(source_path)
        destination_path = os.path.join(destination_dir, filename)
        
        if os.path.exists(destination_path):
            if overwrite:
                shutil.move(source_path, destination_path)
            else:
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
        else:
            shutil.move(source_path, destination_path)
            
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
                "OverwriteFile": ("BOOLEAN", {"default": False}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("FilePaths",)
    OUTPUT_IS_LIST = (True,)
    OUTPUT_NODE = True
    FUNCTION = "make_list"

    CATEGORY = "🔵 JDCN 🔵"

    def make_list(self, FileNames, OutputDirectory, OverwriteFile):

        file_paths = FileNames[0][1]

        if len(file_paths) > 0:
            for file in file_paths:
                move_it(file, OutputDirectory[0], OverwriteFile[0])

        return (file_paths,)


N_CLASS_MAPPINGS = {
    "JDCN_VHSFileMover": JDCN_VHSFileMover,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_VHSFileMover": "JDCN_VHSFileMover",
}
