import json
import dbConnect as db
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import re
import requests
import pandas as pd


def get_greatriver():
    url = 'http://xxfb.mwr.cn/hydroSearch/greatRiver'

    data = {
        "messtype": "json",
        "page": 1,
        "size": 50,
        "callback": "jQuery1830426658582613074_1469201131959",
        "_": "1469201133189",
        ' contentType': 'application/json; charset=utf-8'
    }
    response = requests.post(url, data=data)
    response = response.json()
    datas = response["result"]
    data_detail = datas.get("data")
    colums = list(data_detail[0].keys())
    create_table(colums, "greatriver")
    for line in data_detail:
        insert(line, "greatriver")
    print("greateRiver complete")

    # 创建数据库连接将数据写入表中


def get_greatRsvr():
    url = 'http://xxfb.mwr.cn/hydroSearch/greatRsvr'

    data = {"messtype": "json",
            "page": 1,
            "size": 50,
            "callback": "jQuery1830426658582613074_1469201131959",
            "_": "1469201133189",
            ' contentType': 'application/json; charset=utf-8'
            }
    school_datas = requests.post(url, data=data).json()
    datas = school_datas["result"]
    datadetail = datas.get("data")
    colums = list(datadetail[0].keys())
    create_table(colums, "greatRsvr")
    for line in datadetail:
        insert(line, "greatRsvr")

    # 创建数据库连接将数据写入表中

    print("greateRsvr complete")


def get_pointHydroInfo():
    url = 'http://xxfb.mwr.cn/hydroSearch/pointHydroInfo'

    data = {"messtype": "json",
            "page": 1,
            "size": 50,
            "callback": "jQuery1830426658582613074_1469201131959",
            "_": "1469201133189",
            }
    school_datas = requests.post(url, data=data).json()
    datas = school_datas["result"]
    datadetail = datas.get("data")
    colums = list(datadetail[0].keys())
    create_table(colums, "pointHydroInfo")
    for line in datadetail:
        insert(line, "pointHydroInfo")

    print("pointHydroInfo complete")


def create_table(columns, table_name):
    if db.table_exists(table_name):
        return
    create_table_sql = f"CREATE TABLE {table_name} ("

    for column in columns:
        create_table_sql += f"{column} VARCHAR(255), "

    create_table_sql = create_table_sql.rstrip(", ") + ")"  # 移除最后一个逗号并闭合括号
    db.update(create_table_sql)


def insert(data_dict, table_name):
    columns = ', '.join(data_dict.keys())
    values = []
    for x in data_dict.values():
        values.append("'" + str(x) + "'")
    values = ','.join(values)
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    db.insert(sql)


def work():
    get_greatriver()
    get_greatRsvr()
    get_pointHydroInfo()


def main():
    work()


if __name__ == "__main__":
    main()
