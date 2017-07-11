# -*- coding: utf-8 -*-
#导入工具模块
import pdb

#导入selenium模块
from selenium import webdriver 

#导入appium模块
from appium import webdriver

#导入业务action模块
from .xxxPage import xxxPage

#导入初始化driver模块
from .init_driver import *

#导入log模块
import sys
sys.path.append("..")
from lib.write_log import write_log

#导入生成report模块
from lib.my_report import *
from lib.utils import *


#定义Test Case 中常用方法
def logic_action_xxx(driver,myReport,""):
    xxx = xxxPage(driver,myReport)
    xxx.action_xxx("")
    

    
    
