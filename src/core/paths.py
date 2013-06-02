#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys

global BASE

def get_base():
    global BASE
    return BASE

def set_base(base):
    global BASE
    BASE = base + os.sep if len(base)>0 and base[-1]!=os.sep else base
    
def store_from_base(relpath):
    return os.sep.join([get_base(),relpath]).replace(os.sep*2, os.sep)
    
def get_path(relpath):
    return relpath.replace("<basepath/>",get_base()).replace(os.sep*2, os.sep)
    

