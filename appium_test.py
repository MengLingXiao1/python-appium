from appium import webdriver
import time
desired_capabilities= {}
desired_capabilities['platformName'] = 'Android'
desired_capabilities['platformVersion'] = '8'
desired_capabilities['deviceName'] = 'test'
desired_capabilities['appPackage']= 'com.android.calculator2'
desired_capabilities['app'] = ''
desired_capabilities['appActivity'] = '.Calculator'
desired_capabilities['unicodeKeyboard'] = True
desired_capabilities['resetKeyboard'] = True
desired_capabilities['noReset'] = True
desired_capabilities['fullReset'] = False
print(desired_capabilities)
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_capabilities)
driver.implicitly_wait(10)
driver.find_element_by_id('com.android.calculator2:id/digit_1').click()
time.sleep(1)
driver.find_element_by_accessibility_id('加').click()
time.sleep(1)
driver.find_element_by_id('com.android.calculator2:id/digit_3').click()
time.sleep(1)
driver.find_element_by_accessibility_id('等于').click()

