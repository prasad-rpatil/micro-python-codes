from machine import Pin
import time

# On many ESP32/ESP8266 boards, the built-in LED is on pin 2
led = Pin(2, Pin.OUT)

while True:
    led.value(1)      # LED ON
    print("LED ON")
    time.sleep(1)     # wait 1 second
    led.value(0)      # LED OFF
    print("LED OFF")
    time.sleep(1)     # wait 1 second
