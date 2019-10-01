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
- The second one is called HOST. It hosts several docker containers that makes the system works (it is the big blue BOX in the "Global configuration").
it hosts: influxdb, chronograf and the MQTT broker, which are all pulled from docker hub
- The third one is called THIRD. It is connected to sensors using I2C connection with a raspberry pi

# installing docker
Installing Docker is quite simple, you just have to execute one command:
```
curl -sSL https://get.docker.com | sh
```
# pulling the images

- influxdb
```
docker pull influxdb
```
- chronograf
```
docker pull chronograf
```
- MQTT
```
docker pull eclipse-mosquitto
```

# Creating containers
- chronograf:
```
docker run -dp 8888:8888 --name CHRONOGRAF --restart always chronograf
```
- MQTT
```
docker run -it -dp 1883:1883 -- name MQTT --restart always eclipse-mosquitto
```
- influxdb
```
docker run -p 8086:8086 influxdb
```
It is kind of usefull to use the -v argument to use your own local file configuration, but we are not going to use it.

# Configuring your Chronograf
- Go to the http:/localhost:8888
The chronograf page will appear.

Configure it with the influxdb adress using the ip of your host (ip a) http:/<localhostIPadress>:8086

After that create a database named MQTT

# testing MQTT
This section is kind of important if you want test your MQtt configuration

All the details are in the docker hub page :https://hub.docker.com

