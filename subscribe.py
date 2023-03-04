from paho.mqtt import client as mqtt_client
import random
import json
import convertEpoch
import storeData

broker = '192.168.1.47'
port = 1883
topics = ["sensor", "sensor2", "sensor3"]
# generate client ID with pub prefix randomly
client_id = f'user-{random.randint(0, 100)}'
username = 'admin'
password = '1234'

part = 1
temp = 'message'

def connect_mqtt() -> mqtt_client:
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

def subscribe(client: mqtt_client):
    def on_message(client, userdata, message):
        global part
        global temp
        # convert the message payload to a string
        message_parts = ''.join(message.payload.decode())
        
        if part == 2:
            full_message = temp + message_parts
            payload = json.loads(full_message)
            print('Receive\n' + json.dumps(payload) + ' \nfrom ' + message.topic + '\n')
            
            epoch_time = int(json.dumps(payload['Time'])) / 1000
            time = convertEpoch.convertEpoch(epoch_time)

            storeData.pushData(
                json.dumps(payload['Node']),
                time, 
                json.dumps(payload['Humidity']), 
                json.dumps(payload['Temperature']), 
                json.dumps(payload['ThermalArray'])
            )
            part = 0
        elif part == 1:
            temp = message_parts
        part += 1
    client.subscribe([(t, 0) for t in topics])
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
