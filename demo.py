# !/usr/bin/python
"""Example using a character 4x20 serial Parallax LCD connected to an ESP32/ESP8266."""

from time import sleep
from parallaxlcd import CharLCD

"""Run demo."""
# Initialize the LCD
lcd = CharLCD()

# Show the no cursor
lcd.clear()
lcd.cursorOff()
lcd.print('No Cursor: ')
sleep(3)

# Show no cursor but blinking block
lcd.clear()
lcd.noCursorBlock()
lcd.print('No Cursor')
lcd.carriageReturn()
lcd.print('but blinking block: ')
sleep(3)

# Show the underline cursor
lcd.clear()
lcd.cursorUnderline()
lcd.print('Underline: ')
sleep(3)

# Show the underline cursor + blinking block
lcd.clear()
lcd.cursorBlockBlink()
lcd.print('Underline +')
lcd.carriageReturn()
lcd.print('blinking block: ')
sleep(3)

# Disable blink and underline cursor.
lcd.cursorOff()

# Scroll message right & left
lcd.clear()
lcd.move('Moving right>', 3, 'R')
lcd.clear()
lcd.move('<Moving left', 8, 'L')
lcd.clear()
lcd.move('Moving default', 3)

# Print centered messages with different length
lcd.clear()
lcd.printCenter('0')
sleep(0.5)
lcd.printCenter('01')
sleep(0.5)
lcd.printCenter('012')
sleep(0.5)
lcd.printCenter('0123')
sleep(0.5)
lcd.printCenter('01234')
sleep(0.5)
lcd.printCenter('012345')
sleep(0.5)
lcd.printCenter('01234')
sleep(0.5)
lcd.printCenter('0123')
sleep(0.5)
lcd.printCenter('012')
sleep(0.5)
lcd.printCenter('01')
sleep(0.5)
lcd.printCenter('0')
sleep(0.5)
lcd.clear()


# The End
lcd.printCenter('Ende')

