#!/usr/bin/python
# -*- coding:utf-8 -*-
import time

from display import Display

import kubeclient

import RPi.GPIO as GPIO

display = Display()


def main():
    display.draw_paragraph("CLUSTER STATUS")
    for node in kubeclient.list_all_nodes():
        display.draw_paragraph(
            "Node {node[name]}, {node[addresses]}".format(node=node))
    display.show()

if __name__ == '__main__':
    main()
