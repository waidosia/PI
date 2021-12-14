import datetime
import sqlite3
import time


def query(stars, end):
    _, tem, hum = [], 0, 0
    try:
        conn = sqlite3.connect('db/database.sqlite', check_same_thread=False)
        c = conn.cursor()
        cursor = c.execute("select tem,hum from dht where datetime between {} and {}".format(stars, end))
        for row in cursor:
            _.append(row)
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()
        if len(_) == 0:
            return (tem, hum)
        for i in _:
            tem += i[0]
            hum += i[1]
        tem = round(tem / len(_), 2)
        hum = round(hum / len(_), 2)
        return (tem, hum)

def rtdb():
    tem, hum =  0, 0
    try:
        conn = sqlite3.connect('db/database.sqlite', check_same_thread=False)
        c = conn.cursor()
        cursor = c.execute("select tem,hum from dht order by ID DESC LIMIT 1")
        for row in cursor:
            tem = row[0]
            hum = row[1]
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()
        return (tem,hum)

def queryList():
    now_time = time.localtime(time.time())
    today = datetime.date.today()
    hour = now_time.tm_hour
    tem, hum = [], []
    l1 = [i for i in range(hour, -1, -1)]
    l2 = [i for i in range(23, hour, -1)]
    for i in l1:
        dt = str(today) + " " + str(i)
        ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H")))
        ts_next = ts + 3600
        s = query(ts, ts_next)
        tem.append(s[0])
        hum.append(s[1])
    for i in l2:
        yesterday = today + datetime.timedelta(-1)
        dt = str(yesterday) + " " + str(i)
        ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H")))
        ts_next = ts + 3600
        s = query(ts, ts_next)
        tem.append(s[0])
        hum.append(s[1])

    return (tem,hum)


if __name__ == '__main__':
    print(queryList())
    print(rtdb())



