import textwrap

from PIL import ImageFont

CHARS_PER_LINE = 27

FONT_SIZE = 20
FONT_LOCATION = '/usr/share/fonts/truetype/wqy/wqy-microhei.ttc'
FONT = ImageFont.truetype(FONT_LOCATION, FONT_SIZE)

TEXT_COLOR = 0

def draw_paragraph(image, start_height, label, text, font=FONT, text_color=TEXT_COLOR, line_width=CHARS_PER_LINE, line_padding=2):
    current_height = start_height
    labeled_text = label + ' ' + text
    paragraph = text_to_paragraph(labeled_text, line_width)
    for line in paragraph:
        _, string_height = image.textsize(line, font=font)
        image.text((0, current_height), line, fill=text_color, font=font)
        current_height += (string_height + line_padding)
    return current_height


def text_to_paragraph(text, line_width=CHARS_PER_LINE):
    return textwrap.wrap(text, line_width)


def seq_to_text(seq):
    return " ".join([str(val) for val in seq])
