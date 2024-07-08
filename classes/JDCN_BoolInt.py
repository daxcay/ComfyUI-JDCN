class JDCN_BoolInt:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Boolean": ("BOOLEAN", {"default": False}),
            },
        }
    RETURN_TYPES = ("BOOLEAN", "INT",)
    RETURN_NAMES = ("boolean", "int",)
    FUNCTION = "checkit"
    CATEGORY = "🔵 JDCN 🔵"

    def checkit(self, Boolean):
        if Boolean:
            return (True,1,)
        else:
            return (False,0,)


N_CLASS_MAPPINGS = {
    "JDCN_BoolInt": JDCN_BoolInt,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_BoolInt": "JDCN_BoolInt",
}
