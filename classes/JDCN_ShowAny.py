from .shared import Any
any = Any("*")
class JDCN_ShowAny:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "source": (any,),
                "text": ("STRING", {"multiline": True, "default": "output"}),
            },
        }
    RETURN_TYPES = (any,)
    RETURN_NAMES = ("output",)
    FUNCTION = "main"
    CATEGORY = "🔵 JDCN 🔵"
    # OUTPUT_NODE = True
    def main(self, source, text):
        return (source,)    
    
N_CLASS_MAPPINGS = {
    "JDCN_ShowAny": JDCN_ShowAny,
}
N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_ShowAny": "JDCN_ShowAny",
}