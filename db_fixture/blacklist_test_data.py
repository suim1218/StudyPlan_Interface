import sys
import time
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

'''
# create data
datas = {
    #黑名单表
    'bg_internet_control':[
        {'IC_ID': '8f912bb0d34111e7adfb330c633a347a', 'IC_NAME': '百度', 'IC_URL': 'www.baidu.com',
         'IC_TYPE': '2', 'IS_DELETE': '0', 'IC_SEND_TYPE': '1', 'STATUS1': '0'},

    ],
}


# Inster table datas
def init_data():
    DB().init_data(datas)


if __name__ == '__main__':
    init_data()
'''
