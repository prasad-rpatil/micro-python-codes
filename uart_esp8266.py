from machine import UART
import time

uart = UART(2, baudrate=9600, tx=17, rx=16)

print("ESP32 UART Ready")

while True:
    
    # Send message
    uart.write("Hello from ESP32\n")
    print("Sent: Hello from ESP32")
    
    time.sleep(2)

    # Receive safely
    if uart.any():
        data = uart.readline()
        if data:
            try:
                print("Received:", data.decode('utf-8').strip())
            except:
                print("Raw Data:", data)   # Print raw if decode fails