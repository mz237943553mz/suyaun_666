from selenium import webdriver
import time
we=webdriver.Firefox()
we.get("https://www.baidu.com")
time.sleep(2)
newwindow='window.open("https://www.baidu.com/index.php?tn=monline_3_dg")'
newwindow1='window.open("https://tieba.baidu.com/index.html")'
we.execute_script(newwindow)
we.execute_script(newwindow1)
handle=we.window_handles
we.switch_to.window(handle[0])
time.sleep(3)
we.find_element_by_id("kw").send_keys('迪丽热巴')