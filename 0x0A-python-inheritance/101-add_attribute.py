  #!/usr/bin/python3
"""[AddAttribute function]"""


def add_attribute(obj, attr, value):
    """[Add an attribute to a class]"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
