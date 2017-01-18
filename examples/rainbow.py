import i2c_lcd
from machine import I2C

i2c = I2C(0, I2C.MASTER)
d = i2c_lcd.Display(i2c)

d.home()
d.write('Hello World')

rainbow()

def rainbow():
	rgbColour = [0,0,0]

	while True:
		for x in range(0,255,1):
			d.color(x,0,0)

		for x in range(0,255,1):
			d.color(0,x,0)

		for x in range(0,255,1):
			d.color(0,0,x)
}
