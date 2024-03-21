def split_into_batches(list, batch_size):
    num_batches = len(list) // batch_size + (len(list) % batch_size != 0)
    batches = []
    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min(start_idx + batch_size, len(list))
        batch = list[start_idx:end_idx]
        batches.append(batch)
    return batches


class JDCN_ReBatch:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "FileNames": ("STRING", {"forceInput": True}),
                "BatchSize": ("INT", {"default": 0, "min": 0, "max": 9999}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("FilePaths",)
    OUTPUT_IS_LIST = (True,)
    OUTPUT_NODE = True
    FUNCTION = "make_it"

    def make_it(self, FileNames, BatchSize):

        if len(FileNames) == 0:
            print("Empty FileName")
            return ("",)

        batch = split_into_batches(FileNames,BatchSize[0])

        return (batch,)


N_CLASS_MAPPINGS = {
    "JDCN_ReBatch": JDCN_ReBatch,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_ReBatch": "JDCN_ReBatch",
}
