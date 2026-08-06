from machine import Pin, Timer
import time

led = Pin(2, Pin.OUT)        # On-board LED (GPIO2 on ESP32/8266, change if needed)
button = Pin(4, Pin.IN, Pin.PULL_UP)  # Push button at GPIO4
timer = Timer(0)

start_flag = False
start_time = 0

def button_handler(pin):
    global start_flag, start_time
    if not start_flag:   # prevent multiple presses
        start_flag = True
        start_time = time.ticks_ms()
        print("Switch pressed – Timer started")

button.irq(trigger=Pin.IRQ_FALLING, handler=button_handler)

while True:
    if start_flag:
        elapsed = time.ticks_diff(time.ticks_ms(), start_time)

        if elapsed < 5000:   # First 5s waiting
            pass
        elif elapsed < 10000:   # Next 5s LED ON
            led.value(1)
        else:
            # Special blink pattern
            print("Blink Pattern Start")
            
            for d in [2, 3, 4]:
                led.value(1)
                print("LED ON for", d, "s")
                time.sleep(d)
                led.value(0)
                print("LED OFF for", d, "s")
                time.sleep(d)
            
            led.value(0)
            print("Pattern End")
            start_flag = False
