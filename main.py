#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import datetime
import os

import kubeclient
import pytz
import RPi.GPIO as GPIO

from display import Display

display = Display()


def main():
    display.draw_paragraph("NODES")
    for node in kubeclient.list_all_nodes():
        display.draw_paragraph(
            "{node[name]}, {node[addresses]}".format(node=node))
    display.draw_paragraph("SERVICES")
    for service in kubeclient.list_all_services():
        display.draw_paragraph(
            "{service[name]}, {service[ip]}".format(service=service))
    display.draw_paragraph("Updated: {0}".format(datetime.datetime.now(tz=pytz.timezone(os.environ['TIMEZONE'])).strftime('%H:%M %d/%m')))
    display.show()
    display.sleep()

if __name__ == '__main__':
    main()
