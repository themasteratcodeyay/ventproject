import sys
import Adafruit_DHT
import time

print("Test")
while True:
    print("enter while loop")
    humidity, temperature = Adafruit_DHT.read_retry(11, 17)
    print(humidity)
    print(temperature)
    # print('Temp: {0:0.1f} C Humidity: {1:0.1f}%'.format(temperature, humidity))
    time.sleep(1)