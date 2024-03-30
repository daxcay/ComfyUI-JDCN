
def get_node_names_mappings(classes):
    node_names = {}
    node_classes = {}
    for cls in classes:
        # check if "custom_name" attribute is set
        if hasattr(cls, "custom_name"):
            node_names[cls.__name__] = cls.custom_name
            node_classes[cls.__name__] = cls
    return node_classes, node_names

def node_wrapper(container):
    def wrap_class(cls):
        container.append(cls)
        return cls
    return wrap_class

def validate(container):
    # check if "custom_name", "FUNCTION", "INPUT_TYPES", "RETURN_TYPES", "CATEGORY" attributes are set
    for cls in container:
        for attr in ["FUNCTION", "INPUT_TYPES", "RETURN_TYPES", "CATEGORY"]:
            if not hasattr(cls, attr):
                raise Exception("Class {} doesn't have attribute {}".format(cls.__name__, attr))
            
class AllTrue(str):
    def __init__(self, representation=None) -> None:
        self.repr = representation
        pass
    def __ne__(self, __value: object) -> bool:
        return False
    # isinstance, jsonserializable hijack
    def __instancecheck__(self, instance):
        return True
    def __subclasscheck__(self, subclass):
        return True
    def __bool__(self):
        return True
    def __str__(self):
        return self.repr
    # jsonserializable hijack
    def __jsonencode__(self):
        return self.repr
    def __repr__(self) -> str:
        return self.repr
    def __eq__(self, __value: object) -> bool:
        return True
anytype = AllTrue("*") # when a != b is called, it will always return False
