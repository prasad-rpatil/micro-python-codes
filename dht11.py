from machine import Pin
import dht
import time

dht_sensor=dht.DHT11(Pin(14))
while True:
    try:
        dht_sensor.measure()
        temp=dht_sensor.temperature()
        hum=dht_sensor.humidity()
        
        print("Temperature: {} C Humidity: {}%".format(temp,hum))
    
    except OSError as e:
        print("Failed to read sensor:",e)
    time.sleep(2)