import requests
import unittest
from nose_parameterized import parameterized
from interface.login import login_success
from utils.read_config import read_config


class ThematicEducationTest(unittest.TestCase):

    def setUp(self):
        self.base_url = read_config().get('url')
        self.mobile = login_success().get('mobile')
        self.password = login_success().get('password')
        self.token = login_success().get('token')
        self.session = requests.Session()
        self.column_id_1 = '4bd2df847e7e11e88536436658d7fe9f'  # 媒体上的3U
        self.column_id_2 = '65acf33078e411e89bb28bb681c11dc5'  # 权威解读
        self.column_id_3 = '5bbadf4f78e411e89bb239f8d1ad2a7b'  # 指示要求
        self.column_id_4 = '53cd9b1e78e411e89bb2538e3b767b5f'  # 强军思想
        self.column_id_5 = '32c4db7367ba11e8a00c3335a8521e17'  # 红色记忆
        self.column_id_6 = '2d6c72f267ba11e8a00cb50fa196d5e9'  # 体会展评
        self.column_id_7 = '28468c2167ba11e8a00c93c0b789c0b8'  # 教育动态
        self.column_id_8 = '23e3591067ba11e8a00ccf13631110e2'  # 辅导材料

    def tearDown(self):
        print("run after")

    def test_get_all_col(self):
        """获取所有栏目"""
        self.relative_path = 'studypath/column/getAllCol'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token}
        self.result = self.session.post(self.url, payload).json()
        # print(self.result['data'][0].get("columnName"))
        self.assertEqual(self.result['data'][0].get("columnName"), '媒体上的3U')
        self.assertEqual(self.result['data'][1].get("columnName"), '权威解读')
        self.assertEqual(self.result['data'][2].get("columnName"), '指示要求')
        self.assertEqual(self.result['data'][3].get("columnName"), '强军思想')
        self.assertEqual(self.result['data'][4].get("columnName"), '红色记忆')
        self.assertEqual(self.result['data'][5].get("columnName"), '体会展评')
        self.assertEqual(self.result['data'][6].get("columnName"), '教育动态')
        self.assertEqual(self.result['data'][7].get("columnName"), '辅导材料')
        self.assertEqual(self.result['status'], 0)

    def assert_abstar_column_id_create_time_title(self, abstra, column_id, create_time, title):
        self.assertEqual(self.result['data'][0].get("abstra"), abstra)
        self.assertEqual(self.result['data'][0].get("columnId"), column_id)
        self.assertEqual(self.result['data'][0].get("createTime"), create_time)
        self.assertEqual(self.result['data'][0].get("title"), title)
        self.assertEqual(self.result['status'], 0)

    def test_get_1_list_page_1(self):
        """获取媒体上的3U第一页数据"""
        self.relative_path = 'studypath/article/selectAllArt'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'columnId': self.column_id_1, 'offset': 1, 'limit': 10}
        self.result = self.session.post(self.url, payload).json()
        # 第一条数据
        self.assert_abstar_column_id_create_time_title('北岛现在诗', self.column_id_1, '2018-11-23 11:46', '回答')

        # 第十条数据
        self.assertEqual(self.result['data'][9].get("abstra"), '枕戈观澜')
        self.assertEqual(self.result['data'][9].get("columnId"), self.column_id_1)
        self.assertEqual(self.result['data'][9].get("createTime"), '2018-07-03 19:56')
        self.assertEqual(self.result['data'][9].get("title"), '现实中中国军人会为救别人而牺牲自己吗？答案来了...')

    def test_get_1_list_page_2(self):
        """获取媒体上的3U第二页数据"""
        self.relative_path = 'studypath/article/selectAllArt'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'columnId': self.column_id_1, 'offset': 2, 'limit': 10}
        self.result = self.session.post(self.url, payload).json()
        # 第二页数据
        self.assert_abstar_column_id_create_time_title('冲锋号', self.column_id_1, '2018-07-03 19:50',
                                                       '班长你想套路我？根本不可能')

    def test_get_first_detail(self):
        """获取媒体上的3U第一篇详情"""
        self.relative_path = 'studypath/article/selectDetails'
        self.url = self.base_url + self.relative_path
        self.article_id = '5ebdf41ceed211e88fc6e5ca481aab27'
        payload = {'articleId': self.article_id}
        self.result = self.session.post(self.url, payload).json()
        # print(self.result['data'])
        self.assertEqual(self.result['data'].get("abstra"), '北岛现在诗')
        self.assertEqual(self.result['data'].get("articleId"), self.article_id)
        self.assertEqual(self.result['data'].get("createTime"), '2018-11-23 11:46')
        self.assertEqual(self.result['data'].get("title"), '回答')
        self.assertIn('卑鄙是卑鄙者的通行证', self.result['data'].get("content"))

    def test_get_2_list(self):
        """获取权威解读第一页数据"""
        self.relative_path = 'studypath/article/selectAllArt'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'columnId': self.column_id_2, 'offset': 1, 'limit': 10}
        self.result = self.session.post(self.url, payload).json()
        # 第一条数据
        self.assert_abstar_column_id_create_time_title('做红色传人 建强军新功', self.column_id_2, '2018-07-04 15:51',
                                                       '做红色传人 建强军新功')

    def test_get_3_list(self):
        """获取指示要求第一页数据"""
        self.relative_path = 'studypath/article/selectAllArt'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'columnId': self.column_id_3, 'offset': 1, 'limit': 10}
        self.result = self.session.post(self.url, payload).json()
        # 第一条数据
        self.assert_abstar_column_id_create_time_title('展“传承红色基因担当强军重任”主题教育的意见', self.column_id_3, '2018-07-04 22:40',
                                                       '开展“传承红色基因担当强军重任”主题教育的意见')

    def test_get_4_list(self):
        """获取强军思想第一页数据"""
        self.relative_path = 'studypath/article/selectAllArt'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'columnId': self.column_id_4, 'offset': 1, 'limit': 10}
        self.result = self.session.post(self.url, payload).json()
        # 第一条数据
        self.assert_abstar_column_id_create_time_title('习近平：大抓实战化军事训练 聚力打造精锐作战力量', self.column_id_4, '2018-07-04 11:05',
                                                       '习近平：大抓实战化军事训练 聚力打造精锐作战力量')

    def test_get_5_list(self):
        """获取红色记忆第一页数据"""
        self.relative_path = 'studypath/article/selectAllArt'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'columnId': self.column_id_5, 'offset': 1, 'limit': 10}
        self.result = self.session.post(self.url, payload).json()
        # 第一条数据
        self.assert_abstar_column_id_create_time_title('习主席领航的强军兴军新征程，取得了哪些突破性成果？', self.column_id_5,
                                                       '2018-07-05 08:47',
                                                       '习主席领航的强军兴军新征程，取得了哪些突破性成果？')

    def test_get_6_list(self):
        """获取体会展评第一页数据"""
        self.relative_path = 'studypath/article/selectAllArt'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'columnId': self.column_id_6, 'offset': 1, 'limit': 10}
        self.result = self.session.post(self.url, payload).json()
        # 第一条数据
        self.assert_abstar_column_id_create_time_title('枕戈观澜', self.column_id_6,
                                                       '2018-07-03 19:44',
                                                       '这是什么训练？搞得兵哥哥情商智商全得亮灯！')

    def test_get_7_list(self):
        """获取教育动态第一页数据"""
        self.relative_path = 'studypath/article/selectAllArt'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'columnId': self.column_id_7, 'offset': 1, 'limit': 10}
        self.result = self.session.post(self.url, payload).json()
        # 第一条数据
        self.assert_abstar_column_id_create_time_title('“传承红色基因 担当强军重任”主题教育理论抽考', self.column_id_7,
                                                       '2018-07-05 15:51',
                                                       '“传承红色基因 担当强军重任”主题教育理论抽考')

    def test_get_8_list(self):
        """获取辅导材料第一页数据"""
        self.relative_path = 'studypath/article/selectAllArt'
        self.url = self.base_url + self.relative_path
        payload = {'mobile': self.mobile, 'token': self.token, 'columnId': self.column_id_8, 'offset': 1, 'limit': 10}
        self.result = self.session.post(self.url, payload).json()
        # 第一条数据
        self.assert_abstar_column_id_create_time_title('军营版《一出好戏》震撼来袭！官兵看了都说好', self.column_id_8,
                                                       '2018-08-15 22:11',
                                                       '【关注】军营版《一出好戏》震撼来袭！官兵看了都说好')


if __name__ == '__main__':
    # unittest.main()
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(ThematicEducationTest("test_get_first_detail"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
