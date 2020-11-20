from selenium.webdriver.support.select import Select
import time
from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://sahitest.com/demo/selectTest.htm")
se=driver.find_element_by_id("s1Id")
time.sleep(3)
Select(se).select_by_value("o1")
driver.quit()