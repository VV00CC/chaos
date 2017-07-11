# -*- coding: utf-8 -*-
#导入工具模块
import pdb

#导入selenium模块
from selenium import webdriver

#导入appium模块
from appium import webdriver

#导入业务action模块
import sys
sys.path.append("..")
from actions.xxx_actions import *

#导入log模块
from lib.write_log import write_log

#导入初始化driver模块
from actions.init_driver import *

#导入生成report模块
from lib.my_report import *
from lib.utils import *
from lib.exe_deco import *

#定义输入

#定义期望结果



#定义Test Case
@exe_deco
def case_xxx(driver,myReport):
	xxx_action(driver,myReport)
	......
	write_log("this is log")
	
	
#执行Test Case
if __name__ == '__main__':
        #初始化report
        myReport = myReport()
        resultFilePath = myReport.init_result_file()
        case_xxx(myReport,resultFilePath)
	
	
