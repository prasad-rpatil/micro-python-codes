folder_path = "/sd/kevin_scripts"
try:
    os.mkdir(folder_path)
    print("Folder created:", folder_path)
except OSError:
    print("Folder already exists:", folder_path)

# Save LED blink code inside the folder
file_path = folder_path + "/led_blink.py"
with open(file_path, "w") as f:
    f.write("""from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.value(1)      
    print("LED ON")
    time.sleep(1)     
    led.value(0)      
    print("LED OFF")
    time.sleep(1) 
""")

print("✅ LED blink code saved at:", file_path)