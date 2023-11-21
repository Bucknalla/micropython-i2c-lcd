# This example only works with Grove RGB Backlight i2c LCD Displays
#
# Version 5.0 replaced the LED controller, requiring some changes.
# Please specify which version you use

from i2c_lcd import RGBDisplay
from machine import I2C

i2c = I2C(0)

# Defaults to Grove RGB LCD Display v5.0
# for versions until V4.0 use 
# d = RGBDisplay(i2c, RGBDisplay.GROVE_RGB_V4)
d = RGBDisplay(i2c)


d.home()
d.write('Hello World')

def color_cycle():
	rgbColour = [0,0,0]

	while True:
		for x in range(0,255,1):
			d.color(x,0,0)

		for x in range(0,255,1):
			d.color(0,x,0)

		for x in range(0,255,1):
			d.color(0,0,x)

color_cycle()
