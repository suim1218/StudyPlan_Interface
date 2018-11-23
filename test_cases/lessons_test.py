import requests
import unittest
from nose_parameterized import parameterized
from test_cases.login import login_success
from utils.read_config import read_config


class MyLessonList(unittest.TestCase):

    def setUp(self):
        self.base_url = read_config().get('url')
        self.mobile = login_success().get('mobile')
        self.password = login_success().get('password')
        self.token = login_success().get('token')
        self.session = requests.Session()
        """
        课程顺序:
        aa列表页第一个课程
        aa列表页第二个课程
        打回笔记测试
        测试课程6
        测试课程5
        测试课程4
        测试课程3
        测试课程2
        精选笔记测试
        优秀笔记测试
        第二页第一个课程
        """

    def tearDown(self):
        print("run after")

    def test_get_my_lessons_page_1(self):
        """获取我的课程列表页第一页数据"""
        self.relative_path = 'studypath/chatgroup/getStudyAll'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'offset': 1, 'limit': 10}
        self.result = self.session.get(self.url, params=payload).json()
        # 第一条数据
        self.assertEqual(self.result['data'][0].get("content"), 'aa列表页第一个课程')
        self.assertEqual(self.result['data'][0].get("createTime"), '2018-11-23 13:46')
        self.assertEqual(self.result['data'][0].get("title"), '列表页第一个课程')
        # 第10条数据
        self.assertEqual(self.result['data'][9].get("content"), 'aa优秀笔记测试')
        self.assertEqual(self.result['data'][9].get("createTime"), '2018-11-23 13:40')
        self.assertEqual(self.result['data'][9].get("title"), '优秀笔记测试')
        # 断言是否为10条数据
        self.assertEqual(len(self.result['data']), 10)
        self.assertEqual(self.result['status'], 1)

    def test_get_my_lessons_page_2(self):
        """获取我的课程列表页第二页数据"""
        self.relative_path = 'studypath/chatgroup/getStudyAll'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'offset': 2, 'limit': 10}
        self.result = self.session.get(self.url, params=payload).json()
        # 第一条数据
        self.assertEqual(self.result['data'][0].get("content"), 'aa急急急急急急急急急')
        self.assertEqual(self.result['data'][0].get("createTime"), '2018-11-23 13:37')
        self.assertEqual(self.result['data'][0].get("title"), '第二页第一个课程')
        # status 0:未提交　1:正常提交  2:延时　３:驳回
        # self.assertEqual(self.result['data'][0].get("status"), 1)
        self.assertEqual(self.result['status'], 1)

    def test_excellent_note(self):
        """优秀笔记展示优秀笔记标签"""
        self.relative_path = 'studypath/chatgroup/getStudyAll'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'offset': 1, 'limit': 10}
        self.result = self.session.get(self.url, params=payload).json()

        self.assertEqual(self.result['data'][9].get("content"), 'aa优秀笔记测试')
        self.assertEqual(self.result['data'][9].get("createTime"), '2018-11-23 13:40')
        self.assertEqual(self.result['data'][9].get("title"), '优秀笔记测试')
        # excellent 0:正常笔记 1:优秀笔记
        self.assertEqual(self.result['data'][9].get("excellent"), '1')
        # status 0:未提交　1:正常提交  2:延时　３:驳回
        self.assertEqual(self.result['data'][9].get("status"), 1)
        self.assertEqual(self.result['status'], 1)

    def test_selected_note(self):
        """精选笔记展示精选笔记标签"""
        self.relative_path = 'studypath/chatgroup/getStudyAll'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'offset': 1, 'limit': 10}
        self.result = self.session.get(self.url, params=payload).json()

        self.assertEqual(self.result['data'][8].get("content"), 'aa精选笔记测试')
        self.assertEqual(self.result['data'][8].get("createTime"), '2018-11-23 13:40')
        self.assertEqual(self.result['data'][8].get("title"), '精选笔记测试')
        # selected 0:正常笔记　1:精选笔记
        self.assertEqual(self.result['data'][8].get("selected"), '1')
        # status 0:未提交　1:正常提交  2:延时　３:驳回
        self.assertEqual(self.result['data'][8].get("status"), 1)
        self.assertEqual(self.result['status'], 1)

    def test_not_submitted_note(self):
        """未提交笔记显示未提交标签"""
        self.relative_path = 'studypath/chatgroup/getStudyAll'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'offset': 1, 'limit': 10}
        self.result = self.session.get(self.url, params=payload).json()

        self.assertEqual(self.result['data'][0].get("content"), 'aa列表页第一个课程')
        self.assertEqual(self.result['data'][0].get("createTime"), '2018-11-23 13:46')
        self.assertEqual(self.result['data'][0].get("title"), '列表页第一个课程')
        # selected 0:正常笔记　1:精选笔记
        self.assertEqual(self.result['data'][0].get("selected"), '0')
        # status 0:未提交　1:正常提交  2:延时　３:驳回
        self.assertEqual(self.result['data'][0].get("status"), 0)
        self.assertEqual(self.result['status'], 1)

    def test_repulse_note(self):
        """打回笔记显示打回标签"""
        self.relative_path = 'studypath/chatgroup/getStudyAll'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'offset': 1, 'limit': 10}
        self.result = self.session.get(self.url, params=payload).json()

        self.assertEqual(self.result['data'][2].get("content"), 'aa打回笔记测试')
        self.assertEqual(self.result['data'][2].get("createTime"), '2018-11-23 13:40')
        self.assertEqual(self.result['data'][2].get("title"), '打回笔记测试')
        # selected 0:正常笔记　1:精选笔记
        self.assertEqual(self.result['data'][2].get("selected"), '0')
        # status 0:未提交　1:正常提交  2:延时　３:驳回
        self.assertEqual(self.result['data'][2].get("status"), 3)
        self.assertEqual(self.result['status'], 1)

    def test_lesson_details(self):
        """课程详情"""
        self.relative_path = 'studypath/chatgroup/getGroupStudyDetails'
        self.url = self.base_url + self.relative_path
        self.group_id = '3d5e4d66eee211e88fc6754dfbc82320'  # 课程id
        payload = {'mobile': self.mobile, 'token': self.token, 'groupId': self.group_id}
        self.result = self.session.get(self.url, params=payload).json()
        # 断言作者名称 标题 内容 创建时间
        self.assertEqual(self.result['data'].get("authName"), 'wangyg1')
        self.assertEqual(self.result['data'].get("content"), 'aa优秀笔记测试')
        self.assertEqual(self.result['data'].get("title"), '优秀笔记测试')
        self.assertEqual(self.result['data'].get("createTime"), '2018-11-23 13:40:09')
        self.assertEqual(self.result['status'], 1)

    def test_my_note_details(self):
        """课程详情我的笔记详情"""
        self.relative_path = 'studypath/chatgroup/noteDetails'
        self.url = self.base_url + self.relative_path
        self.group_id = '3d5e4d66eee211e88fc6754dfbc82320'  # 课程id
        payload = {'mobile': self.mobile, 'token': self.token, 'groupId': self.group_id}
        self.result = self.session.get(self.url, params=payload).json()
        # 断言标题 内容 创建时间 是否有优秀笔记
        self.assertEqual(self.result['data'].get("excellent"), '1')
        self.assertEqual(self.result['data'].get("content"),
                         '真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记')
        self.assertEqual(self.result['data'].get("title"), '真的是优秀笔记')
        self.assertEqual(self.result['data'].get("submitDate"), '2018-11-23 14:01:48')
        self.assertEqual(self.result['status'], 1)

    def test_excellent_note_details(self):
        """课程详情优秀笔记详情"""
        self.relative_path = 'studypath/chatgroup/excellentNotes'
        self.url = self.base_url + self.relative_path
        self.group_id = '3d5e4d66eee211e88fc6754dfbc82320'  # 课程id
        payload = {'mobile': self.mobile, 'token': self.token, 'groupId': self.group_id, 'offset': 1, 'limit': 10}
        self.result = self.session.post(self.url, payload).json()
        # 断言标题 内容 评优时间 是否有优秀笔记 作者 组织
        self.assertEqual(self.result['data'][0].get("excellent"), '1')
        self.assertEqual(self.result['data'][0].get("content"),
                         '真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记')
        self.assertEqual(self.result['data'][0].get("title"), '真的是优秀笔记')
        self.assertEqual(self.result['data'][0].get("excellentTime"), '2018-11-23 14:02')
        self.assertEqual(self.result['data'][0].get("userName"), 'test1')
        self.assertEqual(self.result['data'][0].get("orgName"), '3U')
        self.assertEqual(self.result['status'], 1)


class SelectedLessonList(unittest.TestCase):

    def setUp(self):
        self.base_url = read_config().get('url')
        self.mobile = login_success().get('mobile')
        self.password = login_success().get('password')
        self.token = login_success().get('token')
        self.session = requests.Session()
        """
        课程顺序:
        aa列表页第一个课程
        aa列表页第二个课程
        打回笔记测试
        精选笔记测试
        优秀笔记测试
        测试课程6
        测试课程5
        测试课程4
        测试课程3
        测试课程2
        第二页第一个课程
        """

    def tearDown(self):
        print("run after")

    def test_get_selected_lessons_page_1(self):
        """获取精选课程列表页第一页数据"""
        self.relative_path = 'studypath/chatgroup/selectedGroups'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'offset': 1, 'limit': 10}
        self.result = self.session.post(self.url, payload).json()
        # 第一条数据
        self.assertEqual(self.result['data'][0].get("content"), 'aa列表页第一个课程')
        self.assertEqual(self.result['data'][0].get("createTime"), '2018-11-23 13:46')
        self.assertEqual(self.result['data'][0].get("title"), '列表页第一个课程')
        # 第10条数据
        self.assertEqual(self.result['data'][9].get("content"), 'aa测试课程2')
        self.assertEqual(self.result['data'][9].get("createTime"), '2018-11-23 13:38')
        self.assertEqual(self.result['data'][9].get("title"), '测试课程2')
        self.assertEqual(self.result['data'][9].get("authName"), 'wangyg1')
        # 断言是否为10条数据
        self.assertEqual(len(self.result['data']), 10)
        self.assertEqual(self.result['status'], 1)

    def test_get_selected_lessons_page_2(self):
        """获取精选课程列表页第二页数据"""
        self.relative_path = 'studypath/chatgroup/selectedGroups'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'offset': 2, 'limit': 10}
        self.result = self.session.post(self.url, payload).json()
        # 第一条数据
        self.assertEqual(self.result['data'][0].get("content"), 'aa急急急急急急急急急')
        self.assertEqual(self.result['data'][0].get("createTime"), '2018-11-23 13:37')
        self.assertEqual(self.result['data'][0].get("title"), '第二页第一个课程')
        self.assertEqual(self.result['data'][0].get("authName"), 'wangyg1')
        self.assertEqual(self.result['status'], 1)

    def test_selected_lessons_details(self):
        """精选课程详情"""
        self.relative_path = 'studypath/chatgroup/getStudySelectedDetails'
        self.url = self.base_url + self.relative_path
        self.group_id = '3d5e4d66eee211e88fc6754dfbc82320'  # 课程id
        payload = {'mobile': self.mobile, 'token': self.token, 'groupId': self.group_id}
        self.result = self.session.post(self.url, payload).json()
        # 断言作者名称 标题 内容 创建时间
        self.assertEqual(self.result['data'].get("authName"), 'wangyg1')
        self.assertEqual(self.result['data'].get("content"), 'aa优秀笔记测试')
        self.assertEqual(self.result['data'].get("title"), '优秀笔记测试')
        self.assertEqual(self.result['data'].get("createTime"), '2018-11-23 13:40')
        self.assertEqual(self.result['status'], 1)

    def test_excellent_note_details(self):
        """精选课程详情优秀笔记详情"""
        self.relative_path = 'studypath/chatgroup/excellentNotes'
        self.url = self.base_url + self.relative_path
        self.group_id = '3d5e4d66eee211e88fc6754dfbc82320'  # 课程id
        payload = {'mobile': self.mobile, 'token': self.token, 'groupId': self.group_id, 'offset': 1, 'limit': 10}
        self.result = self.session.post(self.url, payload).json()
        # 断言标题 内容 评优时间 是否有优秀笔记 作者 组织
        self.assertEqual(self.result['data'][0].get("excellent"), '1')
        self.assertEqual(self.result['data'][0].get("content"),
                         '真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记真的是优秀笔记')
        self.assertEqual(self.result['data'][0].get("title"), '真的是优秀笔记')
        self.assertEqual(self.result['data'][0].get("excellentTime"), '2018-11-23 14:02')
        self.assertEqual(self.result['data'][0].get("userName"), 'test1')
        self.assertEqual(self.result['data'][0].get("orgName"), '3U')
        self.assertEqual(self.result['status'], 1)


class SelectedNoteList(unittest.TestCase):

    def setUp(self):
        self.base_url = read_config().get('url')
        self.mobile = login_success().get('mobile')
        self.password = login_success().get('password')
        self.token = login_success().get('token')
        self.session = requests.Session()

    def tearDown(self):
        print("run after")

    def test_get_selected_note(self):
        """获取精选笔记列表页第一页数据"""
        self.relative_path = 'studypath/chatgroup/selectedNotes'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'offset': 1, 'limit': 10}
        self.result = self.session.post(self.url, payload).json()
        # 断言 笔记编写人 所属组织 推荐时间 推荐人 课程标题 笔记内容
        self.assertEqual(self.result['data'][0].get("userName"), 'test1')
        self.assertEqual(self.result['data'][0].get("orgName"), '3U')
        self.assertEqual(self.result['data'][0].get("selectedTime"), '2018-11-23 14:02')
        self.assertEqual(self.result['data'][0].get("authName"), 'wangyg1')
        self.assertEqual(self.result['data'][0].get("title"), '精选笔记测试')
        self.assertEqual(self.result['data'][0].get("content"),
                         '真的是精选笔记真的是精选笔记真的是精选笔记真的是精选笔记真的是精选笔记真的是精选笔记真的是精选笔记真的是精选笔记真的'
                         '是精选笔记真的是精选笔记真的是精选笔记真的是精选笔记真的是精选笔记')
        self.assertEqual(self.result['status'], 1)

    def test_get_selected_note_details(self):
        """获取精选笔记详情"""
        self.relative_path = 'studypath/chatgroup/selectedNoteDetails'
        self.url = self.base_url + self.relative_path
        self.group_id = '4afd3da7eee211e88fc6fd420ff088db'
        payload = {'mobile': self.mobile, 'token': self.token, 'groupId': self.group_id, 'studentMobile': self.mobile}
        self.result = self.session.post(self.url, payload).json()
        # 断言 笔记编写人 所属组织 推荐时间 推荐人 笔记标题 笔记内容
        self.assertEqual(self.result['data'].get("userName"), 'test1')
        self.assertEqual(self.result['data'].get("orgName"), '3U')
        self.assertEqual(self.result['data'].get("selectedTime"), '2018-11-23 14:02')
        self.assertEqual(self.result['data'].get("authName"), 'wangyg1')
        self.assertEqual(self.result['data'].get("noteTitle"), '真的是精选笔记')
        self.assertEqual(self.result['data'].get("content"),
                         '真的是精选笔记真的是精选笔记真的是精选笔记真的是精选笔记真的是精选笔记真的是精选笔记真的是精选笔记真的是精选笔记真的'
                         '是精选笔记真的是精选笔记真的是精选笔记真的是精选笔记真的是精选笔记')
        self.assertEqual(self.result['status'], 1)


if __name__ == '__main__':
    unittest.main()
    # 构造测试集
    # suite = unittest.TestSuite()
    # suite.addTest(ThematicEducationTest("test_get_first_detail"))
    # # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
