from machine import Pin, Timer
import time
# LED on GPIO2 (built-in LED in many ESP32 boards)
led = Pin(2, Pin.OUT)
# Switch on GPIO4 (you can change pin based on your board)
switch = Pin(4, Pin.IN, Pin.PULL_UP)

timer_count = Timer(0) # For counting 5 seconds
timer_blink = Timer(1) # For blinking LED with variable delay
# Global variables
count = 0
state = "IDLE"
blink_stage = 0
on_off = 0 # 0 = OFF, 1 = ON
# Timer callback: counts 1 to 5 seconds
def count_up(t):
    global count, state
    count += 1
    print("Counting:", count)
    if count >= 5: # After 5 seconds
        timer_count.deinit() # stop counting timer
        count = 0
        state = "LED_ON"
        led.value(1) # Turn LED ON
        print("LED ON for 5 seconds")
        time.sleep(5) # Keep LED ON for 5 sec
        led.value(0) # Turn LED OFF
        print("LED OFF")
        state = "BLINK"
        start_blink_sequence()
# Function to handle variable blink pattern
def blink_handler(t):
    global blink_stage, on_off
    if on_off == 0:
        led.value(1) # LED ON
        on_off = 1
        duration = (blink_stage + 2) * 1000 # ON duration (2s, 3s, 4s...)
        print(f"LED ON for {blink_stage+2} sec")
    else:
        led.value(0) # LED OFF
        on_off = 0
        duration = (blink_stage + 2) * 1000 # OFF duration
        print(f"LED OFF for {blink_stage+2} sec")
        blink_stage += 1
    if blink_stage > 2: # after 2s, 3s, 4s sequence → stop
        timer_blink.deinit()
        print("Blink sequence finished.")
        return
    timer_blink.init(period=duration, mode=Timer.ONE_SHOT, callback=blink_handler)
 # restart timer with new duration


# Start the special blink sequence
def start_blink_sequence():
    global blink_stage, on_off
    blink_stage = 0
    on_off = 0
    blink_handler(None) 
 # trigger first blink manually
# Interrupt handler when switch is pressed
def switch_pressed(pin):
    global state, count
    if state == "IDLE":
        print("Switch pressed! Starting 5-sec count...")
        state = "COUNTING"
        count = 0
timer_count.init(period=1000, mode=Timer.PERIODIC, callback=count_up)

# Attach interrupt to switch (falling edge = button press)
switch.irq(trigger=Pin.IRQ_FALLING, handler=switch_pressed)
print("System ready. Press the switch to start.")