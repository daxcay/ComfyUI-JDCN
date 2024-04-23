import os


def save_file(filename, output_dir, content, mode='new'):
    """
    Saves content to a file in the specified directory.

    Args:
    filename (str): The name of the file to be created.
    output_dir (str): The directory where the file will be saved.
    content (str): The content to be written to the file.
    mode (str): The mode of saving the file. Possible options are 'append', 'overwrite', or 'new'.

    Returns:
    None
    """
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)
    
    if mode == 'new':
        counter = 0
        while os.path.exists(file_path):
            counter += 1
            file_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}_{counter}{os.path.splitext(filename)[1]}")
    elif mode == 'append' and os.path.exists(file_path):
        with open(file_path, 'a') as file:
            file.write(content)
        print(f"Content appended successfully to {file_path}")
        return
    elif mode == 'overwrite' and os.path.exists(file_path):
        os.remove(file_path)
    
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File saved successfully at {file_path}")

class JDCN_TXTFileSaver:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "content": ("STRING",{"forceInput": True}),
                "file_name": ("STRING",{"forceInput": True}),
                "directory": ("STRING", {"default": "directory path"}),
                "mode": (['append','overwrite','new'],),
            },
        }

    # INPUT_IS_LIST = True
    RETURN_TYPES = ()
    FUNCTION = "SaveIT"
    OUTPUT_NODE = True

    def SaveIT(self, content, file_name, directory, mode):
        try:

            if not os.path.exists(directory):
                os.makedirs(directory)

            save_file(f"{file_name}.txt", directory, content, mode)

        except Exception as e:
            print(f"Error saving: {e}")

        return ()


N_CLASS_MAPPINGS = {
    "JDCN_TXTFileSaver": JDCN_TXTFileSaver,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_TXTFileSaver": "JDCN_TXTFileSaver",
}
