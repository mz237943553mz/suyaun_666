from selenium import  webdriver
import time
driver=webdriver.Firefox()
driver.get("file:///C:/Users/Administrator/Desktop/Selenium/checkbox.html")
inputs=driver.find_elements_by_tag_name("input")
for input in inputs:
    if input.get_attribute("type")=="checkbox":
        input.click()
        time.sleep(2)


# driver.find_elements_by_css_selector("input[type='checkbox']").pop(1).click()

time.sleep(5)
driver.quit()