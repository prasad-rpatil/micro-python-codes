from machine import Pin, ADC, TouchPad
import time

# --- Initialize Touch Sensor on GPIO 4 ---
touch = TouchPad(Pin(4))

# --- Initialize ADC on GPIO 34 ---
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)   # full 0–3.3V range
adc.width(ADC.WIDTH_12BIT) # 12-bit resolution (0–4095)

print("Touch + ADC Demo (No external sensor)\n")

while True:
    # Read values
    touch_val = touch.read()
    adc_val = adc.read()
    voltage = (adc_val / 4095) * 3.3

    # Print results
    print("Touch Value:", touch_val, " | ADC Value:", adc_val, " | Voltage:", round(voltage, 2), "V")
    time.sleep(0.5)