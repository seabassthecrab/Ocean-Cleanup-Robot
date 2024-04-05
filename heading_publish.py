import paho.mqtt.client as mqtt
import time

mqtt_broker = "your_broker_ip"
mqtt_port = 1883
mqtt_topic = "heading"

mqtt_client = mqtt.Client()
mqtt_client.connect(mqtt_broker, mqtt_port)


def publish_heading(heading):
    mqtt_client.publish(mqtt_topic, str(heading))


while True:
    # Read heading from file
    with open("heading_data.txt", "r") as file:
        heading_value = float(file.read().strip())

    # Perform calculations with the heading value
    # For example, let's double the heading value
    #modified_heading = heading_value * 2

    # Publish modified heading to MQTT topic
    #publish_heading(modified_heading)
    publish_heading(heading_value)

    time.sleep(1)  # Adjust sleep time as needed