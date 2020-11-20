import time
from productsuyaun.public import login1
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
DL=login1.Test_Denglu()

class XZCP2():

    def xzlcleb(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text("新增流程类别").click()
        DL.driver.find_element_by_xpath(
            "/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input").send_keys("6荒原帅苹果入库")
        time.sleep(3)
        DL.driver.find_element_by_css_selector(
            "div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys("1")
        time.sleep(3)
        DL.driver.find_element_by_id("zt").click()
        DL.driver.find_element_by_css_selector("option:nth-child(1)").click()
        DL.driver.find_element_by_css_selector(".btn").click()
        time.sleep(5)

    def xzlcl_FAN(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text("新增流程类别").click()
        DL.driver.find_element_by_xpath(
            "/html/body/section/section/section/div/div/section/div/form/div[1]/div[1]/input").send_keys("6荒原帅苹果入库")
        time.sleep(3)
        DL.driver.find_element_by_css_selector(
            "div.form-group:nth-child(2) > div:nth-child(2) > input:nth-child(1)").send_keys("1")
        time.sleep(3)
        DL.driver.find_element_by_id("zt").click()
        DL.driver.find_element_by_css_selector("option:nth-child(1)").click()
        DL.driver.find_element_by_css_selector(".btn").click()
        time.sleep(5)
        # try:
        #     c = DL.driver.find_element_by_class_name("layui-layer-content")
        #     d = "流程类别名有重复!"
        #     DL.driver.assertEqual(c, d, "输入有重复")
        # except Exception as e:
        #     print("异常为：", e)

    def lclbgl(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text("流程类别管理").click()
        time.sleep(3)
        DL.driver.find_element_by_name("lcname").send_keys("5荒原帅苹果入库")
        time.sleep(3)
        DL.driver.find_element_by_css_selector(".btn.btn-success").click()
        time.sleep(5)

    def lclbgl_FAN1(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text("流程类别管理").click()
        time.sleep(3)
        DL.driver.find_element_by_name("lcname").send_keys("吾本韩老魔")
        time.sleep(3)
        DL.driver.find_element_by_css_selector(".btn.btn-success").click()
        time.sleep(5)

    def lclbgl_FAN2(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text("流程类别管理").click()
        time.sleep(3)
        DL.driver.find_element_by_name("lcname").send_keys(" ")
        time.sleep(3)
        DL.driver.find_element_by_css_selector(".btn.btn-success").click()
        time.sleep(5)

    def lclbgl_fxk_all(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text("流程类别管理").click()
        time.sleep(5)
        DL.driver.find_element_by_id("chkAll").click()
        inputs = DL.driver.find_elements_by_tag_name("input")
        for input in inputs:
            if input.get_attribute("type") == "checkbox":
                input.click()
                time.sleep(5)
        DL.driver.find_element_by_id("del").click()
        time.sleep(5)
        alert1 = DL.driver.switch_to.alert
        time.sleep(5)
        alert1.accept()
        time.sleep(5)
        alert2 = DL.driver.switch_to.alert
        time.sleep(5)
        alert2.accept()
        time.sleep(5)

    def lclbgl_fxk_one(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text("流程类别管理").click()
        time.sleep(5)
        DL.driver.find_element_by_css_selector(
            ".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > span:nth-child(2)").click()
        time.sleep(5)
        DL.driver.find_element_by_class_name("layui-layer-btn0").click()
        time.sleep(5)

    def lcjlgl_dellclbgl_bj(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text("流程类别管理").click()
        time.sleep(5)
        DL.driver.find_element_by_css_selector(
            "[class='label label-success label-mini'][href='edit_lc.php?act=edit&id=4']").click()
        time.sleep(5)
        DL.driver.find_element_by_css_selector("div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)")
        DL.driver.find_element_by_css_selector(
            "div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)").clear()
        DL.driver.find_element_by_css_selector(
            "div.form-group:nth-child(3) > div:nth-child(2) > input:nth-child(1)").send_keys("2")
        time.sleep(2)
        DL.driver.find_element_by_id("zt").click()
        DL.driver.find_element_by_css_selector("option:nth-child(2)").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector(".btn.btn-danger").click()
        time.sleep(5)
        # try:
        #     a = DL.driver.find_element_by_link_text("更新成功！")
        #     b = "更新成功！"
        #     DL.driver.assertEqual(a, b, "更新不成功")
        # except Exception as e:
        #     print("异常为：", e)

    def lrlcjl_FAN_WLM(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text("录入流程记录").click()
        time.sleep(5)
        DL.driver.find_element_by_class_name("searchable-select-holder").click()
        DL.driver.find_element_by_css_selector("div.searchable-select-item:nth-child(1)").click()
        time.sleep(5)
        DL.driver.find_element_by_css_selector("textarea.form-control").send_keys("5335500")
        time.sleep(5)
        DL.driver.find_element_by_css_selector("div.col-sm-6:nth-child(2) > input:nth-child(1)").send_keys("黄元帅装箱追踪")
        time.sleep(5)
        DL.driver.find_element_by_css_selector("div.form-group:nth-child(5) > div:nth-child(2) > input:nth-child(1)")
        DL.driver.find_element_by_css_selector(
            "div.form-group:nth-child(5) > div:nth-child(2) > input:nth-child(1)").clear()
        DL.driver.find_element_by_css_selector(
            "div.form-group:nth-child(5) > div:nth-child(2) > input:nth-child(1)").send_keys("辉爷")
        DL.driver.find_element_by_css_selector("#czdate").click()
        DL.driver.find_element_by_id("laydate_today").click()
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".btn.btn-danger").click()
        time.sleep(5)
        # try:
        #     a = DL.driver.find_elements_by_xpath("/html/body/div[3]/div").text
        #     b = "物流码不存在"
        #     DL.driver.assertEqual(a, b, '定位不正确')
        # except Exception as e:
        #     print("异常为：", e)

    def lrlcjl_FAN_time(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_link_text("录入流程记录").click()
        time.sleep(5)
        DL.driver.find_element_by_class_name("searchable-select-holder").click()
        DL.driver.find_element_by_css_selector("div.searchable-select-item:nth-child(1)").click()
        time.sleep(5)
        DL.driver.find_element_by_css_selector("textarea.form-control").send_keys("53355")
        time.sleep(5)
        DL.driver.find_element_by_css_selector("div.col-sm-6:nth-child(2) > input:nth-child(1)").send_keys("黄元帅装箱追踪")
        time.sleep(5)
        DL.driver.find_element_by_css_selector("div.form-group:nth-child(5) > div:nth-child(2) > input:nth-child(1)")
        DL.driver.find_element_by_css_selector(
            "div.form-group:nth-child(5) > div:nth-child(2) > input:nth-child(1)").clear()
        DL.driver.find_element_by_css_selector(
            "div.form-group:nth-child(5) > div:nth-child(2) > input:nth-child(1)").send_keys("辉爷")
        DL.driver.find_element_by_css_selector("#czdate").click()
        DL.driver.find_element_by_id("laydate_clear").click()
        DL.driver.find_element_by_css_selector("#czdate").send_keys("2020-13-23")
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".btn.btn-danger").click()
        time.sleep(5)
        # try:
        #     a = DL.driver.find_element_by_css_selector("#laydate_time > p:nth-child(2)")
        #     b = "日期不符合格式，请重新选择。"
        #     DL.driver.assertEqual(a, b, "定位不正确")
        # except Exception as e:
        #     print("异常为：", e)

    def lcjlgl(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_css_selector("[href='list_lcsy.php']").click()
        time.sleep(5)
        DL.driver.find_element_by_xpath(
            "/html/body/section/section/section/div/div/section/div/form/div[1]/input").send_keys("53355")
        time.sleep(3)
        DL.driver.find_element_by_xpath(
            "/html/body/section/section/section/div/div/section/div/form/div[2]/button").click()
        time.sleep(5)

    def lcjlgl_FAN1(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_css_selector("[href='list_lcsy.php']").click()
        time.sleep(5)
        DL.driver.find_element_by_xpath(
            "/html/body/section/section/section/div/div/section/div/form/div[1]/input").send_keys(Keys.SPACE)
        DL.driver.find_element_by_xpath(
            "/html/body/section/section/section/div/div/section/div/form/div[2]/button").click()
        time.sleep(5)

    def lcjlgl_FAN2(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_css_selector("[href='list_lcsy.php']").click()
        time.sleep(5)
        DL.driver.find_element_by_xpath(
            "/html/body/section/section/section/div/div/section/div/form/div[1]/input").send_keys("237943553")
        DL.driver.find_element_by_xpath(
            "/html/body/section/section/section/div/div/section/div/form/div[2]/button").click()
        time.sleep(5)

    def lcjlgl_del(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_css_selector("[href='list_lcsy.php']").click()
        time.sleep(5)
        DL.driver.find_element_by_id("chkAll").click()
        inputs = DL.driver.find_elements_by_tag_name("input")
        for input in inputs:
            if input.get_attribute("type") == "checkbox":
                input.click()
                time.sleep(5)
        DL.driver.find_element_by_id("del").click()
        time.sleep(5)
        alert1 = DL.driver.switch_to.alert
        time.sleep(5)
        alert1.accept()
        time.sleep(5)
        # try:
        #     a = DL.driver.find_element_by_link_text("批量删除成功！")
        #     b = "批量删除成功！"
        #     DL.driver.assertEqual(a, b, "没成功删除")
        # except Exception as e:
        #     print("异常为：", e)

    def lcjlgl_del_one(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_css_selector("[href='list_lcsy.php']").click()
        time.sleep(5)
        DL.driver.find_element_by_css_selector("span.label:nth-child(2)").click()
        DL.driver.find_element_by_css_selector("layui-layer-btn0").click()

    def lcjlgl_del_bj(self):
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".sub-menu:nth-child(3) span:nth-child(2)").click()
        DL.driver.find_element_by_css_selector("[href='list_lcsy.php']").click()
        time.sleep(5)
        DL.driver.find_element_by_css_selector("a.label").click()
        time.sleep(5)
        DL.driver.find_element_by_class_name("searchable-select-holder").click()
        DL.driver.find_element_by_css_selector("div.searchable-select-item:nth-child(1)").click()
        time.sleep(5)
        DL.driver.find_element_by_css_selector("div.col-sm-4:nth-child(2) > input:nth-child(1)")
        DL.driver.find_element_by_css_selector("div.col-sm-4:nth-child(2) > input:nth-child(1)").clear()
        DL.driver.find_element_by_css_selector("div.col-sm-4:nth-child(2) > input:nth-child(1)").send_keys("45453")
        time.sleep(5)
        DL.driver.find_element_by_css_selector("div.col-sm-6:nth-child(2) > input:nth-child(1)")
        DL.driver.find_element_by_css_selector("div.col-sm-6:nth-child(2) > input:nth-child(1)").clear()
        DL.driver.find_element_by_css_selector("div.col-sm-6:nth-child(2) > input:nth-child(1)").send_keys("红富士装箱追踪")
        time.sleep(5)
        DL.driver.find_element_by_css_selector("div.form-group:nth-child(6) > div:nth-child(2) > input:nth-child(1)")
        DL.driver.find_element_by_css_selector(
            "div.form-group:nth-child(6) > div:nth-child(2) > input:nth-child(1)").clear()
        DL.driver.find_element_by_css_selector(
            "div.form-group:nth-child(6) > div:nth-child(2) > input:nth-child(1)").send_keys("辉爷")
        DL.driver.find_element_by_id("zt").click()
        DL.driver.find_element_by_css_selector("#zt > option:nth-child(1)").click()
        DL.driver.find_element_by_css_selector("#czdate").click()
        DL.driver.find_element_by_id("laydate_clear").click()
        DL.driver.find_element_by_css_selector("#czdate").send_keys("2020-11-09")
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".btn.btn-danger").click()
