import comfy
import folder_paths


class JDCN_AnyCheckpointLoader:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": {
                "ckpt_path": ("STRING", {"default": "undefined"}),
                "config_path": ("STRING", {"default": "Optional"}),
                "embedding_folder": ("STRING", {"default": "Optional"}),
            },
        }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    FUNCTION = "make_list"

    CATEGORY = "🔵 JDCN 🔵"

    def make_list(self, ckpt_path, config_path, embedding_folder):

        guess = 0
        
        if embedding_folder == "Optional":
            embedding_folder = folder_paths.get_folder_paths("embeddings")

        if config_path == "Optional":
            guess = 1
        
        if guess == 0:
            return comfy.sd.load_checkpoint(config_path, ckpt_path, output_vae=True, output_clip=True, embedding_directory=embedding_folder)
        else:
            out = comfy.sd.load_checkpoint_guess_config(ckpt_path, output_vae=True, output_clip=True, embedding_directory=embedding_folder)
            return out[:3]


N_CLASS_MAPPINGS = {
    "JDCN_AnyCheckpointLoader": JDCN_AnyCheckpointLoader,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_AnyCheckpointLoader": "JDCN_AnyCheckpointLoader",
}
