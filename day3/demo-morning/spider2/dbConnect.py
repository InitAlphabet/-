"""
make it try to connect the database
"""

import mysql.connector

config = {
    "host": 'localhost',
    "user": 'root',
    "password": '123456',
    "database": 'lab4'
}


def select(sql_handle=None):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    if sql_handle is None:
        print("please input handles")
        return None
    else:
        cursor.execute(sql_handle)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res


def insert(sql_handle=None):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print(sql_handle)
    if sql_handle is None:
        print("please input handles")
        return 0
    else:
        cursor.execute(sql_handle)
        res = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return res


def update(sql_handle=None):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print(sql_handle)
    if sql_handle is None:
        print("please input handles")
        return 0
    else:
        print(sql_handle)
        cursor.execute(sql_handle)
        res = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return res


def change(sql_handle=None):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    if sql_handle is None:
        print("please input handles")
        return None
    else:
        rows = cursor.execute(sql_handle)
        conn.commit()
        cursor.close()
        conn.close()
        return rows


def get_file(fileID):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM files WHERE fileID = %s', [fileID])
    file = cursor.fetchone()
    cursor.close()
    conn.close()
    if file:
        return file
    else:
        return None


def table_exists(table_name):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    sql = f"SHOW TABLES LIKE '{table_name}'"
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is not None


def save_file(fileID, data):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO files (fileID, file) VALUES (%s, %s)', (fileID, data))
        conn.commit()
        conn.close()
        return True
    except mysql.connector.IntegrityError:
        return False
    finally:
        cursor.close()
        conn.close()
