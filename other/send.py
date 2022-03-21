# python 3.6
import json
import random
import time

from paho.mqtt import client as mqtt_client

broker = '119.91.122.58'
port = 1883
topic = "DHT"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(60)
        tem = random.randint(-20, 60)
        hum = random.randint(0, 100)
        data = {"DHT11": {"tem": tem, "hum": hum}}
        r = json.dumps(data)
        result = client.publish(topic, r)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{r}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
