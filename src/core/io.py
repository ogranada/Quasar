#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
import sys

global LOG

def set_log(log):
    global LOG
    LOG = log
    
def get_log(log):
    global LOG
    return LOG

def write(*args, **kwargs):
    out=sys.stdout
    for arg in args:
        print >> out,arg,    
    for kw in kwargs.keys():
        print >> out,kw,":",kwargs[kw],
    print >> out,""


def log(*args, **kwargs):
    if LOG:
        out=sys.stdout
        for arg in args:
            print >> out,arg,    
        for kw in kwargs.keys():
            print >> out,kw,":",kwargs[kw],
        print >> out,""


def error(*args, **kwargs):
    out=sys.stderr
    for arg in args:
        print >> out,arg,    
    for kw in kwargs.keys():
        print >> out,kw,":",kwargs[kw],
    print >> out,""






set_log(False)


