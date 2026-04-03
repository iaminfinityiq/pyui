from pyui.vector2 import Vector2Int
from pyui.window import Window
from .base_class import Component
import pygame
pygame.init()

class Image(Component):
    def __init__(
        self,
        position: Vector2Int = Vector2Int(0, 0),
        imagePath: str = "",
        imageSize: Vector2Int = Vector2Int(0, 0)
    ):
        super().__init__(position)
        self.imagePath = imagePath
        self.imageSize = imageSize
    
    def Draw(self, wd: Window):
        image = pygame.image.load(self.imagePath).convert()
        image = pygame.transform.scale(image, (self.imageSize.getX(), self.imageSize.getY()))
        wd.wd.blit(image, (self.position.getX(), self.position.getY()))