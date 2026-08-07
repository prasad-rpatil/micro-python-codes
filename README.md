# ESP32/ESP8266 MicroPython Projects

This repository contains my MicroPython practice programs developed while learning ESP32 and ESP8266 programming using the Thonny IDE.

The repository includes MicroPython source codes, firmware files, and examples demonstrating hardware interfacing, communication protocols, sensors, storage devices, and basic IoT applications.

---

## Repository Contents

### MicroPython Programs

- LED Control
- LED Blinking
- Variable LED Blinking
- LED Counter
- DHT11 Temperature & Humidity Sensor
- LM35 Temperature Sensor
- UART Communication
- ESP8266 UART Communication
- Timer Programming
- Touch Sensor
- SD Card Interface
- SD Card File System Integration
- REPL Configuration for SD Card
- ESP32 Web Server
- Basic Messaging Example

---

## Firmware Files

This repository also contains the firmware required for ESP32 development.

- **original_firmware_esp32.bin** – Original ESP firmware backup that can be restored to the board if needed.
- **firmware.bin** – Official MicroPython firmware used to flash the ESP32/ESP8266 for running MicroPython programs.

These firmware files make it easier to restore or reflash the board without downloading them again.

---

## Technologies Used

- MicroPython
- Python
- ESP32
- ESP8266
- Thonny IDE

---

## Hardware Used

- ESP32 Development Board
- ESP8266
- DHT11 Temperature & Humidity Sensor
- LM35 Temperature Sensor
- LEDs
- SD Card Module
- Touch Sensor
- USB-to-Serial Interface

---

## Repository Structure

```
ESP32-MicroPython/
│
├── blinkled.py
├── led.py
├── count.py
├── count_led.py
├── dht11.py
├── lm35.py
├── uart.py
├── uart_esp8266.py
├── timer.py
├── touch_sense.py
├── messaging.py
├── server_esp.py
├── sdcard.py
├── interface_of_sdcard.py
├── repl_codefor_sdcard.py
├── variablebl_blink.py
│
├── original_firmware.bin
├── micropython.bin
│
└── README.md
```

---

## Learning Outcomes

Through these projects, I gained hands-on experience in:

- MicroPython programming
- Embedded Systems Development
- GPIO Programming
- Sensor Interfacing
- UART Communication
- SD Card Storage
- Timer Programming
- Touch Sensor Applications
- ESP32/ESP8266 Firmware Flashing
- Basic IoT and Web Server Development

---

## How to Use

1. Flash the board using **micropython.bin**.
2. Connect the ESP32/ESP8266 using **Thonny IDE**.
3. Upload any Python program from this repository.
4. Execute the program on the board.
5. If required, restore the board using **original_firmware.bin**.

---

## Author

**Prasad R Patil**

Electronics and Communication Engineering (ECE)

Learning Embedded Systems, IoT, and MicroPython through hands-on projects.

⭐ If you found this repository helpful, consider giving it a star.
