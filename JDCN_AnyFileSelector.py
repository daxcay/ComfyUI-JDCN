import os
import numpy as np

class AlwaysEqualProxy(str):
    def __eq__(self, _):
        return True

    def __ne__(self, _):
        return False

class JDCN_AnyFileSelector:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "list": ("STRING", {"forceInput": True}),
                "index": ("INT", {"default": 0, "min": 0, "max": 9999}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("out",)
    OUTPUT_NODE = True
    FUNCTION = "make_list"

    def make_list(self, list, index):

        index = index[0]

        if len(list) == 0:
            print("Error in List Variable")
            return None
        
        if index < 0 or index >= len(list):
            print("Error in List Variable")
            return None

        return (list[index],)

N_CLASS_MAPPINGS = {
    "JDCN_AnyFileSelector": JDCN_AnyFileSelector,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_AnyFileSelector": "JDCN_AnyFileSelector",
}
