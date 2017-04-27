#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a port of https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight
# (c) 2017 Alex Bucknall <alex.bucknall@gmail.com>

# Backlight i2c Address = 0x62

from machine import I2C

class Backlight(object):
    REG_RED = 0x04 # pwm2
    REG_GREEN = 0x03 # pwm1
    REG_BLUE = 0x02 # pwm0

    REG_MODE1 = 0x00
    REG_MODE2 = 0x01
    REG_OUTPUT = 0x08

    def __init__(self, i2c, address):
        if not isinstance(i2c, I2C):
            raise TypeError

        self.i2c = i2c
        self.address = int(address)

        # initialize
        self.set_register(self.REG_MODE1, 0)
        self.set_register(self.REG_MODE2, 0)

        # all LED control by PWM
        self.set_register(self.REG_OUTPUT, 0xAA)

    def blinkLed(self):
        self.set_register(0x07, 0x17) # blink every seconds
        self.set_register(0x06, 0x7f) # 50% duty cycle

    def set_register(self, addr, value):
        value = bytearray([value])
        self.i2c.writeto_mem(self.address, addr, bytearray([]))
        self.i2c.writeto_mem(self.address, addr, value)

    def set_color(self, red, green, blue):
        r = int(red)
        g = int(green)
        b = int(blue)
        self.set_register(self.REG_RED, r)
        self.set_register(self.REG_GREEN, g)
        self.set_register(self.REG_BLUE, b)
