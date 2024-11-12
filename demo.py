from writer import Writer
from ssd1306 import SSD1306_I2C
# Font file converted to a bitmap (for ascii 32-57) 35 pixel height works well for this display
# See https://github.com/peterhinch/micropython-font-to-py
import freesansnum35
from machine import Pin, I2C
import pcf8575
import time

i2c = I2C(0, scl=Pin(17), sda=Pin(16))

for device in i2c.scan():
    print("I2C hexadecimal address: ", hex(device))

OLED_WIDTH = 128
OLED_HEIGHT = 64
oled = SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c, addr=0x3C)
pcf = pcf8575.PCF8575(i2c, 0x20)

for n in range(50):
    button=pcf.pin(0)
    oled.fill(0)
    oled.line(0, 15, oled.width - 1, 15, 1)
    wri = Writer(oled, freesansnum35, verbose=False)
    Writer.set_textpos(oled, 0, 0)
    oled.text("n: " + str(n),  40, 0)
    Writer.set_textpos(oled, 25, 0)
    wri.printstring(str(button))
    oled.show()
    time.sleep(.2)

oled.fill(0)
oled.show()