import serial
import time

ser = serial.Serial('COM7', 9600)
time.sleep(2)  

try:
    while True:
        data = ser.readline().decode('utf-8').strip()
        print(data)
        time.sleep(1) 

except KeyboardInterrupt:
    print("\nLogging stopped by user.")
    ser.close()
