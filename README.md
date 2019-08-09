# PersonalIoT
Create your own IoT platform in few minutes
# What do you need ?
I am doing this main projet using raspberry pi and arduino.
You can use any distribution for this project
But it is better to you use linux based distribution because this tutorial contains some explanations about Systemd

Summary:
1- Presentation
2- Installing Docker
3 - Using DOcker
4 - Microservices
5 - deploy Python scripts with systemd


# Global configuration
![Configuration](https://github.com/TheOliver/PersonalIoT/blob/master/reseau.png)

MQTT is a great protocol because is multiplatform. It is using Publish/Subscribe communication.
It is well explained on this page : https://en.wikipedia.org/wiki/MQTT

So any hardware, any OS and any distribution can communicate with this MQTT solution.

The technical choice that I have made is to host the MQTT broker and the database (+ its client) in the same hardware.
All the things in the MQTT broker is red and stocked in a influxDB database and displayed with the official client: Chronograf.

# System Architecture
![Architecture](https://github.com/TheOliver/PersonalIoT/blob/master/Architecture.png)

