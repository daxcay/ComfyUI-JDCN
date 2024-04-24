import os
import json
import json
import numpy as np
from PIL import Image
from PIL.PngImagePlugin import PngInfo
from comfy.cli_args import args
import psutil


def count_files_in_folder(folder_path):
    file_count = 0
    for _, _, files in os.walk(folder_path):
        file_count += len(files)
    return file_count

def is_folder_open(directory):
    for proc in psutil.process_iter():
        try:
            if proc.name() == "explorer.exe":
                if directory.lower() in [f.path.lower() for f in proc.open_files()]:
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

class JDCN_ImageSaver:

    def __init__(self):
        self.compression = 4

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Images": ("IMAGE",),
                "Directory": ("STRING", {}),
                "FilenamePrefix": ("STRING", {"default": "Image"}),
                "OpenOutputDirectory": ("BOOLEAN", {"default": False}),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
        }

    RETURN_TYPES = ()
    FUNCTION = "BatchSave"
    OUTPUT_NODE = True
    CATEGORY = "JDCN"

    def BatchSave(self, Images, Directory, FilenamePrefix, OpenOutputDirectory, prompt=None, extra_pnginfo=None):

        try:

            Directory = Directory
            FilenamePrefix = FilenamePrefix

            if not os.path.exists(Directory):
                os.makedirs(Directory)

            lastIndex = count_files_in_folder(Directory)
            index = 1

            for image in Images:
                image = image.cpu().numpy()
                image = (image * 255).astype(np.uint8)
                img = Image.fromarray(image)
                metadata = None
                if not args.disable_metadata:
                    metadata = PngInfo()
                    if prompt is not None:
                        metadata.add_text("prompt", json.dumps(prompt))
                    if extra_pnginfo is not None:
                        for x in extra_pnginfo:
                            metadata.add_text(x, json.dumps(extra_pnginfo[x]))
                
                padding = str(lastIndex+index).zfill(4)
                file_name = f"{FilenamePrefix}_{padding}.png"
                file_path = os.path.join(Directory, file_name)
                img.save(file_path, pnginfo=metadata, compress_level=self.compression)
                index = index + 1

            if(OpenOutputDirectory):
                try:
                    os.system(f'explorer "{Directory}"')  
                    os.system(f'open "{Directory}"')    
                    os.system(f'xdg-open "{Directory}"')
                except Exception as e:
                    print(f"Error opening directory: {e}")

        except Exception as e:
            print(f"Error saving image: {e}")

        return ()


N_CLASS_MAPPINGS = {
    "JDCN_ImageSaver": JDCN_ImageSaver,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_ImageSaver": "JDCN_ImageSaver",
}
