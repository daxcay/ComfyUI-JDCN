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
                "List": ("STRING", {}),
                "Index": ("INT", {"default": 1, "min": 1, "max": 9999}),
                "Change": (['fixed', 'increment', 'decrement'],)
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("out",)
    OUTPUT_NODE = True
    FUNCTION = "make_list"

    CATEGORY = "🔵 JDCN 🔵"

    def make_list(self, List, Index, Change):

        Index = Index[0] - 1

        if len(List) == 0:
            print("Error in List Variable")
            return None

        if Index < 0 or Index >= len(List):
            print("Error in List Variable")
            return None

        return (List[Index],)


N_CLASS_MAPPINGS = {
    "JDCN_AnyFileSelector": JDCN_AnyFileSelector,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_AnyFileSelector": "JDCN_AnyFileSelector",
}
