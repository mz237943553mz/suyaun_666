'''
项目名称:产品溯源系统
所属模块:登录
日期:2020/11/04
作者:毛展
版本:version:1.0
'''
from selenium import webdriver
import time

class Test_Denglu():
    driver = webdriver.Firefox()
    def Denglu(self):
        self.driver.get(r"http://123.57.140.190/manage/index.php")
        self.driver.implicitly_wait(2)
        self.driver.find_element_by_css_selector("input.form-control:nth-child(1)").send_keys("admin")
        self.driver.find_element_by_css_selector("input.form-control:nth-child(2)").send_keys("admin999")
        self.driver.find_element_by_css_selector(".btn").click()
        time.sleep(0.5)
a=Test_Denglu()
a.Denglu()

