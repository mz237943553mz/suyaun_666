from selenium import webdriver
import time
browser=webdriver.Firefox()
browser.get("https://passport.meituan.com/account/unitivelogin?")
time.sleep(3)

browser.find_element_by_id("public-email").send_keys("17361637911")
browser.find_element_by_name("password").send_keys("mz237943553")
browser.find_element_by_class_name("btn").click()
browser.find_element_by_css_selector('img[alt="美团网"][src="//s0.meituan.net/bs/file/?f=fe-sso-fs:build/page/static/banner/www.jpg"]')
# browser.find_elements_by_link_text("免费注册").click()

time.sleep(10)

browser.quit()



