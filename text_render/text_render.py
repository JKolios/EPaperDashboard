import textwrap

from PIL import ImageFont

CHARS_PER_LINE = 24

FONT_SIZE = 18
FONT_LOCATION = './text_render/wqy-microhei.ttc'
FONT = ImageFont.truetype(FONT_LOCATION, FONT_SIZE)

TEXT_COLOR = 0


def draw_paragraph(image, start_height, text, font=FONT, text_color=TEXT_COLOR, line_width=CHARS_PER_LINE, line_padding=2):
    current_height = start_height
    paragraph = text_to_paragraph(text, line_width)
    for line in paragraph:
        image.text((0, current_height), line, fill=text_color, font=font)
        current_height += (FONT_SIZE + line_padding)
    return current_height


def text_to_paragraph(text, line_width):
    return textwrap.wrap(text, line_width)
