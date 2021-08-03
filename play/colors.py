from enum import Enum

class Color(tuple, Enum):
    WHITE = (255, 255, 255)
    YELLOW = (223, 225, 0)
    ORANGE = (255, 191, 0)
    GREEN = (159, 226, 191)
    BLUE = (0, 0, 255)