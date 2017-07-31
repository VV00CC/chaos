# -*- coding: utf-8 -*-
#导入selenium模块
from selenium import webdriver 

#导入appium模块
from appium import webdriver

#导入初始化driver模块
from actions.init_driver import *

#导入log模块
from .write_log import write_log


#导入生成report模块
from .my_report import *
from .utils import *


def exe_deco(func):
        def _deco(myReport,resultFilePath):
            startTime=get_specific_time()
            #初始化driver
            #selenium_driver = init_selenium_driver()
            appium_driver = init_appium_driver()
            #调用Test Case
            try:
                myReport.set_test_case_name(func.__name__)
                func(appium_driver,myReport)
                print func.__name__+" finished..."
            except Exception,e:
                write_log(str(e))
                myReport.my_assert(False,str(e))
                print func.__name__+" failed..."
            finally:
                #退出driver
                appium_driver.quit()
            #写入Report
            endTime = get_specific_time()
            duration = endTime-startTime
            myReport.add_result(resultFilePath,startTime,endTime,duration)
            myReport.reset_result()
        return _deco

