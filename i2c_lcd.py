#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a port of https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight
# (c) 2017 Alex Bucknall <alex.bucknall@gmail.com>

from machine import I2C
import i2c_lcd_backlight
import i2c_lcd_screen

class Display(object):
    backlight = None
    screen = None

    i2c = I2C(0, I2C.MASTER)

    def __init__(self, i2c):
        self.backlight = i2c_lcd_backlight.Backlight(i2c, 0x62)
        self.screen = i2c_lcd_screen.Screen(i2c, 0x3e)

    def write(self, text):
        self.screen.write(text)

    def cursor(self, state):
        self.screen.cursor(state)

    def setCursor(self, col, row):
        self.screen.setCursor(col, row)

    def blink(self, state):
        self.screen.blink(state)

    def blinkLed(self):
        self.backlight.blinkLed()

    def display(self, state):
        self.screen.display(state)

    def clear(self):
        self.screen.clear()

    def home(self):
        self.screen.home()

    def color(self, r, g, b):
        self.backlight.set_color(r, g, b)

    def move(self, col, row):
        self.screen.setCursor(col, row)
