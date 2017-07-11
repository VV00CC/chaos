# -*- coding: utf-8 -*-
#导入工具模块
import time

#导入selenium相关模块
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

#导入appium相关模块
from appium import webdriver

#导入自封装模块
from .SeleniumPage import Action
from lib.utils import *
from lib.my_exception import *
from lib.write_log import *

#定义页面类
#继承SeleniumPage中的Action类
class pageName(Action):
        #固定输入值
	xxx_input = ""

	
	#定位器，通过元素属性定位元素对象
	xxx_loc = (By.XPATH,"")
	xxx_loc = (By.ID,"")
	xxx_loc = (By.LINK_TEXT,"")
	
	
	#需要判定的固定输出值
	xxx_show = ""
	
	#页面中的逻辑操作
	def action_xxx(self,""):
		.....
		write_log("this is log")
		
