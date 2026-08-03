from machine import Pin, SPI
import os, sdcard

spi = SPI(1, baudrate=1000000, polarity=0, phase=0,
          sck=Pin(18), mosi=Pin(23), miso=Pin(19))
cs = Pin(5, Pin.OUT)

#Initialise sd card and mount
sd = sdcard.SDCard(spi, cs)
os.mount(sd, "/sd")
print("✅️ SD card mounted!")
