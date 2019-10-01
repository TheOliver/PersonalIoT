'''
This script is used to stock every datas in the influxDB data base.
It must be hosted by the influxdB Host.
Systemd service: influxdbMQTT.service
'''


from influxdb import InfluxDBClient
import paho.mqtt.client as mqtt
from datetime import datetime
import json
import time

'''
Function on_message is an overload from the paho library
Description:
This function pull all the message which are transiting through the MQTT network.
After that it open a connection with the 'MQTT' data base in influxDB.
And finally writte the message.

The messages traveling through the MQTT network must be preformated for the influxdb format
'''

def on_message(client, userdata, message):
    messageMQTT=json.loads(message.payload.decode())
    clientdb= InfluxDBClient(host='localhost',  port=8086) #connect to the influx db data base
    clientdb.switch_database('MQTT')
    result=clientdb.write_points((messageMQTT))
    
SERVEUR='localhost'
client=mqtt.Client() # creating the client
client.on_message=on_message # overloading
client.connect(SERVEUR,1883,300) #beginning MQTT broker connection

client.loop_start() # strating loop
# following lines are the MQTT topics we want to store in the database
client.subscribe("<HOSTNAME1>_channel") 
client.subscribe("<HOSTNAME2>_channel")
client.subscribe("<HOSTNAME3>_channel")
client.subscribe("<HOSTNAME4>_channel")
client.subscribe("TIME_channel/#")

# here is a special topic that I use for personnal project
client.subscribe("IoT/#")

time.sleep(600) # waiting 600 sec for ending this script (Systemd will reload it = it is a service)
client.loop_stop()
client.disconnect()
