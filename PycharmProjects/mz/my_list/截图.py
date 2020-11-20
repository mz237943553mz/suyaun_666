from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()
time.sleep(2)
picture_time=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime((time.time())))
print(picture_time)
try:
    picture_url=driver.get_screenshot_as_file("D:\picture"+picture_time+'.png')
    print("%s:截图成功！！！"%picture_url)
except Exception as msg:
    print(msg)
    driver.quit()


