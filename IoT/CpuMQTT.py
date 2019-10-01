'''
This python script is a basical example of MQTT messages possibilities
It is sending host internal stats to the MQTT borker like cpu, diskusage and temperature
Systemd service: internalStats.service
'''

import paho.mqtt.client as mqtt
import json
from datetime import datetime
import time
import psutil
import re
import os

#os.environ['TARGET_IP']='<yourMQTTServer_IP>' # used for debug
SERVEUR=str(os.environ['TARGET_IP']) # environement variables are defined in the ConfigEnv.env file declare in the service
#SERVEUR='<yourMQTTServer_IP>' # used for debug
HOSTNAME=str(os.environ['HOSTNAME']) 

# starting the connection with the MQTT broker
client=mqtt.Client()
client.connect(SERVEUR,1883,60)
client.loop_start()

string_diskUsage=psutil.disk_usage('/') #collect disk usage at the source in a string
string_temperature=psutil.sensors_temperatures() #collect temperature in a string
cpu=psutil.cpu_percent() #collect cpu

#CPU string treatment
diskUsage=re.findall(r'\w+',  str(string_diskUsage)) #string reduction
float_diskUsage=float(diskUsage[8]+"."+diskUsage[9]) # collect the float in the string

#Temperature string treatment
temperature=re.findall(r'\w+', str(string_temperature))
temperature_string=temperature[5]+"."+temperature[6]
float_temperature=float(temperature_string)

ctime=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ') # date time for the influxdb time trace
json_body = [
    {
        "measurement": "mqtt_publish",
        "tags": {
            "sender": HOSTNAME
        },
        "time": ctime,
        "fields": {
            "CPU": float(cpu), 
            "Temperature": float_temperature, 
            "DiskUsage":float_diskUsage
        }
    }
    ]
#the json_body format must be exactly like that, "measurement", "tags", "time" and "fields" must appear for the influxdb storage format
client.publish(HOSTNAME+'_channel',json.dumps(json_body),1) #publishing to the MQTT broker
    
time.sleep(2) # waiting 2 sec (after that systemd will reload the script)

client.loop_stop()
client.disconnect()
