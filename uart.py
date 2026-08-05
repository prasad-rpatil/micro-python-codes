from machine import UART, Pin
import time

# Initialize two UART ports (change pins depending on board)
# UART1: TX=17, RX=16
# UART2: TX=25, RX=26  (example for ESP32)
uart1 = UART(1, baudrate=9600, tx=17, rx=16)
uart2 = UART(2, baudrate=9600, tx=25, rx=26)

name = "Prasad\n"   # Data to send (your name)

while True:
    # Send data from UART1
    uart1.write(name)
    print("Sent:", name.strip())
    
    time.sleep(1)  # small delay

    # Read data at UART2
    if uart2.any():
        received = uart2.read().decode('utf-8')
        print("Received:", received.strip())
    
    time.sleep(2)
