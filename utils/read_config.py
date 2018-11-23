import pymysql.cursors
import os
import configparser as cparser


# ======== Reading config.ini setting ===========
def read_config():
    base_dir = str(os.path.dirname(os.path.dirname(__file__)))
    base_dir = base_dir.replace('\\', '/')
    # print(base_dir)

    file_path = base_dir + "/config.ini"

    cf = cparser.ConfigParser()

    cf.read(file_path)
    url = cf.get("mysqlconf", "url")
    host = cf.get("mysqlconf", "host")
    port = cf.get("mysqlconf", "port")
    db = cf.get("mysqlconf", "db_name")
    user = cf.get("mysqlconf", "user")
    password = cf.get("mysqlconf", "password")
    mobile = cf.get("mysqlconf", "mobile")
    mobile_password = cf.get("mysqlconf", "mobile_password")
    config_data = {'url': url, 'host': host, 'port': port, 'db': db, 'user': user, 'password': password,
                   'mobile': mobile, 'mobile_password': mobile_password}

    return config_data
    # print(config_data)


# print(read_config().get('url'))
