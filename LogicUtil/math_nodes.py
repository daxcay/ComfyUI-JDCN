from .autonode import node_wrapper, get_node_names_mappings, validate, anytype
classes = []
node = node_wrapper(classes)
import math

@node
class MinNode:
    """
    Returns the minimum of two values
    """
    RETURN_TYPES = (anytype,)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype,),
            "input2": (anytype,),
        }
    }
    FUNCTION = "min"
    CATEGORY = "Math"
    custom_name = "Min"
    def min(self, input1, input2):
        return (min(input1, input2),)

@node
class MaxNode:
    """
    Returns the maximum of two values
    """
    RETURN_TYPES = (anytype,)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype,),
            "input2": (anytype,),
        }
    }
    FUNCTION = "max"
    CATEGORY = "Math"
    custom_name = "Max"
    def max(self, input1, input2):
        return (max(input1, input2),)

@node
class RoundNode:
    """
    Rounds a value to the nearest integer
    """
    RETURN_TYPES = ("INT",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype,),
        }
    }
    FUNCTION = "round"
    CATEGORY = "Math"
    custom_name = "Round"
    def round(self, input1):
        return (round(input1),)

@node
class AbsNode:
    """
    Returns the absolute value of a number
    """
    RETURN_TYPES = (anytype,)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype,),
        }
    }
    FUNCTION = "abs"
    CATEGORY = "Math"
    custom_name = "Abs"
    def abs(self, input1):
        return (abs(input1),)

@node
class FloorNode:
    """
    Returns the floor of a number
    """
    RETURN_TYPES = ("INT",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype,),
        }
    }
    FUNCTION = "floor"
    CATEGORY = "Math"
    custom_name = "Floor"
    def floor(self, input1):
        return (math.floor(input1),)

@node
class CeilNode:
    """
    Returns the ceiling of a number
    """
    RETURN_TYPES = ("INT",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype,),
        }
    }
    FUNCTION = "ceil"
    CATEGORY = "Math"
    custom_name = "Ceil"
    def ceil(self, input1):
        return (math.ceil(input1),)

@node
class PowerNode:
    """
    Returns the power of a number
    """
    RETURN_TYPES = (anytype,)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype,),
            "power": (anytype,),
        }
    }
    FUNCTION = "power"
    CATEGORY = "Math"
    custom_name = "Power"
    def power(self, input1, power):
        # validate power with log scale, prevent overflow
        log_val = math.log(abs(input1), 10)
        if log_val * power > 100 or log_val == 0:
            raise OverflowError("Power is too large, exceeds 100 digits")
        return (math.pow(input1, power),)

class ModuloNode:
    """
    Returns the modulo of a number
    """
    RETURN_TYPES = ("INT",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": ("INT",),
            "modulo": ("INT",),
        }
    }
    FUNCTION = "modulo"
    CATEGORY = "Math"
    custom_name = "Modulo"
    def modulo(self, input1, modulo):
        return (input1 % modulo,)

@node
class LogNode:
    """
    Returns the log of a number
    """
    RETURN_TYPES = ("FLOAT",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": ("FLOAT",),
            "base": ("FLOAT",),
        }
    }
    FUNCTION = "log"
    CATEGORY = "Math"
    custom_name = "Log"
    def log(self, input1, base):
        return (math.log(input1, base),)

@node
class MultiplyNode:
    """
    Returns the product of two numbers
    """
    RETURN_TYPES = (anytype,)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype,),
            "input2": (anytype,),
        }
    }
    FUNCTION = "multiply"
    CATEGORY = "Math"
    custom_name = "Multiply"
    def multiply(self, input1, input2):
        return (input1 * input2,)

@node
class DivideNode:
    """
    Returns the quotient of two numbers
    """
    RETURN_TYPES = ("FLOAT",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "input1": (anytype,),
            "input2": (anytype,),
        }
    }
    FUNCTION = "divide"
    CATEGORY = "Math"
    custom_name = "Divide"
    def divide(self, input1, input2):
        if input2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return (input1 / input2,)

validate(classes)
CLASS_MAPPINGS, CLASS_NAMES = get_node_names_mappings(classes)
