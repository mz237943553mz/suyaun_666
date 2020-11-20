# create time:2010-10-30

from selenium import webdriver
import unittest
import time
from HTMLTestRunnerNew import HTMLTestRunner
from ddt import ddt,data,unpack
from mz.lianxi.datatest import getdata
bb=getdata.Excel1(r"C:\Users\Administrator\Desktop\QQ-Login.xlsx")
cc=bb.login_data()
@ddt()
class Test_Baidu(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.get("https://mail.qq.com/")
        self.driver.implicitly_wait(5)

    # def test_baidu01(self):
    #     self.driver.find_element_by_id("kw").send_keys("QQ邮箱")
    #     self.driver.find_element_by_id("su").click()
    #     time.sleep(3)

    # def test_baidu02(self):
    #     self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[3]/div[1]/h3/a[1]").click()
    #     time.sleep(5)
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #     a=self.driver.title
    #     b="登录QQ邮箱"
    #     self.assertEqual(a,b,msg="没有找到QQ邮箱登录页面")
    #     time.sleep(3)

    # @unittest.skip("不需要")
    # def test_baidu03(self):
    #     time.sleep(3)
    #     self.driver.find_element_by_id("kw").send_keys("韩立")
    #     self.driver.find_element_by_id("su").click()
    #     time.sleep(3)

    # def test_baidu01(self):
    #     time.sleep(3)
    #     self.driver.switch_to.frame("login_frame")
    #     self.driver.find_element_by_css_selector(".inputstyle").send_keys("2379435531")
    #     self.driver.find_element_by_css_selector(".inputstyle.password").send_keys("maozhan2379435@!")
    #     self.driver.find_element_by_css_selector("#login_button").click()
    #     self.driver.switch_to.default_content()
    #     time.sleep(5)
    #
    # def test_baidu02(self):
    #     time.sleep(3)
    #     self.driver.switch_to.frame("login_frame")
    #     self.driver.find_element_by_css_selector(".inputstyle").send_keys("237943553")
    #     self.driver.find_element_by_css_selector(".inputstyle.password").send_keys("1maozhan2379435@!")
    #     self.driver.find_element_by_css_selector("#login_button").click()
    #     self.driver.switch_to.default_content()
    #     time.sleep(5)
    #
    # def test_baidu03(self):
    #     time.sleep(3)
    #     self.driver.switch_to.frame("login_frame")
    #     self.driver.find_element_by_css_selector(".inputstyle").send_keys("1237943553")
    #     self.driver.find_element_by_css_selector(".inputstyle.password").send_keys("!maozhan2379435@!")
    #     self.driver.find_element_by_css_selector("#login_button").click()
    #     self.driver.switch_to.default_content()
    #     time.sleep(5)
    #
    #
    # def test_baidu04(self):
    #     time.sleep(3)
    #     self.driver.switch_to.frame("login_frame")
    #     self.driver.find_element_by_css_selector(".inputstyle").send_keys(" ")
    #     self.driver.find_element_by_css_selector(".inputstyle.password").send_keys(" ")
    #     self.driver.find_element_by_css_selector("#login_button").click()
    #     self.driver.switch_to.default_content()
    #     time.sleep(5)

    @data(*cc)
    @unpack
    def test_baidu05(self,name,pwd):
        time.sleep(3)
        self.driver.switch_to.frame("login_frame")
        self.driver.find_element_by_css_selector(".inputstyle").send_keys("237943553")
        self.driver.find_element_by_css_selector(".inputstyle.password").send_keys("maozhan2379435@!")
        self.driver.find_element_by_css_selector("#login_button").click()
        self.driver.switch_to.default_content()
        time.sleep(5)
        # self.driver.switch_to.window(self.driver.window_handles[-1])
        try:
            c=self.driver.title
            d="QQ邮箱"
            self.assertEqual(c,d,"没有成功登录扣扣邮箱")
        except Exception as e:
            print("异常为：",e)
            time.sleep(3)

    # def test_baidu06(self):
    #     self.driver.find_element_by_css_selector("[id='composebtn'][target='mainFrame']").click()
    #     time.sleep(3)
    #     self.driver.find_element_by_css_selector("body").send_keys("笑口常开")
    #     self.driver.switch_to.frame("mainFrame")
    #     self.driver.find_element_by_css_selector("#toAreaCtrl > div:nth-child(2) > input:nth-child(1)").send_keys(
    #         "328649501")
    #     time.sleep(3)
    #     self.driver.find_element_by_id("subject").send_keys("你好吗？")
    #     time.sleep(3)
    #     self.driver.find_element_by_css_selector(".btn_gray.btn_space").click()
    #     time.sleep(3)
    #     self.driver.switch_to.default_content()


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    suite=unittest.TestSuite()
    # suite.addTest(Test_Baidu('test_baidu01'))
    # suite.addTest(Test_Baidu('test_baidu02'))
    # suite.addTest(Test_Baidu('test_baidu04'))
    suite.addTest(Test_Baidu('test_baidu05'))
    # suite.addTest(Test_Baidu('test_baidu06'))
    runner=unittest.TextTestRunner()
    runner.run(suite)
    # path1=r'C:\Users\Administrator\PycharmProjects\mz\lianxi\report\dengl.html'
    # f=open(path1,'wb')
    # runner=HTMLTestRunner(stream=f,title="ceshibaogao",description="测试描述",tester="毛展")
    # runner.run(suite)



