from adafruit_bitmap_font import adafruit_bitmap_font
from adafruit_display_text.label import Label

from displayio import Group
import glob
from os import path


class PlaceholderLabel(Label):
    """Add a placeholder text while waiting to retrieve data
    """

    def __init__(self, x, y, font, color, text=None, placeholder=None, glyphs=3):
        super().__init__(font, text=text or placeholder, max_glyphs=glyphs)
        self.x = x
        self.y = y
        self.color = color


class Fonts:
    def __init__(self, *font_names, default=None, font_dir="/fonts")

class DefaultTheme:
    """
    Define the base theme for the display
    """

    # the current working directory (where this file is)
    cwd = ("/" + __file__).rsplit("/", 1)[0]
    font_dir = cwd + "/fonts"

    font_paths = glob.glob(font_dir + "/*.bdf")
    fonts = Fonts(path.splitext(font) for font in font_paths)

    def __init__(self, background_image, font=None, bg_dir="/bgs", color=0xFFFFFF):
        """
        Create a new Base Theme.

        Args:
            background_image (str): Background image file name, with
                the file to be found as a *.bmp file in the bg_dir directory.
            font (str, optional): Which font name to use. Defaults to None.
            bg_dir (str, optional): Background image file directory. Defaults to /bgs.
            color (int, optional): Font color, in hexadecimal. Defaults to 0xFFFFFF.
        """
        self.color = color
        self.font = self.fonts[font] if font else self.fonts.default
        self.bg = "{}/{}.bmp".format(bg_dir, background_image)
        self.display = None
        self.display_pos = None
