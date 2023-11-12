#!/usr/bin/python
# -*- coding:utf-8 -*-
import time

from display import Display

import apis.psutil_metrics
import apis.darksky_weather

import RPi.GPIO as GPIO

KEYPRESS_DELAY = 5000

def handle_button_press(channel):
    print("Pressed button on channel {0}".format(channel))
    CHANNEL_PAGE_MAPPING[channel]()

def page_1():
    print("Rendering page 1")
    display.draw_paragraph("Load Avg: " + apis.psutil_metrics.load_averages())
    display.draw_paragraph("CPU Temp: " + str(apis.psutil_metrics.cpu_temp()))
    display.draw_paragraph("Memory Usg: " + str(apis.psutil_metrics.memory_percentage()))
    display.draw_paragraph("Uptime: " + str(apis.psutil_metrics.uptime()))
    display.show()

def page_2():
    print("Rendering page 2")
    display.draw_paragraph("Current Weather: " + apis.darksky_weather.current_weather())
    display.draw_paragraph("Today: " + apis.darksky_weather.todays_forecast())
    display.draw_paragraph("This Week: " + apis.darksky_weather.weekly_forecast())
    display.show()

def page_3():
    print("Rendering page 3")
    display.draw_paragraph("Weight Monitoring")
    display.draw_paragraph("Last Measurement:")
    display.draw_paragraph("Last Measurement:")
    display.show()

def page_4():
    print("Rendering page 4")
    display.draw_paragraph("Bar: " + "Baz")
    display.show()

CHANNEL_PAGE_MAPPING = {
    5: page_1,
    6: page_2,
    13: page_3,
    19: page_4
}

display = Display()

def main():
    print("Starting up")
    channel_list = [5, 6, 13, 19]
    GPIO.setup(channel_list, GPIO.IN)
    for channel in channel_list:
        GPIO.add_event_detect(channel, GPIO.RISING, bouncetime=KEYPRESS_DELAY, callback=handle_button_press)
    print("GPIO event handlers added")
    page_1()
    print("Initial page shown")
    while True:
        time.sleep(10)

    GPIO.cleanup()

if __name__ == '__main__':
    main()
