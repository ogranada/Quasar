
from core import config_manager as cm
from core import memory as mem
from core import io

import core
from core.decorators import *

'''
def validar(x,*args):
    data_types = eval(f.__doc__)
    def call(*args,**kwargs):
        lkw = len(args)+len(kwargs)
        ldt = len(data_types)
        if ldt!=lkw:
            raise Exception("Numero de parametros invalido, se esperaban {0}, recibidos {1}".format(lkw,ldt))
        else:
            param = 0
            for p in range(len(args)):
                if data_types.values()[param] == type():
                    print 'a'
        print data_types
        print args
        print kwargs
    return call
    '''
    
    
@validar(str,b=int,c=float)
def func(a,c=0.0,b=1):
    print a
    print b+c

        
if __name__=='__main__':
    c = cm.ConfigFile("config.cfg")
    func(1,2.0,3)
    print





