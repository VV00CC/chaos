#coding=utf-8
#导入selenium模块
from selenium import webdriver as selenium_driver

#导入appium模块
from appium import webdriver as appium_driver

#初始化selenium driver
def init_selenium_driver():
        driver = selenium_driver.Chrome()
        driver.implicitly_wait(60)
	return driver
	
#初始化appium driver
def init_appium_driver():
	desired_caps = {}
	desired_caps['platformName'] = 'Android'
	desired_caps['platformVersion'] = '4.4.4'
	desired_caps['deviceName'] = 'e2a5c099'
	desired_caps['appPackage'] = 'com.tencent.mm'
	desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
	desired_caps['newCommandTimeout'] = "60"
	desired_caps['noReset'] = "true"
	desired_caps['recreateChromeDriverSessions'] = "true"

	desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}

	driver = appium_driver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

        driver.implicitly_wait(60)
	
	return driver
