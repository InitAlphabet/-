"""
make it try to connect the database
"""

import mysql.connector

config = {
    "host": 'localhost',  # 数据库主机
    "user": 'root',  # 数据库用户
    "password": '123456',  # 用户密码
    "database": 'lab4'  # 数据库名
}


def select(sql_handle=None):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    if sql_handle is None:
        print("please input handles")
        return None
    else:
        print("sql:", sql_handle)
        cursor.execute(sql_handle)
        res = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return res


def update(sql_handle=None):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    if sql_handle is None:
        print("please input handles")
        return 0
    else:
        print("sql:", sql_handle)
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
        print("sql:", sql_handle)
        rows = cursor.execute(sql_handle)
        conn.commit()
        cursor.close()
        conn.close()
        return rows


def table_exists(table_name):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    if table_name is None:
        print("please input table_name")
        return None
    else:
        print("sql_handle:", f"SHOW TABLES LIKE '{table_name}'")
        cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
        res = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return res is not None
