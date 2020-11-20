import unittest
from productsuyaun.testcase import test_02
# from 产品溯源系统.public import login1
# from ddt import ddt,data,unpack
# from 产品溯源系统.data import getdata
# from selenium import webdriver
import time

xzlb2 = test_02.XZCP2()

# denglu=login1.Test_Denglu()

class Test_size(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) :
    #     denglu.Denglu()

    # @classmethod
    # def tearDownClass(cls):
    #     denglu.driver.quit()

    def test_xzlb_15(self):
        xzlb2.xzlcleb()

    def test_xzlb_16(self):
        xzlb2.xzlcl_FAN()

    def test_xzlb_17(self):
        xzlb2.lclbgl()

    def test_xzlb_18(self):
        xzlb2.lclbgl_FAN1()

    def test_xzlb_19(self):
        xzlb2.lclbgl_FAN2()

    def test_xzlb_20(self):
        xzlb2.lclbgl_fxk_all()

    def test_xzlb_21(self):
        xzlb2.lclbgl_fxk_one()

    def test_xzlb_22(self):
        xzlb2.lcjlgl_dellclbgl_bj()

    def test_xzlb_23(self):
        xzlb2.lrlcjl_FAN_WLM()

    def test_xzlb_24(self):
        xzlb2.lrlcjl_FAN_time()

    def test_xzlb_25(self):
        xzlb2.lcjlgl()

    def test_xzlb_26(self):
        xzlb2.lcjlgl_FAN1()

    def test_xzlb_27(self):
        xzlb2.lcjlgl_FAN2()

    def test_xzlb_28(self):
        xzlb2.lcjlgl_del()

    def test_xzlb_29(self):
        xzlb2.lcjlgl_del_one()

    def test_xzlb_30(self):
        xzlb2.lcjlgl_del_bj()

