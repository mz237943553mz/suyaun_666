# 项目名称：
# 所属模块：
# date:2020-10-28
# author:mz
# 代码实现功能：selenium基本方法归纳
# 版本：v1.0
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Firefox()
driver.get("https://www.baidu.com/index.php?tn=monline_3_dg")

se=driver.find_element_by_css_selector(".s-top-right-text.c-font-normal.c-color-t")
ActionChains(driver).move_to_element(se).perform()
driver.find_element_by_css_selector("[target='_blank']").click()


driver.quit()