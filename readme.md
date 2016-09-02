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

