'''
项目名称:产品溯源系统
所属模块:登录
日期:2020/11/04
作者:毛展
版本:version:1.0
'''
import unittest
from productsuyaun.testcase import test_01
from productsuyaun.public import login1
# from ddt import ddt,data,unpack
# from 产品溯源系统.data import getdata
# from selenium import webdriver
import time


xzlb = test_01.XZCP()
denglu=login1.Test_Denglu()

# @ddt()
class Test_size(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        denglu.Denglu()
    #     pass
    # aa = getdata.Excel1(r"C:\Users\Administrator\PycharmProjects\产品溯源系统\data\admin01.xlsx",'name1')
    # bb = aa.login_data()
    # @data(*bb)
    # @unpack
    # def test_xzlb_01(self,name,pwd):
    #     denglu.Denglu(name, pwd)


        # a=cls.find_element_by_css_selector(".pull-right > li:nth-child(1) > a:nth-child(1) > img:nth-child(1)").text
        # cls.assertTrue(a,"没有登录成功")

    # @classmethod
    # def tearDownClass(cls):
    #     denglu.driver.quit()

    def test_01(self):
        xzlb.plscfwm()
        a=denglu.driver.find_element_by_css_selector(".layui-layer-ico")
        self.assertTrue(a,"年代初开")

    def test_xzlb_02(self):
        xzlb.plscfwm_FAN1()

    def test_xzlb_03(self):
        xzlb.dgscfwm()
    def test_xzlb_04(self):
       xzlb.dgscfwm_FAN1()
    def test_xzlb_05(self):
        xzlb.plxgfwm()
    def test_xzlb_06(self):
        xzlb.plxgfwm_FAN1()
    def test_xzlb_07(self):
        xzlb.plxgfwm_FAN2()
    def test_xzlb_08(self):
        xzlb.plxgfwm_ID()
    def test_xzlb_09(self):
       xzlb.plxgfwm_ID_FAN()

    def test_xzlb_10(self):
        xzlb.plxgfwm_pcpl()

    def test_xzlb_11(self):
       xzlb.plxgfwm_pl()

    def test_xzlb_12(self):
        xzlb.plxgfwm_date()

    def test_xzlb_13(self):
        xzlb.plscfwm1_pc()

    def test_xzlb_14(self):
        xzlb.plscfwm1_pl()
#
#
#
#
# if __name__ == '__main__':
#     unittest.main()
#
#
#























