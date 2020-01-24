#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import traceback

from rpi_epd2in7.epd import EPD
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
        drawblack, current_h, "CPU Usg:", seq_to_text(psutil_metrics.cpu_percentages()))

    current_h = draw_paragraph(
        drawblack, current_h, "Load Avg:", seq_to_text(psutil_metrics.load_averages()))

    current_h = draw_paragraph(
        drawblack, current_h, "CPU Temp:", str(psutil_metrics.cpu_temp()))

    current_h = draw_paragraph(
        drawblack, current_h, "Memory Usg:", str(psutil_metrics.memory_percentage()))

    current_h = draw_paragraph(
        drawblack, current_h, "Uptime:", str(psutil_metrics.uptime()))

    return HBlackimage


def page_2():
    HBlackimage = Image.new(
        '1', (epd.width, epd.height), 255)

    # Horizontal
    print("Drawing")
    drawblack = ImageDraw.Draw(HBlackimage)
    current_h = 0

    current_h = draw_paragraph(
        drawblack, current_h, "Current Weather:", darksky_weather.current_weather())

    current_h = draw_paragraph(
        drawblack, current_h, "Today:", darksky_weather.todays_forecast())

    current_h = draw_paragraph(
        drawblack, current_h, "This Week:", darksky_weather.weekly_forecast())

    return HBlackimage

try:
    epd = EPD()
    epd.init()

    page_1_image = page_1().rotate(180)
    epd.smart_update(page_1_image)
    
    time.sleep(10)

    page_2_image = page_2().rotate(180)
    epd.smart_update(page_2_image)

    epd.sleep()

except:
    print('traceback.format_exc():\n%s', traceback.format_exc())
    exit()
