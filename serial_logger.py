import serial
import time

# Replace COM7 with your actual COM port if needed
ser = serial.Serial('COM7', 9600)
time.sleep(2)  # Allow serial connection to settle

try:
    while True:
        data = ser.readline().decode('utf-8').strip()
        print(data)
        time.sleep(1)  # Optional: slow down printing

except KeyboardInterrupt:
    print("\nLogging stopped by user.")
    ser.close()
