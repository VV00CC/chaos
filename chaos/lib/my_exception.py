# -*- coding:utf-8 -*-
from .utils import *

class NoneWebElementErr(Exception):   
    def __init__(self, *loc):
        Exception.__init__(self,'Not get avaliable web element by locator:'+tuple_2_str(loc))
