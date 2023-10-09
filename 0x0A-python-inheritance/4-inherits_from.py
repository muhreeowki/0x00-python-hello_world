"""
Module that contains inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Function that returns True if the object is an
    instance of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False
    """
    return True if \
        type(obj) in a_class.__subclasses__() or a_class.__bases__ else False
