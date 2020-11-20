import time
from productsuyaun.public import login1
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
DL=login1.Test_Denglu()

class XZCP3():

    def sygl(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_link_text("新增溯源实例").click()
        DL.driver.find_element_by_name("name").send_keys("花牛苹果装箱追踪")
        time.sleep(5)
        DL.driver.switch_to.frame(0)
        DL.driver.find_element_by_xpath("/html/body").send_keys(Keys.TAB)
        DL.driver.find_element_by_xpath("/html/body").send_keys("为了保证广大消费者的利益，追踪每一个产品的运输过程")
        time.sleep(5)
        DL.driver.switch_to.default_content()
        DL.driver.find_element_by_css_selector(".btn").click()
        time.sleep(5)
        # try:
        #     a = DL.driver.find_element_by_link_text("恭喜，溯源增加成功！")
        #     b = "恭喜，溯源增加成功！"
        #     DL.driver.assertEqual(a, b, "新增溯源不成功")
        # except Exception as e:
        #     print("异常为：", e)

    def sygl_FAN1(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_link_text("新增溯源实例").click()
        DL.driver.find_element_by_name("name").send_keys(Keys.SPACE)
        time.sleep(5)
        DL.driver.switch_to.frame(0)
        DL.driver.find_element_by_xpath("/html/body").send_keys(Keys.TAB)
        DL.driver.find_element_by_xpath("/html/body").send_keys("为了保证广大消费者的利益，追踪每一个产品的运输过程")
        time.sleep(5)
        DL.driver.switch_to.default_content()
        DL.driver.find_element_by_css_selector(".btn").click()
        time.sleep(5)

    def sygl_FAN2(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_link_text("新增溯源实例").click()
        DL.driver.find_element_by_name("name").send_keys(Keys.SPACE)
        time.sleep(5)
        DL.driver.switch_to.frame(0)
        DL.driver.find_element_by_xpath("/html/body").send_keys(Keys.TAB)
        DL.driver.find_element_by_xpath("/html/body").send_keys(Keys.SPACE)
        time.sleep(5)
        DL.driver.switch_to.default_content()
        DL.driver.find_element_by_css_selector(".btn").click()
        time.sleep(5)
        # try:
        #     a = DL.driver.find_element_by_link_text("还没有填写溯源内容")
        #     b = "还没有填写溯源内容"
        #     DL.driver.assertEqual(a, b, "新增溯源成功")
        # except Exception as e:
        #     print("异常为：", e)

    def sygl1(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[2]/a").click()
        DL.driver.find_element_by_class_name("form-control").send_keys("花牛苹果装箱追踪")
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".btn.btn-success").click()
        time.sleep(5)

    def sygl1_FAN1(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[2]/a").click()
        DL.driver.find_element_by_class_name("form-control").send_keys("花牛苹果装箱追踪1")
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".btn.btn-success").click()
        time.sleep(5)

    def sygl1_FAN2(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[2]/a").click()
        DL.driver.find_element_by_class_name("form-control").send_keys(Keys.SPACE)
        time.sleep(5)
        DL.driver.find_element_by_css_selector(".btn.btn-success").click()
        time.sleep(5)

    def sygl_del_all(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[2]/a").click()
        time.sleep(2)
        DL.driver.find_element_by_id("chkAll").click()
        inputs = DL.driver.find_elements_by_tag_name("input")
        for input in inputs:
            if input.get_attribute("type") == "checkbox":
                input.click()
                time.sleep(2)
        DL.driver.find_element_by_id("del").click()
        time.sleep(2)
        alert1 = DL.driver.switch_to.alert
        time.sleep(2)
        alert1.accept()
        time.sleep(2)
        alert2 = DL.driver.switch_to.alert
        time.sleep(2)
        alert2.accept()
        time.sleep(2)

    def sygl_del_one(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[2]/a").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector("span.label:nth-child(2)").click()
        time.sleep(5)
        DL.driver.find_element_by_class_name("layui-layer-btn0").click()
        time.sleep(5)

    def sygl_bj(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[2]/a").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector(
            ".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(6) > a:nth-child(1)").click()
        DL.driver.find_element_by_name("name")
        DL.driver.find_element_by_name("name").clear()
        DL.driver.find_element_by_name("name").send_keys("红富士苹果装箱追踪")
        time.sleep(5)
        DL.driver.switch_to.frame(0)
        DL.driver.find_element_by_xpath("/html/body").send_keys(Keys.TAB)
        DL.driver.find_element_by_xpath("/html/body")
        DL.driver.find_element_by_xpath("/html/body").clear()
        DL.driver.find_element_by_xpath("/html/body").send_keys("救死扶伤韩老魔")
        time.sleep(5)
        DL.driver.switch_to.default_content()
        DL.driver.find_element_by_css_selector(".btn").click()
        time.sleep(5)

    def sygl_ck(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[2]/a").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector(
            ".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(4) > span:nth-child(1)").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector(".layui-layer-ico").click()

    def plsycz_wlm(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[3]/a").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector("#txm").send_keys("53355")
        time.sleep(2)
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").click()
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(7)").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)").click()

    def plsycz_FAN1(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[3]/a").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector("#txm").send_keys(Keys.SPACE)
        time.sleep(2)
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").click()
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(7)").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)").click()

    def plsycz_FAN2(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[3]/a").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector("#txm").send_keys("53300")
        time.sleep(2)
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").click()
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(7)").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(1) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)").click()

    def plsycz_ID(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[3]/a").click()
        time.sleep(2)
        target_elem = DL.driver.find_element_by_css_selector(
            "div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)")
        DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        DL.driver.find_element_by_css_selector("div.col-sm-2:nth-child(2) > input:nth-child(1)").send_keys("5")
        DL.driver.find_element_by_css_selector("div.col-sm-2:nth-child(3) > input:nth-child(1)").send_keys("5")
        time.sleep(5)
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").click()
        DL.driver.find_element_by_css_selector(".has-next > div:nth-child(2) > div:nth-child(11)").click()
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)").click()
        time.sleep(5)

    def plsycz_ID_FAN(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[3]/a").click()
        time.sleep(2)
        target_elem = DL.driver.find_element_by_css_selector(
            "div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)")
        DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        DL.driver.find_element_by_css_selector("div.col-sm-2:nth-child(2) > input:nth-child(1)").send_keys(Keys.SPACE)
        DL.driver.find_element_by_css_selector("div.col-sm-2:nth-child(3) > input:nth-child(1)").send_keys(Keys.SPACE)
        time.sleep(5)
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").click()
        DL.driver.find_element_by_css_selector(".has-next > div:nth-child(2) > div:nth-child(11)").click()
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(2) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)").click()
        time.sleep(5)

    def plsycz_pc(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[3]/a").click()
        time.sleep(2)
        target_elem = DL.driver.find_element_by_css_selector(
            "div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)")
        DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        DL.driver.find_element_by_xpath(
            "/html/body/section/section/section/div[3]/div/section/div/form/div[1]/div[1]/div/div[1]").click()
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").click()
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(23)").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)").click()
        time.sleep(2)

    def plsycz_cpm(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[3]/a").click()
        time.sleep(2)
        target_elem = DL.driver.find_element_by_css_selector(
            "div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)")
        DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        DL.driver.find_element_by_xpath(
            "/html/body/section/section/section/div[4]/div/section/div/form/div[1]/div[1]/div/div[1]").click()
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(17)").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").click()
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(20)").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(4) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)").click()
        time.sleep(2)

    def plsycz_date(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[3]/a").click()
        time.sleep(2)
        target_elem = DL.driver.find_element_by_css_selector(
            "div.row:nth-child(5) > div:nth-child(1) > section:nth-child(1) > header:nth-child(1) > h3:nth-child(1)")
        DL.driver.execute_script("return arguments[0].scrollIntoView();", target_elem)
        DL.driver.find_element_by_xpath(
            "/html/body/section/section/section/div[5]/div/section/div/form/div[1]/div[1]/div/div[1]").click()
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(5) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(5) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").click()
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(5) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(4) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(18)").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(5) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)").click()
        time.sleep(2)

    def syczjl(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[4]/a").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector("#key").send_keys("产品状态异常 ")
        time.sleep(2)
        DL.driver.find_element_by_css_selector("button.btn:nth-child(2)").click()
        time.sleep(5)

    def syczjl_FAN1(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[4]/a").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector("#key").send_keys(Keys.SPACE)
        time.sleep(2)
        DL.driver.find_element_by_css_selector("button.btn:nth-child(2)").click()
        time.sleep(5)

    def syczjl_FAN2(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[4]/a").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector("#key").send_keys("杀人放火历飞雨")
        time.sleep(2)
        DL.driver.find_element_by_css_selector("button.btn:nth-child(2)").click()
        time.sleep(5)

    def syczjl_def_all(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[4]/a").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector("#chkAll").click()
        inputs = DL.driver.find_elements_by_tag_name("input")
        for input in inputs:
            if input.get_attribute("type") == "checkbox":
                input.click()
                time.sleep(2)
        DL.driver.find_element_by_id("del").click()
        time.sleep(2)
        alert1 = DL.driver.switch_to.alert
        time.sleep(2)
        alert1.accept()
        time.sleep(2)
        alert2 = DL.driver.switch_to.alert
        time.sleep(2)
        alert2.accept()
        time.sleep(2)

    def syczjl_def_one(self):
        DL.driver.find_element_by_link_text("溯源实例管理").click()
        DL.driver.find_element_by_xpath("/html/body/section/aside/div/ul/li[4]/ul/li[4]/a").click()
        time.sleep(2)
        DL.driver.find_element_by_css_selector(
            ".table > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > span:nth-child(1)").click()
        DL.driver.find_element_by_css_selector(".layui-layer-btn0").click()
        DL.driver.find_element_by_css_selector(
            "div.row:nth-child(3) > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2)").click()












