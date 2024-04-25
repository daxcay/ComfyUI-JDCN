import os


def append_text(tags, combined_texts):
    tags_list = tags.split(',')
    temp_tags = []
    for tag in tags_list:
        t = tag.strip()
        temp_tags.append(t)

    tags_list = temp_tags

    text_pos_list = [text_pos.strip().split()
                     for text_pos in combined_texts.split(',')]

    for text_pos in text_pos_list:
        num_pos = len(text_pos)-1
        text = " ".join(text_pos[0:num_pos])
        pos = int(text_pos[num_pos])
        if pos == 0:
            tags_list.insert(0, text)
        else:
            tags_list.insert(pos, text)

    new_tags = ', '.join(tags_list)

    return new_tags


def save_file(filename, output_dir, content, mode='Overwrite'):
    os.makedirs(output_dir, exist_ok=True)
    file_path = os.path.join(output_dir, filename)

    if mode == 'SaveNew':
        counter = 0
        while os.path.exists(file_path):
            counter += 1
            file_path = os.path.join(
                output_dir, f"{os.path.splitext(filename)[0]}_{counter}{os.path.splitext(filename)[1]}")
    elif mode == 'Merge' and os.path.exists(file_path):
        with open(file_path, 'a') as file:
            file.write(content)
        print(f"Content appended successfully to {file_path}")
        return
    elif mode == 'Overwrite' and os.path.exists(file_path):
        os.remove(file_path)
    elif mode == 'MergeAndSaveNew' and os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_content = file.read()
        content = existing_content + content
        counter = 0
        while os.path.exists(file_path):
            counter += 1
            file_path = os.path.join(
                output_dir, f"{os.path.splitext(filename)[0]}_{counter}{os.path.splitext(filename)[1]}")

    with open(file_path, 'w') as file:
        file.write(content)
    print(f"File saved successfully at {file_path}")


def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None


def read_files_from_directory(file_names, directory):
    file_contents = {}
    try:
        for name in file_names:
            file_path = os.path.join(directory, name + ".txt")
            if os.path.isfile(file_path):
                content = read_text_file(file_path)
                if content is not None:
                    file_contents[name] = content
            else:
                print(
                    f"Warning: File '{name}.txt' not found in directory '{directory}'.")
    except Exception as e:
        print(f"Error: {e}")
    return file_contents


class JDCN_TagManipulatorByImageNames:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ImageNames": ("STRING", {"forceInput": True}),
                "TagsDirectory": ("STRING", {"default": "directory path"}),
                "Backup": ("BOOLEAN", {"default":False}),
                "Captions": ("STRING", {"multiline": True, "default": "concept"}),
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ()
    FUNCTION = "SaveIT"
    OUTPUT_NODE = True

    CATEGORY = "JDCN"

    def SaveIT(self, ImageNames, TagsDirectory, Captions, Backup):
        try:

            backup_file_path = os.path.join(TagsDirectory[0], "backup")
            os.makedirs(backup_file_path, exist_ok=True)
            
            Contents = read_files_from_directory(ImageNames, TagsDirectory[0])

            if Backup[0]:
                for name in ImageNames:
                    save_file(f"{name}.txt",backup_file_path,Contents[name],"Overwrite")

            for name in ImageNames:
                Contents[name] = append_text(Contents[name], Captions[0])

            for name in ImageNames:
                save_file(f"{name}.txt",TagsDirectory[0],Contents[name],"Overwrite")

        except Exception as e:
            print(f"Error saving: {e}")

        return ()


N_CLASS_MAPPINGS = {
    "JDCN_TagManipulatorByImageNames": JDCN_TagManipulatorByImageNames,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_TagManipulatorByImageNames": "JDCN_TagManipulatorByImageNames",
}
