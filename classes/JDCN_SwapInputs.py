from .shared import Any

any = Any("*")

class JDCN_SwapInputs:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "inputA": (any,),
                "inputB": (any,),
                "SwapIT": ("BOOLEAN", {"default": False}),
            },
        }
    RETURN_TYPES = (any, any,)
    RETURN_NAMES = ("outputA", "outputB",)
    FUNCTION = "swapit"
    CATEGORY = "🔵 JDCN 🔵"

    def swapit(self, inputA, inputB, SwapIT):
        if SwapIT:
            return (inputB, inputA,)
        else:
            return (inputA, inputB,)


N_CLASS_MAPPINGS = {
    "JDCN_SwapInputs": JDCN_SwapInputs,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_SwapInputs": "JDCN_SwapInputs",
}