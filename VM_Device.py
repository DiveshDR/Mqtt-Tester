import paho.mqtt.client as mqtt
import time
import json
import random
from datetime import datetime

# MQTT broker details
broker = "127.0.0.1"  # Replace with your broker address
port = 1883  # Default MQTT port
topic = "GJ27DM7582"  # Replace with your topic

# Create a client instance
client = mqtt.Client()

# Set username and password
client.username_pw_set("test", "test")

# Connect to the broker
client.connect(broker, port)

try:
    for _ in range(1000):  # Removed the number variable
        # Generate random values for additional data
        status = random.choice([0, 1])
        fuel_level = random.randint(1, 100)
        lolb = random.choice([0, 1])
        latitude = round(random.uniform(-90.0, 90.0), 6)
        longitude = round(random.uniform(-180.0, 180.0), 6)
        running_hours = random.randint(1, 24)
        temperature = random.randint(1, 100)
        fuel_consumption = random.randint(2, 50)  # Random fuel consumption between 2L and 50L
        bt_voltage = 12  # Fixed battery voltage at 12V
        bt_charge_status = 1  # Fixed battery charge status at 1
        
        # Get the current RTC timestamp in YYYY-MM-DD HH:MM:SS format
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # Create a JSON object with all the data
        payload = {
            "Timestamp": timestamp,
            "Status": status,
            "FuelLevel": fuel_level,
            "LOLB": lolb,
            "Latitude": latitude,
            "Longitude": longitude,
            "RunningHours": running_hours,
            "Temperature": temperature,
            "FuelConsumption": fuel_consumption,
            "BatteryVoltage": bt_voltage,
            "BatteryChargeStatus": bt_charge_status
        }
        
        # Convert the payload to JSON format
        payload_json = json.dumps(payload)
        
        # Publish the JSON payload to the topic
        client.publish(topic, payload_json)
        print(f"Published {payload_json} to {topic}")
        
        # Wait for 1 second
        time.sleep(2)

except KeyboardInterrupt:
    print("Process interrupted")

finally:
    # Disconnect from the broker
    client.disconnect()
