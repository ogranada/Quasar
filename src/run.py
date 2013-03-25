
from core import config_manager as cm
from core import memory as mem
from core import io

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
   
def validar(*targs, **tkwargs):
    def _typer(funcion):
        def inner(*args, **kwargs):
            largs = len(args)
            ltargs = len(targs)
            lkwargs = len(kwargs)
            ltkwargs = len(tkwargs)
            if ltargs+ltkwargs!=largs+lkwargs:
                raise Exception("Numero de parametros invalido, se esperaban {0}, recibidos {1}".format(ltargs,largs))
            rango = len(targs) if len(args)>=len(targs) else len(args)
            for i in range(rango):
                if type(args[i])!=targs[i]:
                    raise Exception("Tipo de parametros invalido, se esperaban {0}, recibidos {1}".format(targs[i],type(args[i])))
            kw = tkwargs if len(tkwargs)>len(kwargs) else kwargs
            for i in kw.keys():
                #print targs,tkwargs
                #print args,kwargs
                fordel = []
                if not tkwargs.has_key(i):
                    raise Exception("Llave inesperada: {0}".format(i))
                elif not kwargs.has_key(i):
                    kwargs[i]=tkwargs[i]()
                    fordel.append(i)
                if not kwargs.has_key(i):
                    raise Exception("Llave inesperada: {0}".format(i))
                if type(kwargs.get(i,'None'))!=tkwargs.get(i,None):
                    #print type(kwargs.get(i,'None')),tkwargs.get(i,None)
                    raise Exception("Tipo de parametros invalido, se esperaban {0}, recibidos {1}".format(tkwargs[i],type(kwargs[i])))
                for k in fordel:
                    print k
                    del(kwargs[k])
            return funcion(*args, **kwargs)
        return inner
    return _typer
    
    
@validar(str,b=int,c=float)
def func(a,c=0.0,b=1):
    print a
    print b+c

        
if __name__=='__main__':
    c = cm.ConfigFile("config.cfg")
    func('1',2.0,3)
    print





