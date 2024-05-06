import os
import glob
from pickle import TRUE
import shutil
from PIL import Image,  ImageEnhance

def log(msg, tag="INFO"):
    pass
    # print(f"[{tag}]: {msg}")

def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        log(f"Folder '{folder_path}' successfully deleted.")
    except Exception as e:
        log(f"Error deleting folder '{folder_path}': {e}")

def delete_file(file_path):
    try:
        os.remove(file_path)
        log(f"File '{file_path}' successfully deleted.")
    except Exception as e:
        log(f"Error deleting file '{file_path}': {e}")

def get_file_name(file_path):
    return os.path.basename(file_path)

def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        log(f"Folder '{folder_path}' created.")
    else:
        log(f"Folder '{folder_path}' already exists.")


def get_files_in_folder(folder_path):
    if not os.path.isdir(folder_path):
        log("Folder does not exist.")
        return []
    files = glob.glob(os.path.join(folder_path, "*"))
    return files


def copy_folder(source_folder, destination_folder):
    try:
        shutil.copytree(source_folder, destination_folder)
        log(f"Folder '{source_folder}' successfully copied to '{destination_folder}'.")
    except Exception as e:
        log(f"Error copying folder '{source_folder}' to '{destination_folder}': {e}")


def copy_files(source_files, destination_folder):
    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        for source_file in source_files:
            file_name = os.path.basename(source_file)
            destination_path = os.path.join(destination_folder, file_name)
            shutil.copy(source_file, destination_path)
            log(f"File '{source_file}' successfully copied to '{destination_path}'.")
    except Exception as e:
        log(f"Error copying files: {e}")


def readImg(path):
    try:
        image = Image.open(path)
        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        return image
    except Exception as e:
        log(f"Error opening imag file: {e}", "ERROR")


def change_opacity(image, opacity):
    if image.mode != 'RGBA':
        image= image.convert('RGBA')
    alpha = image.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    image.putalpha(alpha)
    return image


def merge_image(a, b):
    if a.mode != 'RGBA':
        a = a.convert('RGBA')
    if b.mode != 'RGBA':
        b = b.convert('RGBA')
    merged_image = Image.alpha_composite(a, b)
    merged_image = merged_image.convert('RGB')
    return merged_image

def makeSeam(imageDirectory, batchSize, overlapSize):

    affected = []

    delete_folder(os.path.join(imageDirectory, "output"))
    paths = get_files_in_folder(imageDirectory)
    create_folder(os.path.join(imageDirectory, "output"))
    copy_files(paths, os.path.join(imageDirectory, "output"))
    paths = get_files_in_folder(os.path.join(imageDirectory, "output"))

    pathsSize = len(paths)
    totalBatchSize = batchSize+overlapSize
    totalLoops = pathsSize // (totalBatchSize)

    #toTread = totalLoops - 1 
    i = 0
    #affected.append(f"TOTAL SEAMLESS PROCESSING ROUNDS: {toTread}")

    while True:
        try:
          

            f = i * totalBatchSize
            t = f + totalBatchSize

            if t > pathsSize:
                break
            
            affected.append("")
            affected.append("=============================================================================")
            affected.append("")
            affected.append(f"ROUND: {i}")
            affected.append("")

            t1 = t - overlapSize
            t2 = t + overlapSize

            toMerge = paths[t1:t2]
            totalSeam = len(toMerge)
           

            for j in range(totalSeam-overlapSize):
                mergeA = readImg(toMerge[j])
                mergeB = readImg(toMerge[j+overlapSize])
                affected.append(f"MERGING: {toMerge[j]} - {toMerge[j+overlapSize]}")
                savingFileName = get_file_name(toMerge[j+overlapSize])
                delete_file(toMerge[j])
                delete_file(toMerge[j+overlapSize])
                changedOpacityMergeA = change_opacity(mergeA, 1 - (j/overlapSize))
                merged = merge_image(mergeB,changedOpacityMergeA)
                outputPath = os.path.join(imageDirectory, "output", savingFileName)
                merged.save(outputPath, quality=95)
            
          
            i= i+1
        except Exception as e:
            break

    newFiles = get_files_in_folder(os.path.join(imageDirectory, "output"))

    affected.append("")
    affected.append(f"IMAGES BEFORE: {pathsSize}")
    affected.append("")
    affected.append(f"IMAGES AFTER: {len(newFiles)}")

    affected = '\n'.join(affected)

    return newFiles, affected

class JDCN_SeamlessExperience:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "inputDirectory": ("STRING", {"default": "directory path"}),
                "BatchSize": ("INT", {"default": 0, "min": 0, "max": 9999}),
                "OverlapSize": ("INT", {"default": 0, "min": 0, "max": 9999}),
            },
        }

    FUNCTION = "doit"

    # INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("NewImagePaths", "Log")
    OUTPUT_IS_LIST = (True, False)
    OUTPUT_NODE = True
    CATEGORY = "🔵 JDCN 🔵"
    
    def doit(self, inputDirectory, BatchSize, OverlapSize):

        paths, log = makeSeam(inputDirectory, BatchSize, OverlapSize)

        return (paths, log)


N_CLASS_MAPPINGS = {
    "JDCN_SeamlessExperience": JDCN_SeamlessExperience,
}

N_DISPLAY_NAME_MAPPINGS = {
    "JDCN_SeamlessExperience": "JDCN_SeamlessExperience",
}
