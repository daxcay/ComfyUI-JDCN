class JDCN_ListToString:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "list": ("STRING", {"forceInput": True}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("string",)
    OUTPUT_NODE = True
    FUNCTION = "make_list"
    CATEGORY = "🔵 JDCN 🔵"

    def make_list(self, list):

        if len(list) == 0:
            print("Error in List Variable")
            return ("",)

        file_string_list = '\n'.join(list)

        return (file_string_list,)


N_CLASS_MAPPINGS = {
    "JDCN_ListToString": JDCN_ListToString,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_ListToString": "JDCN_ListToString",
}
