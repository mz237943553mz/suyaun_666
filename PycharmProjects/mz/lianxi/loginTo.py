'''
项目名称:产品溯源系统
所属模块:登录
日期:2020/10/30
作者:李锦龙
版本:version:1.0
'''
import time
from selenium import webdriver
import unittest
from ddt import ddt,data,unpack
from HTMLTestRunnerNew import HTMLTestRunner
from data.testdata import getdata

ll = getdata.GetData("D:\\pycharm\\产品溯源系统测试\\data\\testdata\\data.xlsx")
ms = ll.login_data()
print(ms)
@ddt
class LoginTo(unittest.TestCase):



	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.get("http://123.57.140.190/manage/")
		self.driver.maximize_window()
		self.driver.implicitly_wait(5)

	def tearDown(self):
		self.driver.quit()

	@data(*ms)
	@unpack
	def test_dl_01(self,name,pwd):
		self.driver.find_element_by_xpath("//input[@placeholder='管理员帐号']").send_keys(name)
		self.driver.find_element_by_xpath("//input[@type='password']").send_keys(pwd)
		self.driver.find_element_by_css_selector(".btn").click()
		time.sleep(2)
		try:
			x = self.driver.find_element_by_xpath("(//a[@class='dcjq-parent']//span)[1]").text
			y = "产品管理"
			self.assertEqual(x, y, msg="登录失败！")
		except Exception as a:
			print(a)

if __name__ == '__main__':
    unittest.main()