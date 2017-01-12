import i2c_lcd

d = Display(i2c)

d.home()

d.write('Hello World')
