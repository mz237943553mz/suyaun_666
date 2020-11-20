from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("file:///C:/Users/Administrator/Desktop/Selenium/alter.html")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div/input[2]").click()
alert=driver.switch_to.alert
time.sleep(3)
print(alert.text)
alert.accept()
time.sleep(10)
driver.quit()
