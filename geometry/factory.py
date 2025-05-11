from .circle import Circle
from .triangle import Triangle
from .base import Shape

def create_shape(*args) -> Shape:
    if len(args) == 1:
        return Circle(args[0])
    elif len(args) == 3:
        return Triangle(*args)
    else:
        raise ValueError("Unsupported number of arguments")
