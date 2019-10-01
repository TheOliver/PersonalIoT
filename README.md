# PersonalIoT
Create your own IoT platform in few minutes
# What do you need ?
I am doing this main projet using raspberry pi and arduino.
You can use any distribution for this project
But it is better to use linux based distribution because this tutorial contains some explanations about Systemd.

Covered Topics:
- Presentation
- Installing Docker
- Using Docker
- Microservices



# Global configuration
![Configuration](https://github.com/TheOliver/PersonalIoT/blob/master/reseau.png)

MQTT is compatible on multiple platforms. It is publish-subscribe based messaging protocol.
It is well explained on this page : https://en.wikipedia.org/wiki/MQTT
A lot of big companies are using this protocol for IoT applications.

Any hardware, any OS and any distribution can communicate with this MQTT solution.

The technical choice that I have made is to host the MQTT broker and the database (+ its client) in the same hardware.
All the things in the MQTT broker is red and stocked in a influxDB database and displayed with the official client: Chronograf.

# System Architecture
![Architecture](https://github.com/TheOliver/PersonalIoT/blob/master/Architecture.png)

# My Architecture

I am using 3 raspberry pi.
- The 1rst one is called ONE. It hosts the wifi using RaspAp.
- The second one is called HOST. It hosts several docker containers that makes the system works (it is the big blue BOX in the Architecture).
it hosts: influxdb, chronograf and the MQTT broker, which are all pulled from docker hub
- The third one is called THIRD. It is connected to sensors using I2C connection with a raspberry pi
