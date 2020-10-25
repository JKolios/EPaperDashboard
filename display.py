from epd2in7 import EPD, EPD_WIDTH, EPD_HEIGHT
from text_render.text_render import draw_paragraph

from PIL import Image, ImageFont, ImageDraw, ImageChops


class Display:
    def __init__(self, line_width=20):
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
        self._epd.display_frame(self._epd.get_frame_buffer(self._image.rotate(180)))

    def _init_images(self):
        self.cursor_height = 0
        self._image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 255)
        self._image_draw = ImageDraw.Draw(self._image)

    def _sleep(self):
        self._epd.sleep()
