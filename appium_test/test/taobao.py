#coding=utf-8
from appium import webdriver
import time

desired_caps = {
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.taobao.taobao",
  "appActivity": "com.taobao.tao.welcome.Welcome"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps) 

print("App opened!!")
# time.sleep(5)
# driver.find_element_by_id("com.taobao.taobao:id/yes").click()

# print("Click yes!!")

# driver.find_element_by_id('//android.widget.TextView[@content-desc="天猫超市"]').click()

# time.sleep(5)

# print("Quit!!")

driver.quit()