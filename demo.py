from writer import Writer
from ssd1306 import SSD1306_I2C
# Font file converted to a bitmap (for ascii 32-57) 35 pixel height works well for this display
# See https://github.com/peterhinch/micropython-font-to-py


#  Example of using an ssd1306 and supporting multiple size fonts
#  and reading switches using a pcf8675 i2c device
# See the link above to see how to create font files
# https://github.com/mcauser/micropython-pcf8575

import freesansnum35
from machine import Pin, I2C
import pcf8575
import time

i2c = I2C(0, scl=Pin(13), sda=Pin(12))

for device in i2c.scan():
    print("I2C hexadecimal address: ", hex(device))

OLED_WIDTH = 128
OLED_HEIGHT = 64
oled = SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c, addr=0x3C)
pcf = pcf8575.PCF8575(i2c, 0x20)

for n in range(70):
    # Set pin 0 high before reading value
    pcf.pin(0,1)
    button=pcf.pin(0)
    # Set output pin (10) to match input pin (0)
    pcf.pin(10,button)
    oled.fill(0)
    Writer.set_textpos(oled, 0, 0)
    oled.text("n: " + str(n),  40, 0)
    oled.line(0, 15, oled.width - 1, 15, 1)
    # Use writer to write using the larger font
    wri = Writer(oled, freesansnum35, verbose=False)
    Writer.set_textpos(oled, 25, 0)
    wri.printstring(str(button))
    oled.show()
    time.sleep(.2)

oled.fill(0)
oled.show()