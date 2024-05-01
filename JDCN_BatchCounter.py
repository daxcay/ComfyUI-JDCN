class JDCN_BatchCounter:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "Lap": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "Range": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "LapChange": (['fixed', 'increment', 'decrement'],),
                "Log": ("STRING",{ "default": "Log", "multiline": True })
            },
        }

    # INPUT_IS_LIST = True
    RETURN_TYPES = ("INT", "INT", "INT")
    RETURN_NAMES = ("result", "lap", "range")
    OUTPUT_IS_LIST = (False, False, False)
    OUTPUT_NODE = True
    FUNCTION = "do_it"
    
    CATEGORY = "🔵 JDCN 🔵"


    def do_it(self, Lap, Range, LapChange, Log):
        return (Lap*Range, Lap, Range)


N_CLASS_MAPPINGS = {
    "JDCN_BatchCounter": JDCN_BatchCounter,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_BatchCounter": "JDCN_BatchCounter",
}
