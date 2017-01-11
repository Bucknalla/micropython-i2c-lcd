import i2c_lcd

d = Display(i2c, 0x3E)

d.move(0, 0)

d.write('Hello World')
