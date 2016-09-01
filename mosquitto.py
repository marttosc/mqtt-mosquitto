import paho.mqtt.client as mqtt
import sys

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("hello/world")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

def on_disconnect(client, userdata, rc):
    print("Exiting ~> " + str(rc))

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(str(sys.argv[1]), 1883, 60)

client.subscribe("hello/world")

client.publish("hello/world", "hello, how are you?")

client.loop_forever()

