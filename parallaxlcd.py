import machine
import gc
from time import sleep

gc.enable

LCD_UART = 2
LCD_BAUDRATE = 19200
LCD_BOUNCE = 0.05
LCD_NUMROWS = 4
LCD_NUMCOLS = 20
LCD_DISPLAY_OFF = '\x15'
LCD_DISPLAY_ON = '\x18'
LCD_DISPLAY_CLEAR = '\x0C'
LCD_CARRIAGE_RETURN = '\x0D'
LCD_BACKLIGHT_ON = '\x11'
LCD_BACKLIGHT_OFF = '\x12'
LCD_CURSOR_LINE_FEED = '\x0D'
LCD_CURSOR_LEFT = '\x08'
LCD_CURSOR_RIGHT = '\x09'
LCD_CURSOR_UNDERLINE = '\x18'
LCD_CURSOR_BLOCK = '\x17'
LCD_CURSOR = LCD_CURSOR_BLOCK
LCD_CURSOR_OFF = '\x16'
LCD_CURSOR_CHR_BLINK = '\x19'
LCD_ROW_MIN = 0
LCD_COL_MIN = 0
LCD_ROW = 0
LCD_COL = 0
LCD_ROW_MAX = 3
LCD_COL_MAX = 19
LCD_POS_LIST = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
                [0, 7], [0, 8], [0, 9], [0, 10], [0, 11], [0, 12], [0, 13],
                [0, 14], [0, 15], [0, 16], [0, 17], [0, 18], [0, 19],
                [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
                [1, 7], [1, 8], [1, 9], [1, 10], [1, 11], [1, 12], [1, 13],
                [1, 14], [1, 15], [1, 16], [1, 17], [1, 18], [1, 19],
                [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
                [2, 7], [2, 8], [2, 9], [2, 10], [2, 11], [2, 12], [2, 13],
                [2, 14], [2, 15], [2, 16], [2, 17], [2, 18], [2, 19],
                [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6],
                [3, 7], [3, 8], [3, 9], [3, 10], [3, 11], [3, 12], [3, 13],
                [3, 14], [3, 15], [3, 16], [3, 17], [3, 18], [3, 19]]


LCD_COMMAND_LIST = ['\x80', '\x81', '\x82', '\x83', '\x84', '\x85', '\x86', '\x87', '\x88', '\x89', '\x8A', '\x8B', '\x8C', '\x8D', '\x8E', '\x8F',
                    '\x90', '\x91', '\x92', '\x93', '\x94', '\x95', '\x96', '\x97', '\x98', '\x99', '\x9A', '\x9B', '\x9C', '\x9D', '\x9E', '\x9F',
                    '\xA0', '\xA1', '\xA2', '\xA3', '\xA4', '\xA5', '\xA6', '\xA7', '\xA8', '\xA9', '\xAA', '\xAB', '\xAC', '\xAD', '\xAE', '\xAF',
                    '\xB0', '\xB1', '\xB2', '\xB3', '\xB4', '\xB5', '\xB6', '\xB7', '\xB8', '\xB9', '\xBA', '\xBB', '\xBC', '\xBD', '\xBE', '\xBF',
                    '\xC0', '\xC1', '\xC2', '\xC3', '\xC4', '\xC5', '\xC6', '\xC7', '\xC8', '\xC9', '\xCA', '\xCB', '\xCC', '\xCD', '\xCE', '\xCF']

eraseOLD = ' '
eraseROW = LCD_ROW_MAX
eraseCOL = LCD_COL_MAX

class CharLCD:
    def __init__(self):
        self.connection = machine.UART(LCD_UART, baudrate=LCD_BAUDRATE)
        sleep(LCD_BOUNCE)
        self.setup()

    def setup(self):
        self.On()
        self.clear()
        self.backlightOn()

    def On(self):
        self.connection.write(str(LCD_DISPLAY_ON))
        sleep(LCD_BOUNCE)

    def Off(self):
        self.connection.write(LCD_DISPLAY_OFF)
        sleep(LCD_BOUNCE)

    def clear(self):
        self.connection.write(LCD_DISPLAY_CLEAR)
        sleep(LCD_BOUNCE)

    def carriageReturn(self):
        self.connection.write(LCD_CARRIAGE_RETURN)
        sleep(LCD_BOUNCE)

    def cursorUnderline(self):
        self.connection.write(LCD_CURSOR_UNDERLINE)
        sleep(LCD_BOUNCE)

    def noCursorBlock(self):
        self.connection.write(LCD_CURSOR_BLOCK)
        sleep(LCD_BOUNCE)

    def cursorOff(self):
        self.connection.write(LCD_CURSOR_OFF)
        sleep(LCD_BOUNCE)

    def cursorBlockBlink(self):
        self.connection.write(LCD_CURSOR_CHR_BLINK)
        sleep(LCD_BOUNCE)

    def cursorLeft(self):
        self.connection.write(LCD_CURSOR_LEFT)
        sleep(LCD_BOUNCE)

    def cursorRight(self):
        self.connection.write(LCD_CURSOR_RIGHT)
        sleep(LCD_BOUNCE)

    def move(self, text, times, *dir):
        self.cursorOff()
        self.print(text)
        erase = ' '

        for i in range(len(text)):
               erase = erase + ' '

        for i in range(times):
            for i in range(len(text)):
               self.cursorLeft()

            self.print(erase)
            self.cursorLeft()

            for i in range(len(text)):
                self.cursorLeft()

            #dir = dir[]
            print(dir)
            if dir in['L', 'l']:
                self.cursorLeft()
                print('Left')
            else:
                self.cursorRight()
                print('Right')

            self.print(text)

    def cursorLineFeed(self):
        self.connection.write(LCD_CURSOR_LINE_FEED)
        sleep(LCD_BOUNCE)

    def backlightOn(self):
        self.connection.write(LCD_BACKLIGHT_ON)
        sleep(LCD_BOUNCE)

    def backlightOff(self):
        self.connection.write(LCD_BACKLIGHT_OFF)
        sleep(LCD_BOUNCE)

    def print(self, message):
        self.connection.write(message)
        sleep(LCD_BOUNCE)

    def printCenter(self, message):
        global eraseROW
        global eraseCOL
        global eraseOLD

        self.cursorPos(eraseROW, eraseCOL)
        self.print(eraseOLD)

        lineCenter = LCD_ROW_MAX/2
        messageCenterROW = LCD_ROW_MAX//2
        messageCenterCOL = LCD_COL_MAX//2 - len(message)//2

        self.cursorPos(messageCenterROW, messageCenterCOL)
        self.print(message)

        eraseOLD = ' ' * len(message)
        eraseROW = messageCenterROW
        eraseCOL = messageCenterCOL
        
    def cursorPos(self, LCD_ROW, LCD_COL):
        #print('*** In cursorPos: ', LCD_ROW, LCD_COL)
        if LCD_ROW < LCD_ROW_MIN:
            LCD_ROW = LCD_ROW_MIN
        if LCD_ROW > LCD_ROW_MAX:
            LCD_ROW = LCD_ROW_MAX
        if LCD_COL < LCD_COL_MIN:
            LCD_COL = LCD_COL_MIN
        if LCD_COL > LCD_COL_MAX:
            LCD_COL = LCD_COL_MAX

        #print('ROW', LCD_ROW)
        #print('COL', LCD_COL)

        #print('*** Gewuenschte Position: ', LCD_ROW, LCD_COL)
        searchPOS = [LCD_ROW, LCD_COL]
        #print('*** SuchPosition: ', searchPOS)
        if searchPOS in LCD_POS_LIST:
            searchINDEX = LCD_POS_LIST.index([LCD_ROW, LCD_COL])
            #print('*** SuchIndex: ', searchINDEX)
        else:
            print('Not found')

        if searchINDEX < len(LCD_COMMAND_LIST):
            LCD_CURSOR_POS = LCD_COMMAND_LIST[searchINDEX]
            sleep(LCD_BOUNCE)
            self.connection.write(str(LCD_CURSOR_POS))
            sleep(LCD_BOUNCE)
        else:
            print('Out of range ')
