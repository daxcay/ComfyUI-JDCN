# By Jerry Davos & Daxton Caylor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to
# deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""
@author: Daxton Caylor & Jerry Davos
@title: ComfyUI-JDCN
@nickname: ComfyUI-JDCN
@description: Custom Utility Nodes for Artists, Designers and Animators.
"""

from .JDCN_AnyFileList import N_CLASS_MAPPINGS as AnyListMappins, N_DISPLAY_NAME_MAPPINGS as AnyListNameNMappings
from .JDCN_ListToString import N_CLASS_MAPPINGS as ListToStringMappins, N_DISPLAY_NAME_MAPPINGS as ListToStringNameMappings
from .JDCN_StringToList import N_CLASS_MAPPINGS as StringToListMappins, N_DISPLAY_NAME_MAPPINGS as StringToListNameMappings
from .JDCN_AnyFileSelector import N_CLASS_MAPPINGS as AnyFileSelectorMappins, N_DISPLAY_NAME_MAPPINGS as AnyFileSelectorNameMappings
from .JDCN_BatchImageLoadFromList import N_CLASS_MAPPINGS as BatchImageLoadFromListMappins, N_DISPLAY_NAME_MAPPINGS as BatchImageLoadFromListNameMappings
from .JDCN_BatchLatentLoadFromDir import N_CLASS_MAPPINGS as BatchLatentLoadFromDirMappins, N_DISPLAY_NAME_MAPPINGS as BatchLatentLoadFromDirNameMappings
from .JDCN_BatchSaveLatent import N_CLASS_MAPPINGS as BatchSaveLatentMappins, N_DISPLAY_NAME_MAPPINGS as BatchSaveLatentNameMappings
from .JDCN_SeamlessExperience import N_CLASS_MAPPINGS as SeamlessExperienceMappins, N_DISPLAY_NAME_MAPPINGS as SeamlessExperienceNameMappings
from .JDCN_VHSFileMover import N_CLASS_MAPPINGS as VHSFileMoverMappins, N_DISPLAY_NAME_MAPPINGS as VHSFileMoverNameMappings
from .JDCN_ReBatch import N_CLASS_MAPPINGS as ReBatchMappins, N_DISPLAY_NAME_MAPPINGS as ReBatchNameMappings
from .JDCN_FileMover import N_CLASS_MAPPINGS as FileMoverMappins, N_DISPLAY_NAME_MAPPINGS as FileMoverNameMappings
from .JDCN_SplitString import N_CLASS_MAPPINGS as SplitStringMappins, N_DISPLAY_NAME_MAPPINGS as SplitStringNameMappings
from .JDCN_ImageSaver import N_CLASS_MAPPINGS as ImageSaverMappins, N_DISPLAY_NAME_MAPPINGS as ImageSaverNameMappings

NODE_CLASS_MAPPINGS = {}
NODE_CLASS_MAPPINGS.update(AnyListMappins)
NODE_CLASS_MAPPINGS.update(ListToStringMappins)
NODE_CLASS_MAPPINGS.update(StringToListMappins)
NODE_CLASS_MAPPINGS.update(AnyFileSelectorMappins)
NODE_CLASS_MAPPINGS.update(BatchImageLoadFromListMappins)
NODE_CLASS_MAPPINGS.update(BatchLatentLoadFromDirMappins)
NODE_CLASS_MAPPINGS.update(BatchSaveLatentMappins)
NODE_CLASS_MAPPINGS.update(SeamlessExperienceMappins)
NODE_CLASS_MAPPINGS.update(VHSFileMoverMappins)
NODE_CLASS_MAPPINGS.update(ReBatchMappins)
NODE_CLASS_MAPPINGS.update(FileMoverMappins)
NODE_CLASS_MAPPINGS.update(SplitStringMappins)
NODE_CLASS_MAPPINGS.update(ImageSaverMappins)

NODE_DISPLAY_NAME_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS.update(AnyListNameNMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(ListToStringNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(StringToListNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(AnyFileSelectorNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(BatchImageLoadFromListNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(BatchLatentLoadFromDirNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(BatchSaveLatentNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(SeamlessExperienceNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(VHSFileMoverNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(ReBatchNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(FileMoverNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(SplitStringNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(ImageSaverNameMappings)

WEB_DIRECTORY = "./web"