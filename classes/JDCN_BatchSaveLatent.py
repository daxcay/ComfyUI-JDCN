import os
import torch
import comfy.utils
from comfy.cli_args import args


def count_files_in_folder(folder_path):
    file_count = 0
    for _, _, files in os.walk(folder_path):
        file_count += len(files)
    return file_count

def save_latent(index,prefix,output_dir,latent):

    padding = str(index).zfill(4)
    file_name = f"{prefix}_{padding}.latent"
    file_path = os.path.join(output_dir, file_name)

    output = {}
    output["latent_tensor"] = latent
    output["latent_format_version_0"] = torch.tensor([])

    comfy.utils.save_torch_file(output, file_path, None)


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
    CATEGORY = "🔵 JDCN 🔵"

    def BatchSave(self, Latents, Directory, FilenamePrefix):
        try:

            Directory = Directory[0]
            FilenamePrefix = FilenamePrefix[0]

            if not os.path.exists(Directory):
                os.makedirs(Directory)

            lastIndex = count_files_in_folder(Directory)
            index = 1

            for latent in Latents:
                save_latent(lastIndex+index,FilenamePrefix,Directory,latent['samples'])
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
