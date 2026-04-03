import pygame
from .vector2 import Vector2Int

class Window:
    def __init__(
        self,
        size: Vector2Int = Vector2Int(500, 500),
        title: str = "pyui",
        fps: int = 60
    ):
        self.size = size
        self.title = title
        self.fps = fps
        self.components = []
    
    def add_components(self, component):
        self.components += [component]

    def run(self):
        pygame.init()

        self.wd = pygame.display.set_mode((self.size.getX(), self.size.getY()))
        pygame.display.set_caption(self.title)

        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.wd.fill((0, 0, 0))
            for component in self.components:
                component.Draw(self)

            pygame.display.flip()
            clock.tick(self.fps)
        
        pygame.quit()