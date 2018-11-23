import requests
import unittest
from nose_parameterized import parameterized
from interface.login import login_success
from utils.read_config import read_config


class PersonCenterTest(unittest.TestCase):

    def setUp(self):
        self.base_url = read_config().get('url')

        self.mobile = login_success().get('mobile')
        self.password = login_success().get('password')
        self.token = login_success().get('token')
        self.new_password = '111111'
        self.session = requests.Session()

    def tearDown(self):
        print("run after")

    @parameterized.expand([
        ('old_password_error', '11111', 1, '原密码错误，请重新输入'),
        ('old_password_error', ' 111111', 1, '原密码错误，请重新输入'),
        ('old_password_error', '1111 11', 1, '原密码错误，请重新输入'),
        ('old_password_error', '1111111', 1, '原密码错误，请重新输入'),
    ])
    def test_modify_password(self, _, old_password, status, message):
        self.relative_path = 'studypath/userinfo/changePwd'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'pwd': old_password, 'newpwd': self.new_password, 'token': self.token}
        self.result = self.session.post(self.url, payload).json()
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['error'], message)

    def test_modify_password_success(self):
        self.relative_path = 'studypath/userinfo/changePwd'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'pwd': self.password, 'newpwd': self.new_password, 'token': self.token}
        self.result = self.session.post(self.url, payload).json()
        self.assertEqual(self.result['status'], 0)

    def test_about_study_path(self):
        """从关于学习帮手返回个人中心页面"""
        self.relative_path = 'studypath/chatgroup/selectMessageCenter'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token}
        self.result = self.session.post(self.url, payload).json()
        self.assertEqual(self.result['status'], 1)
        self.assertEqual(self.result['count'], 0)


if __name__ == '__main__':
    # unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(PersonCenterTest("test_about_study_path"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
