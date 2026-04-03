from pyui.window import Window
from pyui.vector2 import Vector2Int
from pyui.text import Text
from pyui.color import Color
from pyui.image import Image

if __name__ == "__main__":
    wd = Window(size=Vector2Int(1000, 1000), title="your mom")

    # All the UI goes in here
    wd.add_components(Text(position=Vector2Int(100, 100), text="Hello Fluentix", backgroundColor=Color(255, 0, 0), font="Consolas"))
    wd.add_components(Image(position=Vector2Int(0, 0), imagePath="assets/nglam.png", imageSize=Vector2Int(1000, 1000)))

    wd.run()