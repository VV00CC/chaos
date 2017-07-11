# -*- coding: utf-8 -*-
import time
import datetime
import os
import sys

def str_2_tuple(*str):
	return str

def get_local_time():
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def get_specific_time():
	return datetime.datetime.now()
        
def tuple_2_str(loc):
    lstring=''
    for item in loc:
        if loc[-1]==item:
            lstring+='%s'%item
        else:
            lstring+='%s,'%item
    return lstring
