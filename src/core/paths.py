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
    

set_base(os.getcwd())


