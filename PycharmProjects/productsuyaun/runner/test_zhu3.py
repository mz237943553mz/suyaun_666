import unittest
from productsuyaun.testcase import test_03
from productsuyaun.public import login1
# from ddt import ddt,data,unpack
# from 产品溯源系统.data import getdata
# from selenium import webdriver
import time

xzlb3 = test_03.XZCP3()

denglu=login1.Test_Denglu()

class Test_size(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) :
    #     denglu.Denglu()
    #
    @classmethod
    def tearDownClass(cls):
        denglu.driver.quit()

    def test_xzlb_31(self):
        xzlb3.sygl()

    def test_xzlb_32(self):
        xzlb3.sygl_FAN1()

    def test_xzlb_33(self):
        xzlb3.sygl_FAN2()

    def test_xzlb_34(self):
        xzlb3.sygl1()

    def test_xzlb_35(self):
       xzlb3.sygl1_FAN1()

    def test_xzlb_36(self):
        xzlb3.sygl1_FAN2()

    def test_xzlb_37(self):
        xzlb3.sygl_del_all()

    def test_xzlb_38(self):
        xzlb3.sygl_del_one()

    def test_xzlb_39(self):
        xzlb3.sygl_ck()

    def test_xzlb_40(self):
       xzlb3.plsycz_wlm()

    def test_xzlb_41(self):
        xzlb3.plsycz_FAN1()

    def test_xzlb_42(self):
        xzlb3.plsycz_FAN2()

    def test_xzlb_43(self):
        xzlb3.plsycz_ID()

    def test_xzlb_44(self):
       xzlb3.plsycz_ID_FAN()

    def test_xzlb_45(self):
        xzlb3.plsycz_pc()

    def test_xzlb_46(self):
        xzlb3.plsycz_cpm()

    def test_xzlb_47(self):
        xzlb3.plsycz_date()

    def test_xzlb_48(self):
        xzlb3.syczjl()

    def test_xzlb_49(self):
        xzlb3.syczjl_FAN1()

    def test_xzlb_50(self):
        xzlb3.syczjl_FAN2()

    def test_xzlb_51(self):
        xzlb3.syczjl_def_all()

    def test_xzlb_52(self):
       xzlb3.syczjl_def_one()
