#!/usr/bin/python
# -*- coding:utf-8 -*-


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
                fordel = []
                if not tkwargs.has_key(i):
                    raise Exception("Llave inesperada: {0}".format(i))
                elif not kwargs.has_key(i):
                    kwargs[i]=tkwargs[i]()
                    fordel.append(i)
                if not kwargs.has_key(i):
                    raise Exception("Llave inesperada: {0}".format(i))
                if type(kwargs.get(i,'None'))!=tkwargs.get(i,None):
                    raise Exception("Tipo de parametros invalido, se esperaban {0}, recibidos {1}".format(tkwargs[i],type(kwargs[i])))
                for k in fordel:
                    del(kwargs[k])
            return funcion(*args, **kwargs)
        return inner
    return _typer
   
