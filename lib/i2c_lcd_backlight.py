# This is a port of https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight
# (c) 2017 Alex Bucknall <alex.bucknall@gmail.com>
# 
# reworked by Ubi de Feo - 2023

# Backlight i2c default Address = 0x62
# Backlight Grove RGB Display v5.0 - default address = 0x30

from machine import I2C

class Backlight(object):
    # colour registers for v3 and v4
    # addresses for v5 will be set in __init__
    REG_RED = 0x04 # pwm2
    REG_GREEN = 0x03 # pwm1
    REG_BLUE = 0x02 # pwm0

    REG_MODE1 = 0x00
    REG_MODE2 = 0x01
    REG_OUTPUT = 0x08
    RGB_ADDRESS_V5 = 0x30

    def __init__(self, i2c, address):
        if not isinstance(i2c, I2C):
            raise TypeError

        self.i2c = i2c
        self.address = int(address)

        # initialize
        if address == self.RGB_ADDRESS_V5:
          self.set_register(0x00, 0x07) # reset the chip
          
          self.set_register(0x04, 0x15) # set all led always on
        
          # redefine Registers for RED, GREEN, BLUE
          self.REG_RED = 0x6
          self.REG_GREEN = 0x7
          self.REG_BLUE = 0x8

        else:
          self.set_register(self.REG_MODE1, 0)
          self.set_register(self.REG_MODE2, 0)
          # all LED control by PWM
          self.set_register(self.REG_OUTPUT, 0xAA)
        
    

    def blink(self, state = True):
        if state:
          if self.address == self.RGB_ADDRESS_V5:
            # attach all led to pwm1
            # blink period in seconds = (<reg 1> + 2) *0.128s
            # pwm1 on/off ratio = <reg 2> / 256
            self.set_register(0x04, 0x2a)  # 0010 1010
            self.set_register(0x01, 0x06)  # blink every second
            self.set_register(0x02, 0x7f)  # half on, half off
          else:
            self.set_register(0x07, 0x17) # blink every seconds
            self.set_register(0x06, 0x7f) # 50% duty cycle
        else:
          if self.address == self.RGB_ADDRESS_V5:
            self.set_register(0x04, 0x15)  # 0001 0101
          else:
            self.set_register(0x07, 0x00)
            self.set_register(0x06, 0xff)
    
    def set_register(self, addr, value):
        value = bytearray([value])
        self.i2c.writeto_mem(self.address, addr, bytearray([]))
        self.i2c.writeto_mem(self.address, addr, value)

    def set_color(self, red, green, blue):
        self.set_register(self.REG_RED, int(red))
        self.set_register(self.REG_GREEN, int(green))
        self.set_register(self.REG_BLUE, int(blue))