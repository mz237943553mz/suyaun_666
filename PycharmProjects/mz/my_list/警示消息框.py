from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("file:///C:/Users/Administrator/Desktop/Selenium/alter.html")
driver.find_element_by_xpath("/html/body/div/input[3]").click()
dialog_box=driver.switch_to.alert
time.sleep(2)
print(dialog_box.text)
dialog_box.accept()
print(driver.find_element_by_xpath("//*[@id='textSpan']/font").text)
time.sleep(2)
driver.quit()