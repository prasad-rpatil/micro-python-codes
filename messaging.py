from machine import UART
import time

# UART2: RX=16, TX=17
uart = UART(2, baudrate=9600, tx=17, rx=16)

print("ESP32 Chat Ready")

while True:
    
    # 1️⃣ Receive from ESP8266
    if uart.any():
        data = uart.readline()
        if data:
            try:
                msg = data.decode().strip()
                print("Received from ESP8266:", msg)
            except:
                print("Raw:", data)

    # 2️⃣ Send message manually (edit message below if needed)
    message = "Hello from ESP32"
    uart.write(message + "\n")
    print("Sent:", message)

    time.sleep(3)