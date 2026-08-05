import network, socket, sys, _thread, time
import dht
from machine import Pin

# --- Access Point Setup ---
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='ESP32-Server01', password='12345678', authmode=3)
print("✅ Access Point Created:", ap.ifconfig())

# --- DHT11 Setup ---
dht_sensor = dht.DHT11(Pin(4))

# --- Socket Setup ---
s = socket.socket()
s.bind(('0.0.0.0', 8080))
s.listen(1)
print("📡 Waiting for client to connect...")

conn, addr = s.accept()
print("✅ Connected to client:", addr)

# --- Chat & DHT Threads ---
chat_log = []

def recv_thread():
    while True:
        try:
            data = conn.recv(1024)
            if data:
                text = data.decode().strip()
                print(f"\n📩 [Client]: {text}")
                chat_log.append(f"Client → Server: {text}")
                print("🟢 You: ", end='')
        except:
            pass

_thread.start_new_thread(recv_thread, ())

def dht_thread():
    while True:
        try:
            dht_sensor.measure()
            t = dht_sensor.temperature()
            h = dht_sensor.humidity()
            msg = f"[DHT11] Server Temp={t}°C, Hum={h}%"
            conn.send(msg.encode())
            chat_log.append(f"Server → Client: {msg}")
            time.sleep(5)
        except:
            pass

_thread.start_new_thread(dht_thread, ())

# --- Initial Hello ---
hello_msg = "Hello Client 👋"
conn.send(hello_msg.encode())
chat_log.append(f"Server → Client: {hello_msg}")
print("🟢 Sent:", hello_msg)

# --- Manual Chat ---
while True:
    msg = input("🟢 You: ").strip()
    if msg.lower() == 'exit':
        print("Closing chat...")
        break
    if msg:
        formatted = f"Server → Client: {msg}"
        conn.send(formatted.encode())
        chat_log.append(formatted)

conn.close()
s.close()
