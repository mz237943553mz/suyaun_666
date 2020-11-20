import unittest
from HTMLTestRunnerNew import HTMLTestRunner
import time
class run():
    def get_allcase(self):
        test_dir=r"./"
        discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
        return discover

if __name__ == '__main__':
    a=run()
    b=a.get_allcase()
    runner=unittest.TextTestRunner()
    runner.run(b)

    # now = time.strftime("%Y-%m-%d-%H_%M_%S")
    # report_path = r'C:\Users\Administrator\PycharmProjects\产品溯源系统\report' + now + 'result.html'
    # f=open(report_path,'wb')
    # runner=HTMLTestRunner(stream=f,title="public",description="测试登录描述",tester="毛展")
    # runner.run(b)
