"""
Implements logic gate nodes
"""
import re
from .autonode import node_wrapper, get_node_names_mappings, validate, anytype


classes = []
node = node_wrapper(classes)

@node
class LogicGateCompare:
    """
    Returns 1 if input1 > input2, 0 otherwise
    """
    RETURN_TYPES = ("BOOL",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype, {"default": 0.0}),
            "input2": (anytype, {"default": 0.0}),
        }
    }
    FUNCTION = "compareFloat"
    CATEGORY = "Logic Gates"
    custom_name = "ABiggerThanB"
    def compareFloat(self, input1, input2):
        return (True if input1 > input2 else False,)
@node
class LogicGateInvertBasic:
    """
    Inverts 1 to 0 and 0 to 1
    """
    RETURN_TYPES = (anytype,)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype, {"default": 0}),
        }
    }
    FUNCTION = "invert"
    CATEGORY = "Logic Gates"
    custom_name = "Invert Basic"
    def invert(self, input1):
        return (True if not input1 else False,)
@node
class LogicGateNegateValue:
    """
    Inverts x -> -x
    """
    RETURN_TYPES = (anytype,)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype, {"default": 0}),
        }
    }
    FUNCTION = "invertValue"
    CATEGORY = "Logic Gates"
    custom_name = "Negate Value"
    def invertValue(self, input1):
        return (-input1,)
@node
class LogicGateBitwiseShift:
    """
    Shifts input1 by input2 bits
    Only works on integers
    Negative input2 shifts right, positive input2 shifts left
    """
    RETURN_TYPES = ("INT",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": ("INT", {"default": 0}),
            "input2": ("INT", {"default": 0}),
        }
    }
    FUNCTION = "bitwiseShift"
    CATEGORY = "Logic Gates"
    custom_name = "Bitwise Shift"
    def bitwiseShift(self, input1, input2):
        # validate input2
        if abs(input2) > 32:
            raise ValueError("input2 must be between -32 and 32")
        return (input1 << input2,)
@node
class LogicGateBitwiseAnd:
    """
    Bitwise AND of input1 and input2
    Only works on integers
    """
    RETURN_TYPES = ("INT",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": ("INT", {"default": 0}),
            "input2": ("INT", {"default": 0}),
        }
    }
    FUNCTION = "bitwiseAnd"
    CATEGORY = "Logic Gates"
    custom_name = "Bitwise And"
    def bitwiseAnd(self, input1, input2):
        return (input1 & input2,)
@node
class LogicGateBitwiseOr:
    """
    Bitwise OR of input1 and input2
    Only works on integers
    """
    RETURN_TYPES = ("INT",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": ("INT", {"default": 0}),
            "input2": ("INT", {"default": 0}),
        }
    }
    FUNCTION = "bitwiseOr"
    CATEGORY = "Logic Gates"
    custom_name = "Bitwise Or"
    def bitwiseOr(self, input1, input2):
        return (input1 | input2,)
@node
class LogicGateBitwiseXor:
    """
    Bitwise XOR of input1 and input2
    Only works on integers
    """
    RETURN_TYPES = ("INT",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": ("INT", {"default": 0}),
            "input2": ("INT", {"default": 0}),
        }
    }
    FUNCTION = "bitwiseXor"
    CATEGORY = "Logic Gates"
    custom_name = "Bitwise Xor"
    def bitwiseXor(self, input1, input2):
        return (input1 ^ input2,)
@node
class LogicGateBitwiseNot:
    """
    Bitwise NOT of input1
    Only works on integers
    """
    RETURN_TYPES = ("INT",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": ("INT", {"default": 0}),
        }
    }
    FUNCTION = "bitwiseNot"
    CATEGORY = "Logic Gates"
    custom_name = "Bitwise Not"
    def bitwiseNot(self, input1):
        return (~input1,)
@node
class LogicGateCompare:
    """
    Returns 1 if input1 > input2, 0 otherwise
    """
    RETURN_TYPES = ("BOOL",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype, {"default": 0}),
            "input2": (anytype, {"default": 0}),
        }
    }
    FUNCTION = "compareInt"
    CATEGORY = "Logic Gates"
    custom_name = "ABiggerThanB"
    def compareInt(self, input1, input2):
        return (True if input1 > input2 else False,)
@node
class LogicGateCompareString:
    """
    Returns if given regex (1) is found in given string (2)
    """
    RETURN_TYPES = ("BOOL",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "regex": ("STRING", {"default": ""}),
            "input2": ("STRING", {"default": ""}),
        }
    }
    FUNCTION = "compareString"
    CATEGORY = "Logic Gates"
    custom_name = "AContainsB(String)"
    def compareString(self, regex, input2):
        return (True if re.search(regex, input2) else False,)
@node
class StaticNumberInt:
    """
    Returns a static number
    """
    RETURN_TYPES = ("INT",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "number": ("INT", {"default": 0}),
        }
    }
    FUNCTION = "staticNumber"
    CATEGORY = "Logic Gates"
    custom_name = "Static Number Int"
    def staticNumber(self, number):
        return (number,)
@node
class StaticNumberFloat:
    """
    Returns a static number
    """
    RETURN_TYPES = ("FLOAT",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "number": ("FLOAT", {"default": 0.0}),
        }
    }
    FUNCTION = "staticNumber"
    CATEGORY = "Logic Gates"
    custom_name = "Static Number Float"
    def staticNumber(self, number):
        return (number,)
@node
class StaticString:
    """
    Returns a static string
    """
    RETURN_TYPES = ("STRING",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "string": ("STRING", {"default": ""}),
        }
    }
    FUNCTION = "staticString"
    CATEGORY = "Logic Gates"
    custom_name = "Static String"
    def staticString(self, string):
        return (string,)
@node
class LogicGateAnd:
    """
    Returns 1 if all inputs are True, 0 otherwise
    """
    RETURN_TYPES = ("BOOL",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype, {"default": 0.0}),
            "input2": (anytype, {"default": 0.0}),
        }
    }
    FUNCTION = "and_"
    CATEGORY = "Logic Gates"
    custom_name = "AAndBGate"
    def and_(self, input1, input2):
        return (True if input1 and input2 else False,)
@node
class LogicGateOr:
    """
    Returns 1 if any input is True, 0 otherwise
    """
    RETURN_TYPES = ("BOOL",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype, {"default": 0}),
            "input2": (anytype, {"default": 0}),
        }
    }
    FUNCTION = "or_"
    CATEGORY = "Logic Gates"
    custom_name = "AOrBGate"
    def or_(self, input1, input2):
        return (True if input1 and input2 else False,)
@node
class LogicGateEither:
    """
    Returns input1 if condition is true, input2 otherwise
    """
    RETURN_TYPES = (anytype,)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "condition": (anytype, {"default": 0}),
            "input1": (anytype, {"default": ""}),
            "input2": (anytype, {"default": ""}),
        }
    }
    FUNCTION = "either"
    CATEGORY = "Logic Gates"
    custom_name = "ReturnAorBValue"
    def either(self, condition, input1, input2):
        return (input1 if condition else input2,)
@node
class AddNode:
    """
    Returns the sum of the inputs
    """
    RETURN_TYPES = (anytype,)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype, {"default": 0}),
            "input2": (anytype, {"default": 0}),
        }
    }
    FUNCTION = "add"
    CATEGORY = "Logic Gates"
    custom_name = "Add Values"
    def add(self, input1, input2):
        return (input1 + input2,)
@node
class MergeString:
    """
    Returns the concatenation of the inputs
    """
    RETURN_TYPES = ("STRING",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype, {"default": ""}),
            "input2": (anytype, {"default": ""}),
        }
    }
    FUNCTION = "merge"
    CATEGORY = "Logic Gates"
    custom_name = "Merge String"
    def merge(self, input1, input2):
        return (str(input1) + str(input2),)

@node
class ReplaceString:
    """
    Returns the concatenation of the inputs
    """
    RETURN_TYPES = ("STRING",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "String": ("STRING", {"default": ""}),
            "Regex": ("STRING", {"default": ""}),
            "ReplaceWith": ("STRING", {"default": ""}),
        }
    }
    FUNCTION = "replace"
    CATEGORY = "Logic Gates"
    custom_name = "Replace String"
    def replace(self, String, Regex, ReplaceWith):
        # using regex
        return (re.sub(Regex, ReplaceWith, String),)
    
@node
class MemoryNode:
    """
    Stores a value in memory.
    Flip-flop behaviour.
    """
    def __init__(self):
        self.memory_value = None
    RETURN_TYPES = (anytype,)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype, {"default": ""}),
            "flag": (anytype, {"default": 0}),
        }
    }
    FUNCTION = "memory"
    CATEGORY = "Logic Gates"
    custom_name = "Memory String"
    def memory(self, input1, flag):
        if self.memory_value is None or flag:
            self.memory_value = input1
        return (self.memory_value,)



CLASS_MAPPINGS, CLASS_NAMES = get_node_names_mappings(classes)
validate(classes)
