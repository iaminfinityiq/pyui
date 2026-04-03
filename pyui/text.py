from pyui.vector2 import Vector2Int
from pyui.window import Window
from .base_class import Component
from .color import Color
import pygame

pygame.init()

class Text(Component):
    def __init__(
        self,
        position: Vector2Int = Vector2Int(0, 0),
        text: str = "",
        backgroundColor: Color | None = None,
        textColor: Color = Color(255, 255, 255),
        font: str = "Arial",
        fontSize: int = 22,
    ):
        super().__init__(position)
        self.text = text
        self.backgroundColor = backgroundColor
        self.textColor = textColor
        self.font = font
        self.fontSize = fontSize

        font = pygame.font.SysFont(self.font, self.fontSize)
        self.textSurface = font.render(self.text, True, self.textColor.toTuple())
        if self.backgroundColor != None:
            dimensions = self.textSurface.get_rect()
            self.backgroundRect = pygame.Rect(self.position.getX(), self.position.getY(), dimensions.width, dimensions.height)
    
    def Draw(self, wd: Window):
        if self.backgroundColor != None:
            pygame.draw.rect(wd.wd, self.backgroundColor.toTuple(), self.backgroundRect)

        wd.wd.blit(self.textSurface, (self.position.getX(), self.position.getY()))