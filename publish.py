from paho.mqtt import client as mqtt_client
import random
import time
import json
import readData
import uuid
import sys

# check if a topic is provided
if len(sys.argv) != 2: 
    print('Please include a topic')
    exit()

# topic = "sensor"
broker = '192.168.1.47'
port = 1883
topic = sys.argv[1]
# generate client ID with pub prefix randomly
client_id = f'user-{random.randint(0, 1000)}'
username = 'admin'
password = '1234'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    time.sleep(1)
    chunk_size = 250
    msg_count = 0
    for row in json.loads(readData.data):
        # generate random unique id
        nodeId = str(uuid.uuid4().int)[:4]
        row['Node'] = int(nodeId)
        msg = f"messages: {msg_count}"
        message = json.dumps(row)
        
        # publish message as a part
        for i in range(0, len(message), chunk_size):
            chunk = message[i:i+chunk_size]
            result = client.publish(topic, chunk)
            
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        time.sleep(180)

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    client.loop_stop()

if __name__ == '__main__':
    run()
