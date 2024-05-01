import math

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
                "Overlap": ("INT", {"default": 1, "min": 1, "max": 9999}),
                "Frames": ("INT", {"default": 1, "min": 1, "max": 9999}),
            },
        }

    RETURN_TYPES = ("INT", "INT", "INT", "INT", "INT", "INT", "INT", "INT")
    RETURN_NAMES = ("Lap", "Range", "FinalRange", "Overlap", "TotalLapsNeeded", "Frames", "SkipFrame", "WithoutSkipFrame")
    FUNCTION = "dobca"

    CATEGORY = "🔵 JDCN 🔵"

    def dobca(self, Lap, LapChange, Range, Frames, Overlap):

        try:
        
            finalRange = Range + Overlap
            totalLaps = math.ceil(Frames/Range)

            extra = Frames % Range
            extraLap = 0
            SkipFrame = 0
            SkipFrameWithout = 0

            if(extra > (Overlap*2)):
                extraLap = 1

            if(Lap <= totalLaps):
                SkipFrame = (finalRange * Lap) - (Overlap * (Lap - 1)) if Lap > 0 else 0            
                SkipFrameWithout = Range * Lap        
                if Lap == totalLaps and extra <= (Overlap*2) and extraLap == 0:
                    SkipFrame += extra
                    SkipFrameWithout += extra
                    finalRange += extra
                    Overlap = 0        
            elif extraLap > 0 and Lap == (totalLaps + extraLap):
                lf = Lap - 1
                SkipFrame = (finalRange * lf) - (Overlap * (lf - 1)) if lf > 0 else 0
                SkipFrameWithout = Range * lf
                SkipFrame += extra
                SkipFrameWithout += extra
                finalRange = extra
                Overlap = 0
            else:
                raise ValueError("Err")
            
        except ValueError as e:
            print(e)

        return (Lap, Range, finalRange, Overlap, (totalLaps+extraLap), Frames, SkipFrame, SkipFrameWithout )


N_CLASS_MAPPINGS = {
    "JDCN_BatchCounterAdvance": JDCN_BatchCounterAdvance,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_BatchCounterAdvance": "JDCN_BatchCounterAdvance",
}
