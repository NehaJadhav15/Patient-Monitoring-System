import serial
import time
import schedule
import urllib

import threading
from urllib.request import urlopen


def thingspeak_post(i,n,p):
    threading.Timer(15, thingspeak_post).start()

    URL = 'https://api.thingspeak.com/update?api_key='
    KEY = 'FIZS3NV2PNE3WCCO'
    HEADER = '&field1={}&field2={}&field3={}'.format(i, n, p)

    NEW_URL = URL+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)


def main_func():
    arduino = serial.Serial('com1', 9600)
    print('Established serial connection to Arduino')
    arduino_data = arduino.readline()

    decoded_values = str(arduino_data[0:len(arduino_data)].decode("utf-8"))
    list_values = decoded_values.split('x')

    for item in list_values:
        list_in_floats.append(float(item))
    a=list_in_floats[0];
    b=list_in_floats[1];
    c=list_in_floats[2];
    thingspeak_post(a,b,c);

    print(f'Collected readings from Arduino: {list_in_floats}')

    arduino_data = 0
    list_in_floats.clear()
    list_values.clear()
    arduino.close()


# ----------------------------------------Main Code------------------------------------
# Declare variables to be used
list_values = []
list_in_floats = []

print('Program started')

# Setting up the Arduino
schedule.every(2).seconds.do(main_func)


while True:
    schedule.run_pending()
    time.sleep(1)


