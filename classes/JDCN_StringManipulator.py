import random


class JDCN_StringManipulator:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        names_of_separators = [
            'Comma',
            'Semicolon',
            'Pipe',
            'Hyphen',
            'Colon',
            'Period',
            'Question Mark',
            'Exclamation Mark',
            'Space',
            'Tab',
            'Newline',
            'Carriage Return',
            'Form Feed',
            'Vertical Tab',
            'Custom'
        ]

        return {
            "required": {
                "text": ("STRING", {"multiline": True, "default": "concept"}),
                "index": ("INT", {"default": 0, "min": 0}),
                "index_change": (['fixed', 'increment', 'decrement', 'random'],),
                "order": (['toptobottom', 'bottomtotop', 'random'],),
                "separator": (names_of_separators,),
                "custom_separator": ("STRING", {"default": "NA"}),
                "batch_size": ("INT", {"default": 1, "min": 1}),
                "joiner": (names_of_separators,),
                "custom_joiner": ("STRING", {"default": "NA"}),
                "space_before_join": ("BOOLEAN", {"default": False}),
            },
        }

    # INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING", "INT", "INT", "INT")
    RETURN_NAMES = ("text", "index_from", "index_to", "batch_size")
    # OUTPUT_IS_LIST = (True,)
    # OUTPUT_NODE = True
    FUNCTION = "make_list"
    CATEGORY = "🔵 JDCN 🔵"

    def make_list(self, text, index, index_change, order, separator, custom_separator, batch_size, joiner, custom_joiner, space_before_join):

        separators_by_names = {
            'Comma': ',',
            'Semicolon': ';',
            'Pipe': '|',
            'Hyphen': '-',
            'Colon': ':',
            'Period': '.',
            'Question Mark': '?',
            'Exclamation Mark': '!',
            'Space': ' ',
            'Tab': '\t',
            'Newline': '\n',
            'Carriage Return': '\r',
            'Form Feed': '\f',
            'Vertical Tab': '\v',
        }

        separated = []

        if separator == "Custom":
            separated = text.split(custom_separator)
        else:
            separated = text.split(separators_by_names[separator])

        separated = [line.strip() for line in separated]
        selected = None

        if order == "random":
            selected = random.sample(separated, batch_size)
        elif order == "toptobottom":
            selected = separated[index:index + batch_size]
        elif order == "bottomtotop":
            selected = separated[::-1][index:index + batch_size]

        if len(selected) == 0:
            return ("Index error", 0, 0, 0)

        if joiner == "Custom":
            if space_before_join:
                joinwith = custom_joiner+" "
                result = joinwith.join(selected)
            else:
                result = custom_joiner.join(selected)
        else:
            if space_before_join:
                joinwith = separators_by_names[joiner]+" "
                result = joinwith.join(selected)
            else:
                result = separators_by_names[joiner].join(selected)

        return (result, index, index + batch_size, batch_size)


N_CLASS_MAPPINGS = {
    "JDCN_StringManipulator": JDCN_StringManipulator,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_StringManipulator": "JDCN_StringManipulator",
}
