from epd import EPD
from text_render.text_render import draw_paragraph

from PIL import Image, ImageFont, ImageDraw, ImageChops

VERTICAL_MODE = 0
HORIZONTAL_MODE = 1

class Display:
    def __init__(self, mode=VERTICAL_MODE, line_width=20):
        self.mode = mode
        self.line_width = line_width
        self._epd = EPD()
        self._epd.init()
   
        self._init_images()

    def draw_paragraph(self, text):
        self.cursor_height = draw_paragraph(self._image_draw, self.cursor_height, text, line_width=self.line_width)

    def show(self):
        self._update()
        self._init_images()

    def sleep(self):
        self._sleep()

    def _update(self):
        if self.mode == HORIZONTAL_MODE:
            self._epd.smart_update(self._image.rotate(90, expand=True))
            return
        self._epd.smart_update(self._image)

    def _init_images(self):
        self.cursor_height = 0
        self._image = Image.new('1', (self._epd.width, self._epd.height), 255)
        self._image_draw = ImageDraw.Draw(self._image)

    def _sleep(self):
        self._epd.sleep()
