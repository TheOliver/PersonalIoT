import paho.mqtt.client as mqtt
import json
from datetime import datetime
import time
import os

def on_message(client, userdata, message):
    messageMQTT=json.loads(message.payload.decode())
    print(messageMQTT[0]['tags']['sender'])
    nom=messageMQTT[0]['tags']['sender']
    #print(messageMQTT[0]['fields'])
    SERVEUR=str(os.environ['TARGET_IP'])
    #SERVEUR='<MQTT_IP_SERVER>' 
    
    client=mqtt.Client()
    client.connect(SERVEUR,1883,60)
    Heure=str(datetime.now().time())
    #print(Heure)
    Hour=Heure[0:2]
    Minutes=Heure[3:5]
    Seconds=Heure[6:8]
    #print(Hour)
    #print(Minutes)
    #print(Seconds)
    ctime=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    json_body = [
    {
        "measurement": "mqtt_publish",
        "tags": {
            "sender": HOSTNAME
        },
        "time": ctime,
        "fields": {
            "Hour": int(Hour), 
            "Minutes":int(Minutes), 
            "Seconds":int(Seconds)
        }
    }
    ]
    client.publish('TIME_channel/SET'+str(nom),json.dumps(json_body),1)
    client.loop_stop()
    client.disconnect()


SERVEUR=str(os.environ['TARGET_IP'])
#SERVEUR='<your_IP_MQTT_SERVER' # used for debug
HOSTNAME=str(os.environ['HOSTNAME'])
#HOSTNAME='<your_HOST_NAME>' #used for debug
client=mqtt.Client()
client.on_message=on_message
client.connect(SERVEUR,1883,60)

client.loop_start()
client.subscribe("TIME_channel/ASK")


message={}


ctime=datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
json_body = [
    {
        "measurement": "mqtt_publish",
        "tags": {
            "sender": HOSTNAME
        },
        "time": ctime,
        "fields": {
            "HeartB": 1
        }
    }
    ]
    
client.publish('TIME_channel/ASK',json.dumps(json_body),1)
    
time.sleep(300)

client.loop_stop()
client.disconnect()
