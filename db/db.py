import sqlite3

conn = sqlite3.connect('database.sqlite')
print("Opened database successfully")
c = conn.cursor()
c.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY NOT NULL,
        tem INT NOT NULL,
        hum INT NOT NULL,
       datetime DATETIME NOT NULL);
       ''')
print("Table created successfully")
conn.commit()
conn.close()
