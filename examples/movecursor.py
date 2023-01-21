# This example works with both Grove i2c LCD Displays:
# - Black on Yellow
# - RGB Backlight 

from i2c_lcd import Display
from machine import I2C

i2c = I2C(0)
d = Display(i2c)

d.home()
d.write('Hello,')

d.move(0,1)
d.write('World!')