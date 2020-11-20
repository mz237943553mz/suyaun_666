
from selenium import webdriver
import time
browser=webdriver.Firefox()
browser.get("https://mail.qq.com/")
browser.switch_to.frame("login_frame")
browser.find_element_by_css_selector(".inputstyle").send_keys("237943553")
browser.find_element_by_css_selector(".inputstyle.password").send_keys("maozhan2379435@!")
browser.find_element_by_css_selector("#login_button").click()
browser.switch_to.default_content()
time.sleep(3)
browser.find_element_by_css_selector("[id='composebtn'][target='mainFrame']").click()
time.sleep(3)
browser.find_element_by_css_selector("body").send_keys("笑口常开")
browser.switch_to.frame("mainFrame")
browser.find_element_by_css_selector("#toAreaCtrl > div:nth-child(2) > input:nth-child(1)").send_keys("328649501")
time.sleep(3)
browser.find_element_by_id("subject").send_keys("你好吗？")
time.sleep(3)
browser.find_element_by_css_selector(".btn_gray.btn_space").click()
time.sleep(3)
browser.switch_to.default_content()


