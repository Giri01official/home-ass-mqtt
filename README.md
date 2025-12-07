Home Assistant MQTT Assignment
Student Details

    Name: Giridharan S
    Register Number: 42110367

Project Overview

This project demonstrates Python to MQTT to Home Assistant integration. Sensor values are published using a Python script to a unique MQTT topic and displayed live in the Home Assistant dashboard.
MQTT Details

    Broker: Mosquitto (Windows)
    Topic: home/Giridharan-2025/sensor

Sensors Implemented

    Temperature (25°C)
    Humidity (40%)
    Light Intensity (350 lux)

Files in This Repository

    sensor_publish.py : Python script to publish sensor data
    screenshots/ : Contains Home Assistant and MQTT output screenshots
    summary.pdf : One-page assignment summary
    README.md : Project documentation

Steps Followed

    Installed Home Assistant OS using VirtualBox on Windows.
    Installed and configured Mosquitto MQTT broker.
    Developed a Python script to publish sensor data to MQTT.
    Configured MQTT integration in Home Assistant.
    Displayed live sensor values on the Home Assistant dashboard.

How to Run

    Start Mosquitto on Windows.
    Run the Python script: python sensor_publish.py
    Open Home Assistant dashboard to view live updates.

Output
Sensor values update every 5 seconds in Home Assistant.
