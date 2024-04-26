def split_string(main_string, search_string, from_rear=False, occurrence=1, incs=False):
    if from_rear:
        index = main_string.rfind(search_string)
    else:
        index = main_string.find(search_string)
    if index == -1:
        return main_string, "", -1
    for _ in range(occurrence - 1):
        if from_rear:
            index = main_string.rfind(search_string, 0, index)
        else:
            index = main_string.find(search_string, index + len(search_string))
        if index == -1:
            return main_string, "", -1
    front = main_string[:index]
    rear = main_string[index + len(search_string):]
    if incs:
        front += search_string
    
    return front, rear, index


class JDCN_SplitString:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "MainString": ("STRING", {"forceInput": True}),
                "SearchFor": ("STRING", {}),
                "StartFrom": (['front', 'rear'],),
                "Occurence": ("INT", {"default": 1, "min": 1, "max": 9999}),
                "IncludeSearchFor": ("BOOLEAN", {"default": False}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "INT")
    RETURN_NAMES = ("Suffix", "Prefix", "FoundAt")
    FUNCTION = "dosplitit"

    CATEGORY = "🔵 JDCN 🔵"

    def dosplitit(self, MainString, SearchFor, StartFrom, Occurence, IncludeSearchFor):

        if len(MainString) == 0:
            return ("", "", 0)
        if len(SearchFor) == 0:
            return ("", "", 0) 

        from_rear = False
        if StartFrom == "rear":
            from_rear = True

        suffix, prefix, foundat = split_string(MainString, SearchFor, from_rear, Occurence, IncludeSearchFor)

        return (suffix, prefix, foundat)


N_CLASS_MAPPINGS = {
    "JDCN_SplitString": JDCN_SplitString,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_SplitString": "JDCN_SplitString",
}
