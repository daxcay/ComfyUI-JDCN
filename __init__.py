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

from .JDCN_AnyFileList import N_CLASS_MAPPINGS as AnyListMappings, N_DISPLAY_NAME_MAPPINGS as AnyListNameNMappings
from .JDCN_AnyFileListHelper import N_CLASS_MAPPINGS as AnyListHelperMappings, N_DISPLAY_NAME_MAPPINGS as AnyListHelperNameNMappings
from .JDCN_AnyFileSelector import N_CLASS_MAPPINGS as AnyFileSelectorMappings, N_DISPLAY_NAME_MAPPINGS as AnyFileSelectorNameMappings
from .JDCN_AnyFileListRandom import N_CLASS_MAPPINGS as AnyFileListRandomMappings, N_DISPLAY_NAME_MAPPINGS as AnyFileListRandomNameMappings
from .JDCN_ListToString import N_CLASS_MAPPINGS as ListToStringMappings, N_DISPLAY_NAME_MAPPINGS as ListToStringNameMappings
from .JDCN_StringToList import N_CLASS_MAPPINGS as StringToListMappings, N_DISPLAY_NAME_MAPPINGS as StringToListNameMappings
from .JDCN_FileMover import N_CLASS_MAPPINGS as FileMoverMappings, N_DISPLAY_NAME_MAPPINGS as FileMoverNameMappings
from .JDCN_SplitString import N_CLASS_MAPPINGS as SplitStringMappings, N_DISPLAY_NAME_MAPPINGS as SplitStringNameMappings
from .JDCN_BatchImageLoadFromList import N_CLASS_MAPPINGS as BatchImageLoadFromListMappings, N_DISPLAY_NAME_MAPPINGS as BatchImageLoadFromListNameMappings
from .JDCN_BatchLatentLoadFromList import N_CLASS_MAPPINGS as BatchLatentLoadFromListMappings, N_DISPLAY_NAME_MAPPINGS as BatchLatentLoadFromListNameMappings
from .JDCN_BatchLatentLoadFromDir import N_CLASS_MAPPINGS as BatchLatentLoadFromDirMappings, N_DISPLAY_NAME_MAPPINGS as BatchLatentLoadFromDirNameMappings
from .JDCN_BatchSaveLatent import N_CLASS_MAPPINGS as BatchSaveLatentMappings, N_DISPLAY_NAME_MAPPINGS as BatchSaveLatentNameMappings
from .JDCN_SeamlessExperience import N_CLASS_MAPPINGS as SeamlessExperienceMappings, N_DISPLAY_NAME_MAPPINGS as SeamlessExperienceNameMappings
from .JDCN_VHSFileMover import N_CLASS_MAPPINGS as VHSFileMoverMappings, N_DISPLAY_NAME_MAPPINGS as VHSFileMoverNameMappings
from .JDCN_ReBatch import N_CLASS_MAPPINGS as ReBatchMappings, N_DISPLAY_NAME_MAPPINGS as ReBatchNameMappings
from .JDCN_ImageSaver import N_CLASS_MAPPINGS as ImageSaverMappings, N_DISPLAY_NAME_MAPPINGS as ImageSaverNameMappings
from .JDCN_TXTFileSaver import N_CLASS_MAPPINGS as TXTFileSaverMappings, N_DISPLAY_NAME_MAPPINGS as TXTFileSaverNameMappings
from .JDCN_BatchCounter import N_CLASS_MAPPINGS as BatchCounterMappings, N_DISPLAY_NAME_MAPPINGS as BatchCounterNameMappings

from .JDCN_TagManipulatorByImageNames import N_CLASS_MAPPINGS as TagManipulatorByImageNamesMappings, N_DISPLAY_NAME_MAPPINGS as TagManipulatorByImageNamesNameMappings

from .LogicUtil.logic_gates import CLASS_MAPPINGS as LogicMapping, CLASS_NAMES as LogicNames
from .LogicUtil.randomness import CLASS_MAPPINGS as RandomMapping, CLASS_NAMES as RandomNames
from .LogicUtil.conversion import CLASS_MAPPINGS as ConversionMapping, CLASS_NAMES as ConversionNames
from .LogicUtil.math_nodes import CLASS_MAPPINGS as MathMapping, CLASS_NAMES as MathNames
from .LogicUtil.io_node import CLASS_MAPPINGS as IOMapping, CLASS_NAMES as IONames

NODE_CLASS_MAPPINGS = {}
NODE_CLASS_MAPPINGS.update(AnyListMappings)
NODE_CLASS_MAPPINGS.update(AnyListHelperMappings)
NODE_CLASS_MAPPINGS.update(AnyFileSelectorMappings)
NODE_CLASS_MAPPINGS.update(AnyFileListRandomMappings)
NODE_CLASS_MAPPINGS.update(BatchImageLoadFromListMappings)
NODE_CLASS_MAPPINGS.update(BatchLatentLoadFromListMappings)
NODE_CLASS_MAPPINGS.update(BatchLatentLoadFromDirMappings)
NODE_CLASS_MAPPINGS.update(BatchSaveLatentMappings)
NODE_CLASS_MAPPINGS.update(FileMoverMappings)
NODE_CLASS_MAPPINGS.update(ImageSaverMappings)
NODE_CLASS_MAPPINGS.update(ListToStringMappings)
NODE_CLASS_MAPPINGS.update(ReBatchMappings)
NODE_CLASS_MAPPINGS.update(SplitStringMappings)
NODE_CLASS_MAPPINGS.update(StringToListMappings)
NODE_CLASS_MAPPINGS.update(SeamlessExperienceMappings)
NODE_CLASS_MAPPINGS.update(VHSFileMoverMappings)
NODE_CLASS_MAPPINGS.update(TXTFileSaverMappings)
NODE_CLASS_MAPPINGS.update(BatchCounterMappings)
NODE_CLASS_MAPPINGS.update(TagManipulatorByImageNamesMappings)

#Logic Util https://github.com/aria1th/ComfyUI-LogicUtils
NODE_CLASS_MAPPINGS.update(IOMapping)
NODE_CLASS_MAPPINGS.update(LogicMapping)
NODE_CLASS_MAPPINGS.update(RandomMapping)
NODE_CLASS_MAPPINGS.update(ConversionMapping)
NODE_CLASS_MAPPINGS.update(MathMapping)

NODE_DISPLAY_NAME_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS.update(AnyListNameNMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(AnyListHelperNameNMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(AnyFileSelectorNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(AnyFileListRandomNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(BatchImageLoadFromListNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(BatchLatentLoadFromListNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(BatchLatentLoadFromDirNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(BatchSaveLatentNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(FileMoverNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(ImageSaverNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(ListToStringNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(ReBatchNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(SplitStringNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(StringToListNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(SeamlessExperienceNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(VHSFileMoverNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(TXTFileSaverNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(BatchCounterNameMappings)
NODE_DISPLAY_NAME_MAPPINGS.update(TagManipulatorByImageNamesNameMappings)

#Logic Util https://github.com/aria1th/ComfyUI-LogicUtils
NODE_DISPLAY_NAME_MAPPINGS.update(IONames)
NODE_DISPLAY_NAME_MAPPINGS.update(LogicNames)
NODE_DISPLAY_NAME_MAPPINGS.update(RandomNames)
NODE_DISPLAY_NAME_MAPPINGS.update(ConversionNames)
NODE_DISPLAY_NAME_MAPPINGS.update(MathNames)


WEB_DIRECTORY = "./web"