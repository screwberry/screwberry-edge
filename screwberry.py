#!/usr/bin/env python3

from ruuvitag_sensor.ruuvi import RuuviTagSensor
from azure.iot.device import IoTHubDeviceClient, Message
import datetime
import config as cfg

stored = {}

def handle_data(input):
    input[1]['time'] = datetime.datetime.now().timestamp()
    if input[0] not in stored:
        print("Identified new sensor: " + input[0])
        send_data(input)
    else:
        # Send data if any value has changed more than set threshold
        for check in cfg.THRESHOLDS.items():
            if round(abs(stored[input[0]][check[0]] - input[1][check[0]]),2) >= check[1]:
                send_data(input)
    
def send_data(input):
    stored[input[0]] = input[1]
    msg_txt_formatted = cfg.MESSAGE.format(time=input[1]['time'],
                                   alias = cfg.ALIASES.get(input[0], input[0]),
                                   temperature=input[1]['temperature'],
                                   humidity=input[1]['humidity'],
                                   pressure=input[1]['pressure'],
                                   acceleration=input[1]['acceleration'])
    message = Message(msg_txt_formatted)
    #message.custom_properties["unit"] = input[0]
    print( "Sending: {}".format(message) )
    client.send_message(message)
    
def exception_factory(msg, e):
    print( "ERROR:", msg )
    print( e )

if __name__ == '__main__':
    try:
        client = IoTHubDeviceClient.create_from_connection_string(cfg.CONNECTION_STRING)
    except ValueError as e: exception_factory("Connection to IoT Hub failed:", e)
    else:
        try:
            print ( "Connection to IoT Hub established (Ctrl-C to exit)" )
            RuuviTagSensor.get_datas(handle_data)
        except AttributeError as e: exception_factory("Error in configuration:", e)
    finally:
        print ( "Exiting..." ) 