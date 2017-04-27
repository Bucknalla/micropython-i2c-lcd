#!/usr/bin/python
# -*- coding: utf-8 -*-
# This is a port of https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight
# (c) 2017 Alex Bucknall <alex.bucknall@gmail.com>

from machine import I2C
import time

class Screen(object):
    # commands
    LCD_CLEARDISPLAY = 0x01
    LCD_RETURNHOME = 0x02
    LCD_ENTRYMODESET = 0x04
    LCD_DISPLAYCONTROL = 0x08
    LCD_CURSORSHIFT = 0x10
    LCD_FUNCTIONSET = 0x20
    LCD_SETCGRAMADDR = 0x40
    LCD_SETDDRAMADDR = 0x80

    # flags for display entry mode
    LCD_ENTRYRIGHT = 0x00
    LCD_ENTRYLEFT = 0x02
    LCD_ENTRYSHIFTINCREMENT = 0x01
    LCD_ENTRYSHIFTDECREMENT = 0x00

    # flags for display on/off control
    LCD_DISPLAYON = 0x04
    LCD_DISPLAYOFF = 0x00
    LCD_CURSORON = 0x02
    LCD_CURSOROFF = 0x00
    LCD_BLINKON = 0x01
    LCD_BLINKOFF = 0x00

    # flags for display/cursor shift
    LCD_DISPLAYMOVE = 0x08
    LCD_CURSORMOVE = 0x00
    LCD_MOVERIGHT = 0x04
    LCD_MOVELEFT = 0x00

    # flags for function set
    LCD_8BITMODE = 0x10
    LCD_4BITMODE = 0x00
    LCD_2LINE = 0x08
    LCD_1LINE = 0x00
    LCD_5x10DOTS = 0x04
    LCD_5x8DOTS = 0x00

    def __init__(self, i2c, address, oneline=False, charsize=LCD_5x8DOTS):

        self.i2c = i2c
        self.address = address

        i2c.init(I2C.MASTER, baudrate=20000)

        self.disp_func = self.LCD_DISPLAYON # | 0x10
        if not oneline:
            self.disp_func |= self.LCD_2LINE
        elif charsize != 0:
            # for 1-line displays you can choose another dotsize
            self.disp_func |= self.LCD_5x10DOTS

        # wait for display init after power-on
        time.sleep_ms(50) # 50ms

        # send function set
        self.cmd(self.LCD_FUNCTIONSET | self.disp_func)
        time.sleep_us(4500) ##time.sleep(0.0045) # 4.5ms
        self.cmd(self.LCD_FUNCTIONSET | self.disp_func)
        time.sleep_us(150) ##time.sleep(0.000150) # 150µs = 0.15ms
        self.cmd(self.LCD_FUNCTIONSET | self.disp_func)
        self.cmd(self.LCD_FUNCTIONSET | self.disp_func)

        # turn on the display
        self.disp_ctrl = self.LCD_DISPLAYON | self.LCD_CURSOROFF | self.LCD_BLINKOFF
        self.display(True)

        # clear it
        self.clear()

        # set default text direction (left-to-right)
        self.disp_mode = self.LCD_ENTRYLEFT | self.LCD_ENTRYSHIFTDECREMENT
        self.cmd(self.LCD_ENTRYMODESET | self.disp_mode)

    def cmd(self, command):
        assert command >= 0 and command < 256
        command = bytearray([command])
        self.i2c.writeto_mem(self.address, 0x80, bytearray([]))
        self.i2c.writeto_mem(self.address, 0x80, command)


    def write_char(self, c):
        assert c >= 0 and c < 256
        c = bytearray([c])
        self.i2c.writeto_mem(self.address, 0x40, c)

    def write(self, text):
        for char in text:
            self.write_char(ord(char))

    def cursor(self, state):
        if state:
            self.disp_ctrl |= self.LCD_CURSORON
            self.cmd(self.LCD_DISPLAYCONTROL  | self.disp_ctrl)
        else:
            self.disp_ctrl &= ~self.LCD_CURSORON
            self.cmd(self.LCD_DISPLAYCONTROL  | self.disp_ctrl)

    def setCursor(self, col, row):
        col = (col | 0x80) if row == 0 else (col | 0xc0)
        self.cmd(col)

    def autoscroll(self, state):
        if state:
            self.disp_ctrl |= self.LCD_ENTRYSHIFTINCREMENT
            self.cmd(self.LCD_DISPLAYCONTROL  | self.disp_ctrl)
        else:
            self.disp_ctrl &= ~self.LCD_ENTRYSHIFTINCREMENT
            self.cmd(self.LCD_DISPLAYCONTROL  | self.disp_ctrl)

    def blink(self, state):
        if state:
            self.disp_ctrl |= self.LCD_BLINKON
            self.cmd(self.LCD_DISPLAYCONTROL  | self.disp_ctrl)
        else:
            self.disp_ctrl &= ~self.LCD_BLINKON
            self.cmd(self.LCD_DISPLAYCONTROL  | self.disp_ctrl)

    def display(self, state):
        if state:
            self.disp_ctrl |= self.LCD_DISPLAYON
            self.cmd(self.LCD_DISPLAYCONTROL  | self.disp_ctrl)
        else:
            self.disp_ctrl &= ~self.LCD_DISPLAYON
            self.cmd(self.LCD_DISPLAYCONTROL  | self.disp_ctrl)

    def clear(self):
        self.cmd(self.LCD_CLEARDISPLAY)
        time.sleep_ms(2) # 2ms

    def home(self):
        self.cmd(self.LCD_RETURNHOME)
        time.sleep_ms(2) # 2m
