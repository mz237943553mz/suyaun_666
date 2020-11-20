from  selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("file:///C:/Users/Administrator/Desktop/Selenium/checkbox.html")
radio1=driver.find_elements_by_css_selector("input[type='radio']")
for radio in radio1:
    radio.click()
    time.sleep(5)
time.sleep(2)
driver.quit()

