#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, sys, traceback

global LOG


colores = {
    "<ne>":'\033[1;30m',
    "</ne>":'\033[0m',
    "<ro>":'\033[1;31m',
    "</ro>":'\033[0m',
    "<ve>":'\033[1;32m',
    "</ve>":'\033[0m',
    "<am>":'\033[1;33m',
    "</am>":'\033[0m',
    "<az>":'\033[1;34m',
    "</az>":'\033[0m',
    "<pu>":'\033[1;35m',
    "</pu>":'\033[0m',
    "<aq>":'\033[1;36m',
    "</aq>":'\033[0m',
    "<bl>":'\033[1;37m',
    "</bl>":'\033[0m',
}


def set_log(log):
    global LOG
    LOG = log
    
def get_log(log):
    global LOG
    return LOG

def write(*args, **kwargs):
    out=sys.stdout
    for arg in args:
        for color in colores:
            arg = str(arg).replace(color,colores[color])
        print >> out,arg,
    for kw in kwargs.keys():
        val = kwargs[kw]
        for color in colores:
            val = val.replace(color,colores[color])
        print >> out,kw,":",val,
    print >> out,""


def log(*args, **kwargs):
    if LOG:
        out=sys.stdout
        for arg in args:
            for color in colores:
                arg = str(arg).replace(color,colores[color])
            print >> out,arg,
        for kw in kwargs.keys():
            val = kwargs[kw]
            for color in colores:
                val = val.replace(color,colores[color])
            print >> out,kw,":",val,
        print >> out,""


def error(*args, **kwargs):
    out=sys.stderr
    print >> out, colores["<ro>"]
    #### print stacktrace ####
    if(kwargs.get("traceback",False)):
        stack = traceback.format_stack()
        stack = stack[0:-2]
        traceback.print_exc()
    ##########################
    for arg in args:
        for color in colores:
            arg = str(arg).replace(color,colores[color])
        print >> out,arg,
    for kw in kwargs.keys():
        val = kwargs[kw]
        for color in colores:
            val = val.replace(color,colores[color])
        print >> out,kw,":",val,
    print >> out, colores["</ro>"]
    print >> out,""
    
e = error
    

def warning(*args, **kwargs):
    out=sys.stderr
    print >> out, colores["<am>"]
    #### print stacktrace ####
    if(kwargs.get("traceback",False)):
        stack = traceback.format_stack()
        stack = stack[0:-2]
        traceback.print_exc()
    ##########################
    for arg in args:
        for color in colores:
            arg = str(arg).replace(color,colores[color])
        print >> out,arg,
    for kw in kwargs.keys():
        val = kwargs[kw]
        for color in colores:
            val = val.replace(color,colores[color])
        print >> out,kw,":",val,
    print >> out, colores["</am>"]
    print >> out,""

w = warning


set_log(False)


