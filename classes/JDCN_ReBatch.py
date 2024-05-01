def split_into_batches(list, batch_size):
    num_batches = len(list) // batch_size + (len(list) % batch_size != 0)
    batches = []
    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min(start_idx + batch_size, len(list))
        batch = list[start_idx:end_idx]
        batches.append(batch)
    return batches

def batches_to_string(batches):
    string_representation = []
    for batch in batches:
        string_representation.append("\n".join(batch))
    return string_representation


class JDCN_ReBatch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "FileNames": ("STRING", {"forceInput": True}),
                "BatchSize": ("INT", {"default": 1, "min": 1, "max": 9999}),
                "TextList": ("BOOLEAN", {"default": False}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("FilePaths",)
    OUTPUT_IS_LIST = (True,)
    OUTPUT_NODE = True
    FUNCTION = "make_it"
    CATEGORY = "🔵 JDCN 🔵"

    def make_it(self, FileNames, BatchSize, TextList):

        if len(FileNames) == 0:
            print("Empty FileName")
            return ("",)

        batches = split_into_batches(FileNames,BatchSize[0])

        if(TextList[0]): 
            batches = batches_to_string(batches)

        return (batches,)


N_CLASS_MAPPINGS = {
    "JDCN_ReBatch": JDCN_ReBatch,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_ReBatch": "JDCN_ReBatch",
}
