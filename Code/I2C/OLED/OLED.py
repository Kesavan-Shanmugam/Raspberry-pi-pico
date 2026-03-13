import ssd1306
import time
from machine import Pin, I2C

# Initialize I2C
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=400000)

# OLED Init
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

# Clear OLED
oled.fill(0)

# Display text
oled.text("Hello, KESAVAN", 0, 0)

# Update display
oled.show()
print(oled.text)