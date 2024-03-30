

import json
import numpy as np

from .exif.exif import read_info_from_image_stealth
from .autonode import node_wrapper, get_node_names_mappings, validate, anytype
import time
import os
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import folder_paths
from comfy.cli_args import args

fundamental_classes = []
fundamental_node = node_wrapper(fundamental_classes)

@fundamental_node
class SleepNodeAny:
    FUNCTION = "sleep"
    RETURN_TYPES = (anytype,)
    CATEGORY = "Misc"
    custom_name = "SleepNode"
    @staticmethod
    def sleep(interval, inputs):
        time.sleep(interval)
        return (inputs,)
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "interval": ("FLOAT", {"default": 0.0}),
            },
            "optional": {
                "inputs": (anytype, {"default": 0.0}),
            }
        }
@fundamental_node
class SleepNodeImage:
    FUNCTION = "sleep"
    RETURN_TYPES = (anytype,)
    CATEGORY = "Misc"
    custom_name = "Sleep (Image tunnel)"
    @staticmethod
    def sleep(interval, image):
        time.sleep(interval)
        return (image,)
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "interval": ("FLOAT", {"default": 0.0}),
                "image": (anytype,),
            }
        }

@fundamental_node
class ErrorNode:
    FUNCTION = "raise_error"
    RETURN_TYPES = ("STRING",)
    CATEGORY = "Misc"
    custom_name = "ErrorNode"
    @staticmethod
    def raise_error(error_msg = "Error"):
        raise Exception("Error: {}".format(error_msg))
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "error_msg": ("STRING", {"default": "Error"}),
            }
        }

@fundamental_node
class DebugComboInputNode:
    FUNCTION = "debug_combo_input"
    RETURN_TYPES = ("STRING",)
    CATEGORY = "Misc"
    custom_name = "Debug Combo Input"
    @staticmethod
    def debug_combo_input(input1):
        print(input1)
        return (input1,)
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input1": (["0", "1", "2"], { "default": "0" }),
            }
        }

# https://github.com/comfyanonymous/ComfyUI/blob/340177e6e85d076ab9e222e4f3c6a22f1fb4031f/custom_nodes/example_node.py.example#L18
@fundamental_node
class TextPreviewNode:
    """
    Displays text in the UI
    """
    FUNCTION = "text_preview"
    RETURN_TYPES = ()
    CATEGORY = "Misc"
    custom_name = "Text Preview"
    RESULT_NODE = True
    OUTPUT_NODE = True

    def text_preview(self, text):
        print(text)
        # below does not work, why?
        return {"ui": {"text": str(text)}}
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": (anytype,{"default": "text", "type" : "output"}),
            }
        }

@fundamental_node
class ParseExifNode:
    """
    Parses exif data from image
    """
    FUNCTION = "parse_exif"
    RETURN_TYPES = ("STRING",)
    CATEGORY = "Misc"
    custom_name = "Parse Exif"
    @staticmethod
    def parse_exif(image):
        return (read_info_from_image_stealth(image),)
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
            }
        }


@fundamental_node
class SaveImageCustomNode:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.prefix_append = ""
        self.compress_level = 4

    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    {"images": ("IMAGE", ),
                     "filename_prefix": ("STRING", {"default": "ComfyUI"}),
                     "subfolder_dir": ("STRING", {"default": ""}),
                     },
                "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"},
                }

    RETURN_TYPES = ("STRING",) #Filename
    FUNCTION = "save_images"

    OUTPUT_NODE = True

    CATEGORY = "image"
    custom_name = "Save Image Custom Node" 

    def save_images(self, images, filename_prefix="ComfyUI",subfolder_dir="", prompt=None, extra_pnginfo=None):
        filename_prefix += self.prefix_append
        output_dir = os.path.join(self.output_dir, subfolder_dir)
        full_output_folder, filename, counter, subfolder, filename_prefix = folder_paths.get_save_image_path(filename_prefix, output_dir, images[0].shape[1], images[0].shape[0])
        results = list()
        for image in images:
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            metadata = None
            if not args.disable_metadata:
                metadata = PngInfo()
                if prompt is not None:
                    metadata.add_text("prompt", json.dumps(prompt))
                if extra_pnginfo is not None:
                    for x in extra_pnginfo:
                        metadata.add_text(x, json.dumps(extra_pnginfo[x]))

            file = f"{filename}_{counter:05}_.png"
            img.save(os.path.join(full_output_folder, file), pnginfo=metadata, compress_level=self.compress_level)
            results.append({
                "filename": file,
                "subfolder": subfolder,
                "type": self.type
            })
            counter += 1

        return { "ui": { "images": results }, "outputs": { "images": file.rstrip('.png') } }

@fundamental_node
class SaveTextCustomNode:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"
        self.prefix_append = ""
        self.compress_level = 4

    @classmethod
    def INPUT_TYPES(s):
        return {"required": 
                    {"text": (anytype, ),
                     "filename_prefix": ("STRING", {"default": "ComfyUI"}),
                     "subfolder_dir": ("STRING", {"default": ""}),
                     "filename": ("STRING", {"default": ""}),
                     },
                }
    
    RETURN_TYPES = ("STRING",) #Filename
    FUNCTION = "save_text"
    custom_name = "Save Text Custom Node"
    CATEGORY = "text"

    def save_text(self, text, filename_prefix="ComfyUI",subfolder_dir="",filename=""):
        text = str(text)
        assert len(text) > 0 and len(filename) > 0, "Text and filename must be non-empty"
        filename_prefix += self.prefix_append
        output_dir = os.path.join(self.output_dir, subfolder_dir)
        filename_merged = filename_prefix + filename + ".txt"
        full_output_folder, subfolder, actual_filename = output_dir, "", filename_merged 
        results = list()
        file = actual_filename
        with open(os.path.join(full_output_folder, file), "w") as f:
            f.write(text)
        results.append({
            "filename": file,
            "subfolder": subfolder,
            "type": self.type
        })
        counter += 1

        return { "ui": { "texts": results }, "outputs": { "images": file.rstrip('.txt') } }
CLASS_MAPPINGS, CLASS_NAMES = get_node_names_mappings(fundamental_classes)
validate(fundamental_classes)
