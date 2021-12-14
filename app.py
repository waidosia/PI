import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/data')
def data():
    dict = {}
    conn = sqlite3.connect('db/database.sqlite', check_same_thread=False)
    c = conn.cursor()
    cursor = c.execute("select tem,hum from dht order by id DESC limit 1")
    for row in cursor:
        dict[str(row[0])] = str(row[1])
    conn.close()
    return dict


if __name__ == '__main__':
    app.run()
