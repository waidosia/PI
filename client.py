# data = {"DHT11": {"tem": tem, "hum": hum}}
# 连接MQTT服务器
import json
import sqlite3
from paho.mqtt import client as mqtt_client
import time

CLIENT_ID = "PI"  # 设备标识
SERVER = '119.91.122.58'  # MQTT地址
PORT = 1883  # 端口


def insert_dt(dd):
    try:
        conn = sqlite3.connect('db/database.sqlite')
        c = conn.cursor()
        c.execute(
            "insert into dht (tem, hum, datetime, deviceID) VALUES ({},{},{},{});".format(dd['tem'], dd['hum'],
                                                                               int(time.time()),8266))
                                                                                
        print('DHT插入成功')
        conn.commit()
        conn.close()

    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()


def insert_l(ll):
    try:
        conn = sqlite3.connect('db/database.sqlite')
        c = conn.cursor()
        c.execute(
            "insert into light (strength, datatime,deviceID) VALUES ({},{},{});".format(ll['light'],
                                                                                 int(time.time()),32))

        print('Light插入成功')
        conn.commit()
        conn.close()

    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()     


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(CLIENT_ID)
    client.on_connect = on_connect
    client.connect(SERVER, PORT)
    return client


def on_message(client, userdata, msg):
    d = msg.payload.decode()
    dd = json.loads(d)
    if 'DHT11' in dd:
        print(dd['DHT11'])
        insert_dt(dd['DHT11'])
    else:
        print(dd['Light'])
        insert_l(dd['Light'])


def subscribe(client: mqtt_client):
    client.subscribe('mqttx/#')
    client.on_message = on_message


def main():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()



if __name__ == '__main__':
    main()
