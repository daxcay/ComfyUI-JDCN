import glob
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


def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")


def get_files_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Folder does not exist.")
        return []
    files = glob.glob(os.path.join(folder_path, "*"))
    return files


class JDCN_FileMover:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "FilePaths": ("STRING", {"forceInput": True}),
                "OutputDirectory": ("STRING", {"default": "directory path"}),
                "OverwriteFile": ("BOOLEAN", {"default": False}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("NewFilePaths",)
    OUTPUT_IS_LIST = (True,)
    OUTPUT_NODE = True
    FUNCTION = "make_list"
    CATEGORY = "🔵 JDCN 🔵"

    def make_list(self, FilePaths, OutputDirectory, OverwriteFile):

        if len(FilePaths) == 0:
            print("Empty FileName string")
            return ([],)

        create_folder_if_not_exists(OutputDirectory[0])

        for file in FilePaths:
            move_it(file, OutputDirectory[0], OverwriteFile[0])

        file_paths_new = get_files_in_folder(OutputDirectory[0])

        return (file_paths_new,)


N_CLASS_MAPPINGS = {
    "JDCN_FileMover": JDCN_FileMover,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_FileMover": "JDCN_FileMover",
}
