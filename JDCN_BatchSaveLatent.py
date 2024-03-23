import os
import torch
import json
import comfy.utils
import folder_paths
from comfy.cli_args import args


def count_files_in_folder(folder_path):
    file_count = 0
    for _, _, files in os.walk(folder_path):
        file_count += len(files)
    return file_count


class JDCN_BatchSaveLatent:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "Latents": ("LATENT",),
                "Directory": ("STRING", {}),
                "FilenamePrefix": ("STRING", {"default": "Latent"})
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ()
    FUNCTION = "BatchSave"
    OUTPUT_NODE = True

    def BatchSave(self, Latents, Directory, FilenamePrefix):
        try:

            Directory = Directory[0]
            FilenamePrefix = FilenamePrefix[0]

            if not os.path.exists(Directory):
                os.makedirs(Directory)

            lastIndex = count_files_in_folder(Directory)
            index = 1

            print(Latents)

            for latent in Latents:
                output = {}
                fill = str(lastIndex+index).zfill(4)
                file = f"{FilenamePrefix}_{fill}.latent"
                file = os.path.join(Directory, file)
                output["latent_tensor"] = latent["samples"]
                output["latent_format_version_0"] = torch.tensor([])
                comfy.utils.save_torch_file(output, file)
                index=index+1

        except Exception as e:
            print(f"Error saving latent: {e}")

        return ()


N_CLASS_MAPPINGS = {
    "JDCN_BatchSaveLatent": JDCN_BatchSaveLatent,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_BatchSaveLatent": "JDCN_BatchSaveLatent",
}
