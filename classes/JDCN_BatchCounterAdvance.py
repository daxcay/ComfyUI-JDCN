import math

def getRemaining(lap,range,frames):
    remain = (frames - (lap*range))
    return remain if remain > 0 else 0 

def conditionCheckMinor(lap,range,frames,overlap):
    remain = getRemaining(lap,range,frames)
    final_range = range + overlap + 10
    overlapped_range = range + overlap
    return remain if (remain <= final_range) else overlapped_range

def conditionCheck(lap,range,frames,overlap):
    remain = getRemaining(lap,range,frames)
    condition_check_a = conditionCheckMinor(lap,range,frames,overlap)
    final_range = range + overlap + 10
    condition_check_b = remain + range 
    if(condition_check_b > final_range):
        return condition_check_a
    else:
        return 0

class JDCN_BatchCounterAdvance:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "Lap": ("INT", {"default": 0, "min": 0, "max": 9999}),
                "LapChange": (['fixed', 'increment', 'decrement'],),
                "Range": ("INT", {"default": 1, "min": 1, "max": 9999}),
                "Overlap": ("INT", {"default": 1, "min": 0, "max": 9999}),
                "Frames": ("INT", {"default": 1, "min": 1, "max": 9999}),
            },
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT", "INT", "INT", "INT", "INT")
    RETURN_NAMES = ("Lap", "Range", "FinalRange", "Overlap", "TotalLapsNeeded", "Frames", "SkipFrame", "WithoutSkipFrame")
    FUNCTION = "dobca"

    CATEGORY = "🔵 JDCN 🔵"

    def dobca(self, Lap, LapChange, Range, Frames, Overlap):
    
        finalRange = conditionCheck(Lap, Range, Frames, Overlap)
        SkipFrameWithout = Lap * Range
        SkipFrame = Lap * (Range + Overlap)

        return (Lap, Range, finalRange, Overlap, math.ceil(Frames/Range), Frames, SkipFrame, SkipFrameWithout )

N_CLASS_MAPPINGS = {
    "JDCN_BatchCounterAdvance": JDCN_BatchCounterAdvance,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_BatchCounterAdvance": "JDCN_BatchCounterAdvance",
}
