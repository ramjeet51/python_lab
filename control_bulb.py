import json
import time
import paho.mqtt.client as mqtt

# MQTT broker details
BROKER = 'localhost'
PORT = 1883
TOPIC = 'home/bulb'

# Initialize the MQTT client
mqtt_client = mqtt.Client()

# Connect callback
def on_connect(client, userdata, flags, rc):
        if rc == 0:
                    print("Connected to MQTT broker")
        else:
                                    print(f"Failed to connect, return code {rc}")

                                    # Message publish callback
                                    def on_publish(client, userdata, mid):
                                            print("Message published")

                                            # Set callback functions
                                            mqtt_client.on_connect = on_connect
                                            mqtt_client.on_publish = on_publish

                                            # Connect to the MQTT broker
                                            mqtt_client.connect(BROKER, PORT, 60)

                                            # Start the network loop in a separate thread
                                            mqtt_client.loop_start()

                                            # Function to turn the bulb on
                                            def turn_on_bulb():
                                                    payload = {
                                                                    "state": {
                                                                                    "desired": {
                                                                                                        "power": "ON"
                                                                                                                    }
                                                                                            }
                                                                        }
                                                    mqtt_client.publish(TOPIC, json.dumps(payload))

                                                        # Function to turn the bulb off
                                            def turn_off_bulb():
                                                                payload = {
                                                                                "state": {
                                                                                                "desired": {
                                                                                                                    "power": "OFF"
                                                                                                                                }
                                                                                                        }
                                                                                    }
                                                                mqtt_client.publish(TOPIC, json.dumps(payload))

                                                                    # Example usage
                                            if _name_ == "_main_":
                                                                            turn_on_bulb()  # Turn the bulb on
                                                                            time.sleep(2)   # Wait for 2 seconds
                                                                            turn_off_bulb() # Turn the bulb off
                                                                                        # Stop the MQTT network loop
                                                                            mqtt_client.loop_stop()
                                                                            mqtt_client.disconnect()
