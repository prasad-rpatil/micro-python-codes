from machine import ADC, Pin
import time

adc=ADC(Pin(32))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)
Vref=3.3

while True:
    value=adc.read()
    vol=(value/4095)*Vref
    temp=vol*100
    
    print("ADC Value:",value,"Voltage: {:.2f} v".format(vol),"Temperature: {:.2f} C".format(temp))
    time.sleep(1)