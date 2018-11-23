import requests
import unittest
from nose_parameterized import parameterized

from utils.read_config import read_config


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.base_url = read_config().get('url')
        self.relative_path = 'studypath/userinfo/login'
        self.url = self.base_url + self.relative_path
        self.session = requests.Session()
        self.mobile = read_config().get('mobile')
        self.password = read_config().get('mobile_password')
        self.is_Test = 0

    def tearDown(self):
        print("run after")

    @parameterized.expand([
        ('mobile_error', '1331234000', 1, '账号或密码错误，请重新输入'),
        ('mobile_error', '133123400011', 1, '账号或密码错误，请重新输入'),
        ('mobile_error', '13312 340001', 1, '账号或密码错误，请重新输入'),
        ('mobile_error', ' 13312340001', 1, '账号或密码错误，请重新输入'),
        ('mobile_error', 'abc', 1, '账号或密码错误，请重新输入'),
        ('mobile_error', '1331234000.', 1, '账号或密码错误，请重新输入'),

    ])
    def test_mobile_error(self, _, phone, status, message):
        """手机号错误"""
        payload = {'mobile': phone, 'pwd': self.password, 'isTest': self.is_Test}
        self.result = self.session.post(self.url, payload).json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['error'], message)

    @parameterized.expand([
        ('password_error', '11111', 1, '账号或密码错误，请重新输入'),
        ('password_error', '1111111111111111111111111', 1, '账号或密码错误，请重新输入'),
        ('password_error', '111 111', 1, '账号或密码错误，请重新输入'),
        ('password_error', ' 111111', 1, '账号或密码错误，请重新输入'),

    ])
    def test_password_error(self, _, password, status, message):
        """密码错误"""
        payload = {'mobile': self.mobile, 'pwd': password, 'isTest': self.is_Test}
        self.result = self.session.post(self.url, payload).json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['error'], message)

    def test_login_success(self):
        """登录成功"""
        payload = {'mobile': self.mobile, 'pwd': self.password, 'isTest': self.is_Test}
        self.result = self.session.post(self.url, payload).json()
        self.assertEqual(self.result['status'], 0)


if __name__ == '__main__':
    unittest.main()
