# MQTT using Mosquitto

This project has an academic purpose, but can be used to exemplify a basic implementation with MQTT.

#### Student

* Gustavo Marttos, 536202

### How-to

Pull the Docker container running the following command:

```
docker run -it --name mosquitto -p 1883:1883 -p 9001:9001 marttosc/mosquitto:latest
```

Then, open another terminal and run the following command:

```
python mosquitto.py YOUR_DOCKER_IP
```

If an error occurs, make sure you have installed the "paho-mqtt" library using `pip install paho-mqtt`.

### Example

```
python mosquitto.py 172.0.0.1
```

### What is and how it works

MQTT is a lightweight messaging protocol that provides resource-constrained network clients with a simple way to distribute telemetry information. The protocol, which uses a publish/subscribe communication pattern, is used for machine-to-machine (M2M).

The protocol allows devices to send (publish) information about a given topic to a server that functions as an MQTT message broker. The broker then pushes the information out to those clients that have previously subscribed to the client's topic.

