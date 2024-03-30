"""
Converts int / float / boolean
Note that it depends on the order of the conversion
"""
from .autonode import validate, node_wrapper, get_node_names_mappings, anytype
classes = []
node = node_wrapper(classes)

conversion_operators = {
    "Int" : int,
    "Float" : float,
    "Bool" : bool,
    "String" : str
}
def create_class(type_to):
    class_name = "ConvertAny2{}".format(type_to)
    class CustomClass:
        FUNCTION = "convert"
        RETURN_TYPES = (type_to.upper(),)
        CATEGORY = "Conversion"
        custom_name = "Convert to {}".format(type_to)
        @staticmethod
        def convert(input1):
            return (conversion_operators[type_to](input1),)
        @classmethod
        def INPUT_TYPES(cls):
            return {
            "required": {
                "input1": (anytype, {"default": 0.0}),
            }
        }
    CustomClass.__name__ = class_name
    node(CustomClass)
    return CustomClass


@node
class StringListToCombo:
    """
    Converts raw string, separates with separator, then picks the first element or the element at index
    """
    RETURN_TYPES = (anytype,)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "string": ("STRING", {"default": ""}),
            "separator": ("STRING", {"default": "$"}),
        },
        "optional": {
            "index": ("INT", {"default": 0}),
        }
    }
    FUNCTION = "stringListToCombo"
    CATEGORY = "Logic Gates"
    custom_name = "String List to Combo"
    def stringListToCombo(self, string, separator, index = 0):
        if isinstance(string, (float, int, bool)):
            return (string,)
        if separator == "" or separator == None or separator not in string:
            return (string,)
        # check length
        splitted = string.split(separator)
        if index >= len(splitted):
            return (splitted[-1],)
        return (splitted[index],)

@node
class ConvertComboToString:
    """
    Converts raw list to string, separated with separator
    """
    RETURN_TYPES = ("STRING",)
    @classmethod
    def INPUT_TYPES(s):
        return {
        "required": {
            "combo": (anytype, {"default": []}),
            "separator": ("STRING", {"default": "$"}),
        }
    }
    FUNCTION = "convertComboToString"
    CATEGORY = "Logic Gates"
    custom_name = "Convert Combo to String"
    def convertComboToString(self, combo, separator):
        if isinstance(combo, (str, float, int, bool)):
            return (combo,)
        return (separator.join(combo),)

for type_to in conversion_operators:
    create_class(type_to)

CLASS_MAPPINGS, CLASS_NAMES = get_node_names_mappings(classes)
validate(classes)
