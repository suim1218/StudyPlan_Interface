# coding=utf-8
import pymysql.cursors
import os
import configparser as cparser
from utils.read_config import read_config

# ======== Reading config.ini setting ===========


host = read_config().get('host')
port = read_config().get('port')
db = read_config().get('db')
user = read_config().get('user')
password = read_config().get('password')


# ======== MySql base operating ===================
class DB:
    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # clear table data
    def clear(self, table_name):
        # real_sql = "truncate table " + table_name + ";"
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"
        key = ','.join(table_data.keys())
        # print(key)
        value = ','.join(table_data.values())
        # print(value)
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        # print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()

    # close database
    def close(self):
        self.connection.close()

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()


'''
if __name__ == '__main__':
    db = DB()
    table_name = "sys2_org"
    data = {'ORG_ID': 0, 'ORG_NAME': '管理部门', 'ORG_CODE': 0, 'ORG_ADDR': '',
            'ORG_LEVEL': 0, 'ORG_IS_LEAF': 1,
            'STATUS1': 0, 'RECORD_TYPE': 1, 'ORG_BELONG': 0}

    db.clear(table_name)
    db.insert(table_name, data)
    db.close()
'''
