import i2c_lcd
import time
from machine import I2C

def rainbow():
    rgbColour = [0,0,0]

    while True:
        time.sleep(0.1)
        for x in range(0,255,1):
            d.color(x,0,0)
        time.sleep(0.1)
        for x in range(0,255,1):
            d.color(0,x,0)
        time.sleep(0.1)
        for x in range(0,255,1):
            d.color(0,0,x)

i2c = I2C(0)
d = i2c_lcd.Display(i2c)

d.home()
d.write('Hello World')

rainbow()
