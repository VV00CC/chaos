# -*- coding: utf-8 -*-

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import sys
sys.path.append("..")
from lib.my_exception import *
from lib.write_log import *


class Action(object):
    #默认timeout为10秒
    time_out = 10

    #初始化driver、report、等
    def __init__(self, driver, myReport):
        self.driver = driver
        self.myReport = myReport

    #设置time_out
    def set_timeout(time_out):
        self.time_out = time_out

    #打开页面，校验页面标题是否加载正确
    def open(self, url, pagetitle):
        try:
            #使用get打开访问链接地址
            self.driver.get(url)
            self.driver.maximize_window()
            #使用assert进行校验，打开的页面标题是否与配置的标题一致。调用on_page()方法
            self.myReport.my_assert(self.on_page(pagetitle),u"打开开页面失败 %s"% url)
        except:
            write_log(u"cannot open page %s"%url)
    

    #重写元素定位方法
    #
    def find_element(self,loc):
        #return self.driver.find_element(*loc)
        try:
            WebDriverWait(self.driver,self.time_out).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            write_log(u"%s 页面中未能找到 %s 元素"%(self, loc))
            raise NoneWebElementErr(*loc)
            
    def find_elements(self,loc):
        #return self.driver.find_element(*loc)
        try:
            WebDriverWait(self.driver,self.time_out).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_elements(*loc)
        except:
            write_log(u"%s 页面中未能找到 %s 元素"%(self, loc))
            raise NoneWebElementErr(*loc)
        
        

    def find_child_element(self,el,loc):
        #return el.find_element(*loc)
        try:
            WebDriverWait(self.driver,self.time_out).until(lambda driver: el.find_element(*loc).is_displayed())
            return el.find_element(*loc)
        except:
            write_log(u"%s 页面中未能找到 %s 元素"%(self, loc))
            raise NoneWebElementErr(*loc)

    def find_enable_child_element(self,el,loc):
        #return el.find_element(*loc)
        try:
            WebDriverWait(self.driver,self.time_out).until(lambda driver: el.find_element(*loc).is_enabled())
            return el.find_element(*loc)
        except:
            write_log(u"%s 页面中未能找到 %s 元素"%(self, loc))
            raise NoneWebElementErr(*loc)
                
    def find_enable_element(self,loc):
        #return self.driver.find_element(*loc)
        try:
            WebDriverWait(self.driver,self.time_out).until(lambda driver: driver.find_element(*loc).is_enabled())
            return self.driver.find_element(*loc)
        except:
            write_log(u"%s 页面中未能找到 %s 元素"%(self, loc))
            raise NoneWebElementErr(*loc)

                 
    def find_clickable_element(self,loc):
        #return self.driver.find_element(*loc)
        try:
            return WebDriverWait(self.driver,self.time_out).until(EC.element_to_be_clickable(loc))

        except:
            write_log(u"%s 页面中未能找到 %s 元素"%(self, loc))
            raise NoneWebElementErr(*loc)

    def find_present_element(self,loc):
        #return self.driver.find_element(*loc)
        try:
            return WebDriverWait(self.driver,self.time_out).until(EC.presence_of_element_located(loc))
        except:
            write_log(u"%s 页面中未能找到 %s 元素"%(self, loc))
            raise NoneWebElementErr(*loc)

    def find_visibility_element(self,loc):
        #return self.driver.find_element(*loc)
        try:
            return WebDriverWait(self.driver,self.time_out).until(EC.visibility_of_element_located(loc))
        except:
            write_log(u"%s 页面中未能找到 %s 元素"%(self, loc))
            raise NoneWebElementErr(*loc)

    #重写switch_frame方法
    def switch_frame(self, loc):
        try:
            return self.driver.switch_to_frame(loc)
        except:
            write_log(u"%s 无法切换frame %s"%(self, loc))
            
    #使用current_url获取当前窗口Url地址，进行与配置地址作比较，返回比较结果（True False）
    def on_page(self, pagetitle):
        return pagetitle in self.driver.title
    
    #使用current_url获取当前窗口Url地址，进行与配置地址作比较，返回比较结果（True False）
    def on_page_source(self, content):
        return content in self.driver.page_source

    #定义script方法，用于执行js脚本，范围执行结果
    def script(self, src):
        self.driver.execute_script(src)
            
    #重写定义send_keys方法
    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
                if click_first:
                        self.find_enable_element(loc).click()
                if clear_first:
                        self.find_enable_element(loc).clear()
                        self.find_enable_element(loc).send_keys(vaule)
        except Exception,e:
            write_log(str(e))
            self.myReport.my_assert(False,str(e))
				
    #重写定义click方法
    def click(self, loc,is_child=False,ploc=None,pEl=None):
        try:
            if not is_child:
               self.find_clickable_element(loc).click()
            elif ploc is not None:
                el = self.find_element(ploc)
                self.find_enable_child_element(el,loc).click()
            else:
                self.find_enable_child_element(pEl,loc).click()
        except Exception,e:
            write_log(str(e))
            self.myReport.my_assert(False,str(e))


    #重写定义get_attribute方法
    def get_attribute(self,loc,attr_name,is_child=False,pEl=None):
        attr_value = ""
        try:
            if not is_child:
                attr_value = self.find_element(loc).get_attribute(attr_name)
            else:
                attr_value = self.find_child_element(pEl,loc).get_attribute(attr_name)
        except Exception,e:
            write_log(str(e))
            self.myReport.my_assert(False,str(e))
        finally:
            return attr_value

    #重写定义text方法
    def get_text(self,loc,is_child=False,pEl=None):
        text = ""
        try:
            if not is_child:
                text = self.find_element(loc).text
            else:
                text = self.find_child_element(pEl,loc).text
        except Exception,e:
            write_log(str(e))
            #self.myReport.my_assert(False,str(e))
        finally:
            return text

    #判断元素存在
    def exist_element(self,loc):
        try:
            return self.find_element(loc) is not None
        except:
            return None
    #获取元素个数
    def get_elements_count(self,loc):
        try:
            return len(self.find_elements(loc))
        except:
            return 0
        
	
    #关闭浏览器
    def close(self):
        self.driver.close()
        self.driver.quit()
    #切换上下文
    def switch_context(self,ctx_name):
        flag = False
        try:
            contexts = self.driver.contexts
            for ctx in contexts:
                if ctx_name in ctx:
                    self.driver.switch_to.context(ctx)
                    write_log(u"switch to context %s"%self.driver.current_context)
                    flag = True
	except Exception,e:
            write_log(u"cannot switch to context %s"%str(e))
            self.myReport.my_assert(False,str(e))
        finally:
            return flag
		    
    #切换到默认上下文
    def switch_default_context(self):
	self.switch_context("NATIVE_APP")

    #按手机返回键
    def goback(self):
        self.driver.keyevent(4)
