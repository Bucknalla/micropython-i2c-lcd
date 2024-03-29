# This example works with both Grove i2c LCD Displays:
# - Black on Yellow
# - RGB Backlight 

import i2c_lcd
from machine import I2C

i2c = I2C(0)
d = i2c_lcd.Display(i2c)

d.home()
d.write('Hello, World!')
d.move(0,1)
d.write('How are you?')
