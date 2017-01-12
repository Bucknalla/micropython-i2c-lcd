import i2c_lcd

d = Display(i2c, 0x3E)

d.home()

d.write('Hello World')
