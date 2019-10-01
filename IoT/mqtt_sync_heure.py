import paho.mqtt.client as mqtt
import json
from datetime import datetime
import time
import os
def on_message(client, userdata, message):
    messageMQTT=json.loads(message.payload.decode())
    print(messageMQTT)
    HH=messageMQTT[0]['fields']['Hour']
    MM=messageMQTT[0]['fields']['Minutes']
    SS=messageMQTT[0]['fields']['Seconds']
    phrase="date -s '"+str(HH)+":"+str(MM)+":"+str(SS)+"'"
    os.system(phrase)



SERVEUR=str(os.environ['TARGET_IP'])
#SERVEUR='<MQTT_SERVER_IP' # used for debug
HOSTNAME=str(os.environ['HOSTNAME'])
#HOSTNAME='<YOUR_HOSTNAME>' #used for debug
client=mqtt.Client()
client.on_message=on_message
client.connect(SERVEUR,1883,60)
client.subscribe("TIME_channel/SET"+str(HOSTNAME))
client.loop_start()


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
