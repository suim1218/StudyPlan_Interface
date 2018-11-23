import requests
import unittest
from nose_parameterized import parameterized

from utils.read_config import read_config


def login_success():
    base_url = read_config().get('url')
    session = requests.Session()
    mobile = read_config().get('mobile')
    password = read_config().get('mobile_password')
    relative_path = 'studypath/userinfo/login'
    url = base_url + relative_path
    is_Test = 0
    payload = {'mobile': mobile, 'pwd': password, 'isTest': is_Test}
    result = session.post(url, payload).json()
    config_data = {'mobile': mobile, 'password': password, 'token': result['data']['token']}
    return config_data

# print(login_success())
