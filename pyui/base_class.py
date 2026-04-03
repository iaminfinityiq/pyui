from .vector2 import Vector2Int
from .window import Window

class Component:
    def __init__(
        self,
        position: Vector2Int = Vector2Int(0, 0)
    ):
        self.position = position
    
    def Draw(self, wd: Window):
        pass