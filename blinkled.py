from machine import Pin
import time

LED_PIN = 2
SWITCH_PIN = 14 #switch GPIO

led = Pin(LED_PIN, Pin.OUT)
switch = Pin(SWITCH_PIN, Pin.IN, Pin.PULL_UP)

while True:
    if switch.value() == 0:
        led.value(1)
        print("LED ON")
    else:
        led.value(0)
        print("LED OFF")
    time.sleep(1)
