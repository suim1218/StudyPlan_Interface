import time, sys
from HTMLTestRunner import HTMLTestRunner
import unittest
sys.path.append('./test_cases')
sys.path.append('./db_fixture')


# 指定测试用例为当前文件夹下的 test_cases 目录
test_dir = './test_cases'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='StudyPlan Interface Test Report',
                            description='Implementation Example with: ')
    runner.run(discover)
    fp.close()
