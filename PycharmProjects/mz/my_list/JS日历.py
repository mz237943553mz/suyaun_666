from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://trains.ctrip.com/TrainBooking/SearchTrain.aspx")
driver.execute_script("document.getElementById('departDate').removeAttribute('readonly')")
driver.find_element_by_id("departDate").clear()
driver.find_element_by_id("departDate").send_keys("2019-08-12")
time.sleep(10)
