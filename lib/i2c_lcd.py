# ******************************************************************************
# 
# MicroPython driver for Grove LCD 16x2 Display modules
# Allows to control Black on Yellow (simple backlight)
# as well as RGB Backlight modules
#
# Ubi de Feo <ubidefeo.com>, 2023
#
# Originally a port of https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight
# by Alex Bucknall <alex.bucknall@gmail.com>
# https://github.com/Bucknalla/micropython-i2c-lcd
# 
# ******************************************************************************

from machine import I2C
import i2c_lcd_backlight
import i2c_lcd_screen



class Display(object):
    screen = None

    def __init__(self, i2c, lcd_addr=0x3e):
        self.screen = i2c_lcd_screen.Screen(i2c, lcd_addr)

    def write(self, text):
        self.screen.write(text)

    def cursor(self, state):
        self.screen.cursor(state)

    def blink(self, state):
        self.screen.blink(state)

    def autoscroll(self, state):
        self.screen.autoscroll(state)

    def display(self, state):
        self.screen.display(state)

    def clear(self):
        self.screen.clear()

    def home(self):
        self.screen.home()

    def move(self, col, row):
        self.screen.setCursor(col, row)

class RGBDisplay(Display):
    backlight = None

    def __init__(self, i2c, lcd_addr=0x3e, rgb_addr = 0x62):
        self.backlight = i2c_lcd_backlight.Backlight(i2c, rgb_addr)
        super().__init__(i2c, lcd_addr)
    
    def color(self, r, g, b):
        self.backlight.set_color(r, g, b)
    
    def blinkLed(self):
        self.backlight.blinkLed()
