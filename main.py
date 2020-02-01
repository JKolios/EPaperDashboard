#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import traceback

from rpi_epd2in7.epd import EPD, VERTICAL_MODE, HORIZONTAL_MODE
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageChops

import psutil_metrics
import darksky_weather
from text_render import draw_paragraph, text_to_paragraph, seq_to_text


def page_1():

    HBlackimage = Image.new(
        '1', (epd.width, epd.height), 255)

    # Horizontal
    print("Drawing")
    drawblack = ImageDraw.Draw(HBlackimage)

    current_h = 0

    current_h = draw_paragraph(
        drawblack, current_h, "CPU Usg:", seq_to_text(psutil_metrics.cpu_percentages()), line_width=27)

    current_h = draw_paragraph(
        drawblack, current_h, "Load Avg:", seq_to_text(psutil_metrics.load_averages()), line_width=27)

    current_h = draw_paragraph(
        drawblack, current_h, "CPU Temp:", str(psutil_metrics.cpu_temp()), line_width=27)

    current_h = draw_paragraph(
        drawblack, current_h, "Memory Usg:", str(psutil_metrics.memory_percentage()), line_width=27)

    current_h = draw_paragraph(
        drawblack, current_h, "Uptime:", str(psutil_metrics.uptime()), line_width=27)

    return HBlackimage


def page_2():
    HBlackimage = Image.new(
        '1', (epd.width, epd.height), 255)

    # Horizontal
    print("Drawing")
    drawblack = ImageDraw.Draw(HBlackimage)
    current_h = 0

    current_h = draw_paragraph(
        drawblack, current_h, "Current Weather:", darksky_weather.current_weather(), line_width=27)

    current_h = draw_paragraph(
        drawblack, current_h, "Today:", darksky_weather.todays_forecast(), line_width=27)

    current_h = draw_paragraph(
        drawblack, current_h, "This Week:", darksky_weather.weekly_forecast(), line_width=27)

    return HBlackimage


try:
    epd = EPD(mode=HORIZONTAL_MODE)
    epd.init()

    page_1_image = page_1()
    epd.smart_update(page_1_image)

    page_2_image = page_2()
    epd.smart_update(page_2_image)

    epd.sleep()

except:
    print('traceback.format_exc():\n%s', traceback.format_exc())
    exit()
