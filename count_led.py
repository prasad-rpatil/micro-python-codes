from machine import Pin, Timer
import time

led = Pin(2, Pin.OUT)   # Onboard LED
timer = Timer(1)

count = 0

# Step 1: LED ON 5s / OFF 5s with counter
print("LED ON for 5s, OFF for 5s")
led.value(1)
print("LED ON - Count:", count)
time.sleep(5)

led.value(0)
count += 1
print("LED OFF - Count:", count)
time.sleep(5)

# Step 2: 10s pause using timer
print("Maintaining 10s delay before pattern")
time.sleep(10)

# Step 3: Variable ON/OFF 1s up to 10s
print("Stage 2: Variable Blink Pattern Start")
for d in range(1, 11):
    led.value(1)
    print("LED ON for", d, "s - Count:", count)
    time.sleep(d)
    led.value(0)
    count += 1
    print("LED OFF for", d, "s - Count:", count)
    time.sleep(d)

print("Pattern Complete")
