from .shared import Any

any = Any("*")

class JDCN_EnableDisable:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Enable": ("BOOLEAN", {"default": False}),
            },
        }
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("output",)
    FUNCTION = "checkit"
    CATEGORY = "🔵 JDCN 🔵"

    def checkit(self, Enable):
        if Enable:
            return ("enable",)
        else:
            return ("disable",)


N_CLASS_MAPPINGS = {
    "JDCN_EnableDisable": JDCN_EnableDisable,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_EnableDisable": "JDCN_EnableDisable",
}
