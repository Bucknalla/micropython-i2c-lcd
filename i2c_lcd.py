from machine import I2C
import time
import i2c_lcd_backlight
import i2c_lcd_screen

class Display(object):
    backlight = None
    screen = None

    i2c = I2C(0, I2C.MASTER)

    def __init__(self, i2c):
        self.backlight = backlight.Backlight(i2c, 0x62)
        self.screen = screen.Screen(i2c, 0x3e)

    def write(self, text):
        self.screen.write(text)

    def cursor(self, state):
        self.screen.cursor(state)

    def blink(self, state):
        self.screen.blink(state)

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
