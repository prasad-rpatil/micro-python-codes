# Sender ESP32 Code
from machine import UART, Pin
import time

uart = UART(1, baudrate=9600, tx=17, rx=16)  # UART1 setup

led = Pin(2, Pin.OUT)  # internal LED for indication

while True:
    msg = "Hello from ESP32-1\n"
    uart.write(msg)
    led.value(not led.value())  # Blink to show data being sent
    print("Sent:", msg.strip())
    time.sleep(2)
 
sender

# Receiver ESP32 Code
from machine import UART, Pin
import time

uart = UART(1, baudrate=9600, tx=17, rx=16)  # UART1 setup (rx pin used)
led = Pin(2, Pin.OUT)  # internal LED for indication

while True:
    if uart.any():
        data = uart.readline()
        if data:
            print("Received:", data.decode().strip())
            led.value(not led.value())  # blink on receive
    time.sleep(0.1)

