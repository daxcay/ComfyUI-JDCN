class JDCN_StringToList:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "string": ("STRING", {"forceInput": True}),
            },
        }

    # INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("list",)
    OUTPUT_IS_LIST = (True,)
    OUTPUT_NODE = True
    FUNCTION = "make_list"
    CATEGORY = "🔵 JDCN 🔵"

    def make_list(self, string):

        if len(string) == 0:
            print("Error in string Variable")
            return ("",)

        file_paths = string.split('\n')

        return (file_paths,)


N_CLASS_MAPPINGS = {
    "JDCN_StringToList": JDCN_StringToList,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_StringToList": "JDCN_StringToList",
}
