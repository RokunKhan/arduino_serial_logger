# Arduino Serial Logger

This project logs temperature and humidity data from an Arduino over serial using Python.

## 🔧 Components Used
- Arduino Uno (or compatible)
- DHT11 Temperature & Humidity Sensor
- Python 3
- pyserial library

## 📂 Files
- `arduino_logger.ino` – Arduino code that reads sensor data and sends it over serial.
- `serial_logger.py` – Python script that receives and logs serial data from the Arduino.

## 🚀 How It Works
- The Arduino reads temperature and humidity using the DHT11 sensor.
- It sends that data over the serial port.
- The Python script reads it in real time and displays/logs it.

## 🧠 Skills Applied
- Serial communication (UART)
- Sensor integration (DHT11)
- Python scripting
- Embedded systems
- Data acquisition & visualization basics

## 📌 Future Improvements
- Add CSV or database logging
- Integrate GPS or other sensors
- Build a GUI using Tkinter or PyQt

---

> Developed as part of an electrical engineering hands-on logging system project.
