# !/usr/bin/python
"""Example using a character 4x20 serial Parallax LCD connected to an ESP32/ESP8266."""

from time import sleep
from classtest import LCD_CURSOR_UNDERLINE, CharLCD

"""Run demo."""
# Initialize the LCD
lcd = CharLCD()

# Print a 2 line centered message

# # Show the no cursor
# lcd.clear()
# lcd.cursorOff()
# lcd.print('No Cursor: ')
# sleep(3)

# # Show no cursor but blinking block
# lcd.clear()
# lcd.noCursorBlock()
# lcd.print('No Cursor: ')
# lcd.carriageReturn()
# lcd.print('but blinking block: ')
# sleep(3)

# # Show the underline cursor
# lcd.clear()
# lcd.cursorUnderline()
# lcd.print('Underline: ')
# sleep(3)

# # Show the underline cursor + blinking block
# lcd.clear()
# lcd.cursorBlockBlink()
# lcd.print('Underline +')
# lcd.carriageReturn()
# lcd.print('blinking block: ')
# sleep(3)

# # Disable blink and underline cursor.
# lcd.cursorOff()

# Scroll message right & left
lcd.clear()
#lcd.move('Moving right>', 5, 'R')
#lcd.move('<Moving left', 8, 'l')
#lcd.clear()
#lcd.move('Moving default', 5)
# lcd.printCenter('0')
# sleep(2)
# lcd.printCenter('01')
# sleep(2)
# lcd.printCenter('012')
# sleep(2)
# lcd.printCenter('0123')
# sleep(2)
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
lcd.clear


# The End


print('Ende')

'''
run()
def run():
    """Run demo."""
    # Initialize the LCD
    lcd = CharLCD(cols=16, rows=4)

    # Print a 2 line centered message
    lcd.message('Hello')
    #lcd.set_line(1)
    lcd.message('World!')
    sleep(3.0)

    # Show the underline cursor.
    lcd.clear()
    lcd.show_underline()
    lcd.message('Underline')
    lcd.set_line(1)
    lcd.message('Cursor: ')
    sleep(3.0)

    # Also show the blinking cursor.
    lcd.clear()
    lcd.show_blink()
    lcd.message('Blinking')
    lcd.set_line(1)
    lcd.message('Cursor: ')
    sleep(3.0)

    # Disable blink and underline cursor.
    lcd.show_underline(False)
    lcd.show_blink(False)

    # Scroll message right & left.
    lcd.clear()
    lcd.message('Scrolling Demo')
    sleep(1.0)
    for i in range(16):
        sleep(0.25)
        lcd.move_right()
    for i in range(16):
        sleep(0.25)
        lcd.move_left()
    sleep(2.0)

    # The End
    lcd.create_char(0, bytearray([7, 12, 24, 16, 22, 22, 22, 16]))
    lcd.create_char(1, bytearray([28, 6, 3, 1, 13, 13, 13, 1]))
    lcd.create_char(2, bytearray([16, 20, 20, 23, 19, 24, 12, 7]))
    lcd.create_char(3, bytearray([1, 1, 5, 29, 25, 3, 6, 28]))
    lcd.clear()
    lcd.message('The', 3)
    lcd.home()
    lcd.message('\x00')
    lcd.message('\x01')
    lcd.set_line(1)
    lcd.message('End', 3)
    lcd.set_cursor(0, 1)
    lcd.message('\x02')
    lcd.message('\x03')
'''