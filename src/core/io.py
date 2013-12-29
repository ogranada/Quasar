#!/usr/bin/python
# -*- coding:utf-8 -*-

import os, sys, traceback
import platform
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

if sys.version_info >= (3, 0):
    Print = getattr(__builtins__,"get")("print")
else:
    def Print(*args, **kwargs):
        sep=" " if "sep" not in kwargs else kwargs["sep"]
        end="\n" if "end" not in kwargs else kwargs["end"]
        file=sys.stdout if "file" not in kwargs else kwargs["file"]
        if "sep" in kwargs:
            kwargs.pop("sep")
        if "end" in kwargs:
            kwargs.pop("end")
        if "file" in kwargs:
            kwargs.pop("file")
        for i in args:
            file.write(i)
            file.write(sep)
        for k in kwargs.keys():
            file.write("{0}:{1}".format(k,kwargs[k]))        
            file.write(sep)        
        file.write(end)


def putColors(val):
    if platform.system().lower()=="windows":
        for color in colores:
            val = val.replace(color,"")
    else:
        for color in colores:
            val = val.replace(color,colores[color])
    return val


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
            arg = putColors(str(arg))
        Print(arg , end=" ",file=out)
    for kw in kwargs.keys():
        val = kwargs[kw]
        for color in colores:
            val = putColors(val)
        Print(kw,":",val , end=" ",file=out)
    Print("",file=out)
    
    
def log(*args, **kwargs):
    if LOG:
        out=sys.stdout
        for arg in args:
            for color in colores:
                arg = putColors(str(arg))
            Print(arg , end=" ",file=out)
        for kw in kwargs.keys():
            val = kwargs[kw]
            for color in colores:
                val = putColors(val)
            Print(kw,":",val , end=" ",file=out)
        Print("",file=out)


def error(*args, **kwargs):
    out=sys.stderr
    col = putColors("<ro>")
    Print(col,file=out)
    #### Print stacktrace ####
    if(kwargs.get("traceback",False)):
        stack = traceback.format_stack()
        stack = stack[0:-2]
        traceback.Print_exc()
    ##########################
    for arg in args:
        for color in colores:
            arg = putColors(str(arg))
        Print(arg, end=" ",file=out)
    for kw in kwargs.keys():
        val = kwargs[kw]
        for color in colores:
            val = putColors(val)
        Print(kw,":",val, end=" ",file=out)        
    col = putColors("</ro>")
    Print(col,file=out)
    Print("",file=out)
    
e = error
    

def warning(*args, **kwargs):
    out=sys.stderr
    col = putColors("<am>")
    Print(col,file=out)
    #### Print stacktrace ####
    if(kwargs.get("traceback",False)):
        stack = traceback.format_stack()
        stack = stack[0:-2]
        traceback.Print_exc()
    ##########################
    for arg in args:
        for color in colores:
            arg = str(arg).replace(color,colores[color])
        Print(arg, end="",file=out)
    for kw in kwargs.keys():
        val = kwargs[kw]
        for color in colores:
            val = val.replace(color,colores[color])
        Print(kw,":",val, end="",file=out)
    col = putColors("</am>")
    Print(col,file=out)
    Print("",file=out)

w = warning


set_log(False)


