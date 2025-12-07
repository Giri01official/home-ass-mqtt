import time
import random
import paho.mqtt.client as mqtt

BROKER = "127.0.0.1"
PORT = 1883
BASE_TOPIC = "home/giridharan-2025/sensor"

client = mqtt.Client()
client.connect(BROKER, PORT, 60)

try:
    while True:
        temp = round(20 + random.random()*10, 1)       # 20.0 - 30.0 C
        hum  = round(40 + random.random()*40, 0)       # 40 - 80 %
        sound = round(30 + random.random()*40, 1)     # 30 - 70 dB

        client.publish(f"{BASE_TOPIC}/temperature", temp)
        client.publish(f"{BASE_TOPIC}/humidity", hum)
        client.publish(f"{BASE_TOPIC}/sound_db", sound)

        print("Published:", temp, hum, sound)
        time.sleep(5)

except KeyboardInterrupt:
    print("Stopped")
    client.disconnect()
