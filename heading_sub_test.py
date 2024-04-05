import paho.mqtt.client as mqtt
import time
import math

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


    def on_message(client, userdata, msg):
        received_heading = float(msg.payload.decode())
        own_heading = heading_value()
        print("Received Heading:", received_heading)
        print("Own Heading:", own_heading)
        if abs(received_heading - own_heading) < 10:  # Adjust the threshold as needed
            print("Headings are close.")
        else:
            print("Headings are not close.")


    # Initialize MQTT Client
    mqtt_client = mqtt.Client()

    # Set up MQTT callbacks
    mqtt_client.on_message = on_message

    # Connect to MQTT Broker
    mqtt_client.connect(mqtt_broker, mqtt_port)

    # Subscribe to MQTT topic
    mqtt_client.subscribe(mqtt_topic)

    # Start the MQTT loop
    mqtt_client.loop_forever()

    time.sleep(0.03)  # Adjust sleep time as needed