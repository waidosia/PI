import hashlib
import sqlite3


def login_s(uname, passwd):
    try:
        m = hashlib.md5()
        m.update(passwd.encode("utf8"))
        passwd = m.hexdigest()
        conn = sqlite3.connect('db/database.sqlite', check_same_thread=False)
        c = conn.cursor()
        sql = "select * from login where username = '{}' and passwd = '{}'".format(uname, passwd)
        cur = c.execute(sql)
        results = cur.fetchone()
        if results:
            return 'ok'
        else:
            return 'error'
    except Exception as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    print(login_s('admin', 'admin'))
