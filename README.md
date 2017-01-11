## MicroPython I2C 16x2 LCD Screen

This library is designed to support a MicroPython interface for i2c LCD character screens.

##### Compatible LCDs
- Grove LCD RGB Backlight

### Module

This module supports writing to, clearing and refreshing the LCD screen, among other functions.

##### write(text)

Prints text to LCD screen at the location of the cursor.

##### home()

Returns the cursor to the (0,0) location on screen

##### move(col, row)

Moves the cursor to (col,row)

##### color(r, g, b)

Changes the color of the LCD Backlight to (r,g,b)
