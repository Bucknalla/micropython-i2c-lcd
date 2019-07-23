# MicroPython I2C 16x2 LCD Screen

This library is designed to support a MicroPython interface for i2c LCD character screens. It's designed around the Pycom implementation of MicroPython so will need to be tweaked to work for CircuitPython.

## Compatible LCDs
- [Grove LCD RGB Backlight](https://www.seeedstudio.com/grove-lcd-rgb-backlight-p-1643.html?cPath=34_36)

## Tested Dev Kits

- LoPy
- WiPy
- SiPy

## Module

This module supports writing to, clearing and refreshing the LCD screen, among other functions.

### write(text)

Prints text to LCD screen at the location of the cursor.

### autoscroll(bool)

Enables lcd to scroll text as typed.

### cursor(bool)

Sets cursor visibility.

### blink(bool)

Sets blink visibility.

### display(bool)

Sets display state (on/off).

### home()

Returns the cursor to the (0,0) location on screen

### move(col, row)

Moves the cursor to (col,row)

### color(r, g, b)

Changes the color of the LCD Backlight to (r,g,b)
