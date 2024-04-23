import os
import glob
import shutil
from PIL import Image,  ImageEnhance
# from server import PromptServer
# from aiohttp import web

def get_files_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Folder does not exist.")
        return []
    files = glob.glob(os.path.join(folder_path, "*"))
    return files

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")

def delete_files_in_folder(folder_path): 
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Failed to delete file '{file_path}': {e}")

def copy_images_and_delete_folder(file_paths, destination_folder, deleting_folder):

    if len(file_paths) <= 0:
        print("Source image path list is empty.")
        return

    if not os.path.isdir(destination_folder):
        print("Destination folder does not exist.")
        return

    delete_files_in_folder(destination_folder)

    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        destination_file_path = os.path.join(destination_folder, file_name)
        shutil.copyfile(file_path, destination_file_path)
        # print(f"Image '{file_name}' copied to '{destination_folder}'.")
    
    delete_files_in_folder(deleting_folder)


def copy_images(file_paths, destination_folder):

    if len(file_paths) <= 0:
        print("Source image path list is empty.")
        return

    if not os.path.isdir(destination_folder):
        print("Destination folder does not exist.")
        return

    delete_files_in_folder(destination_folder)

    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        destination_file_path = os.path.join(destination_folder, file_name)
        shutil.copyfile(file_path, destination_file_path)
        # print(f"Image '{file_name}' copied to '{destination_folder}'.")

def change_opacity(im, opacity):
    assert opacity >= 0 and opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im


def merge_images(image1, image2):
    # Convert images to RGBA mode if not already
    if image1.mode != 'RGBA':
        image1 = image1.convert('RGBA')
    if image2.mode != 'RGBA':
        image2 = image2.convert('RGBA')

    # Ensure both images have 24-bit depth
    image1 = image1.convert('RGB')
    image2 = image2.convert('RGB')

    # Merge the images
    merged_image = Image.alpha_composite(image1, image2)

    return merged_image

def updateProgress(current,max):
    pass
    # client_id = PromptServer.instance.client_id
    # PromptServer.instance.send_sync("jdcnse/progress", { "details": { "value": current, "max": max } }, client_id)
    # print(f"current: {current} max: {max} left: {(current/max)*100}")


def seamless(arr, batch_size, overlap_size, output_folder):

    affected = []
    steps = (len(arr) // batch_size)

    affected.append(f"TOTAL SEAMLESS PROCESSING ROUNDS: {steps-1}")

    for i in range(1, steps):
        affected.append("")
        affected.append("=============================================================================")
        affected.append("")
        affected.append(f"ROUND: {i}/{steps-1}")
        affected.append("")
        select_start_a = (batch_size * i) + (overlap_size * (i-1)) + 1
        select_end_a = select_start_a + overlap_size

        select_start_b = select_end_a
        select_end_b = select_start_b + overlap_size

        merge_this = arr[select_start_a-1:select_end_a-1]
        merge_that = arr[select_start_b-1:select_end_b-1]

        affected.append(f"SET 1: {merge_this[0]} - {merge_this[len(merge_this)-1]}")
        affected.append(f"SET 2: {merge_that[0]} - {merge_that[len(merge_that)-1]}")

        for j in range(len(merge_this)):
            image_path_1 = merge_this[j]
            image_path_2 = merge_that[j]

            image1 = Image.open(image_path_1)
            image2 = Image.open(image_path_2)

            if image1.mode != 'RGBA':
                image1 = image1.convert('RGBA')
            if image2.mode != 'RGBA':
                image2 = image2.convert('RGBA')

            opacity = ((j+1) / (overlap_size))

            image_a = change_opacity(image1, 1 - opacity)

            merge = merge_images(image2, image_a)

            image2_filename = os.path.basename(image_path_2)
            output_path = os.path.join(output_folder, image2_filename)

            os.remove(image_path_1)
            os.remove(image_path_2)
            merge.save(output_path, quality=95)
            current = i+(j/overlap_size)
            max = steps
            updateProgress(current,max)


        # print(f"Batch {i}/{steps-1} completed")

    return affected


class JDCN_SeamlessExperience:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "ImagePaths": ("STRING", {"forceInput": True}),
                "OutputDirectory": ("STRING", {"default": "directory path"}),
                "BatchSize": ("INT", {"default": 0, "min": 0, "max": 9999}),
                "OverlapSize": ("INT", {"default": 0, "min": 0, "max": 9999}),
            },
        }

    FUNCTION = "doit"

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("NewImagePaths", "Log")
    OUTPUT_IS_LIST = (True, False)
    OUTPUT_NODE = True

    def doit(self, ImagePaths, OutputDirectory, BatchSize, OverlapSize):

        input_folder = "./input/jdcn"

        create_folder_if_not_exists(input_folder)

        copy_images(ImagePaths, input_folder)
        input_file_paths = get_files_in_folder(input_folder)
        log = seamless(input_file_paths, BatchSize[0], OverlapSize[0], input_folder)
        file_paths = get_files_in_folder(input_folder)
        copy_images_and_delete_folder(file_paths, OutputDirectory[0], input_folder)
        file_paths = get_files_in_folder(OutputDirectory[0])

        log.append("")
        log.append(f"IMAGES BEFORE: {len(input_file_paths)}")
        log.append("")
        log.append(f"IMAGES AFTER: {len(file_paths)}")

        log_string = '\n'.join(log)

        updateProgress(1,1)

        return (file_paths, log_string)


N_CLASS_MAPPINGS = {
    "JDCN_SeamlessExperience": JDCN_SeamlessExperience,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_SeamlessExperience": "JDCN_SeamlessExperience",
}
