import os
import glob
import torch
import numpy as np
from PIL import Image, ImageSequence

from .shared import FILE_EXTENSIONS


def filter_strings(input_list, search_for):
    search_strings = search_for.split(",")
    filtered_list = []
    for string in input_list:
        for search_string in search_strings:
            if search_string.strip() in string:
                filtered_list.append(string)
                break
    return filtered_list

def pickFolders(list):
    filtered_list = []
    for str in list:
        if os.path.isdir(str):
            filtered_list.append(str)    
    return filtered_list


class JDCN_AnyFileListHelper:

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
            "folder"
        ]

        FileExtensions = ["*"]
        FileExtensions.extend(FILE_EXTENSIONS["images"])
        FileExtensions.extend(FILE_EXTENSIONS["audio"])
        FileExtensions.extend(FILE_EXTENSIONS["video"])
        FileExtensions.extend(FILE_EXTENSIONS["text"])

        return {
            "required": {
                "List": ("STRING", {"forceInput": True}),
                "search": ("STRING", {}),
                "filter_by": (FilterBy,),
                "extension": (FileExtensions,),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("out",)
    OUTPUT_IS_LIST = (True,)
    OUTPUT_NODE = True
    FUNCTION = "make_list"

    CATEGORY = "🔵 JDCN 🔵"

    def make_list(self, List, search, filter_by, extension):

        revised = filter_strings(List, search[0])        
        if len(revised) == 0:
            return ([],) 
        
        if filter_by[0] == "folder":
            revised = pickFolders(revised)
        elif filter_by[0] == "*":
            pass
        else:
            revised = filter_strings(revised, ",".join(FILE_EXTENSIONS[filter_by[0]]))

        if len(revised) == 0:
            return ([],)            

        if extension[0] != "*":    
            revised = filter_strings(revised, extension[0])

        if len(revised) == 0:
            return ([],)            

        return (revised,)


N_CLASS_MAPPINGS = {
    "JDCN_AnyFileListHelper": JDCN_AnyFileListHelper,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_AnyFileListHelper": "JDCN_AnyFileListHelper",
}
