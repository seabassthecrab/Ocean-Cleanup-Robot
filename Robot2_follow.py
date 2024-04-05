import paho.mqtt.client as mqtt
import time

mqtt_broker_ip = "your_mqtt_broker_ip"
mqtt_port = 1883
robot1_topic = "robot1/move"
robot2_topic = "robot2/move"

# Connect to the MQTT broker
client = mqtt.Client()
client.connect(mqtt_broker_ip, mqtt_port, 60)
def control_robot1():
    while True:
        key = input("Enter command (w/a/s/d): ")
        if key == "w":
            # Move forward
            client.publish(robot1_topic, "forward")
        elif key == "a":
            # Turn left
            client.publish(robot1_topic, "left")
        elif key == "s":
            # Move backward
            client.publish(robot1_topic, "backward")
        elif key == "d":
            # Turn right
            client.publish(robot1_topic, "right")