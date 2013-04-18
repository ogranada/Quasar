#!/usr/bin/python
# -*- coding:utf-8 -*-

import os,sys

class Core(object):
        
    def __new__(cls, *args, **kwargs):
        '''
        Constructor de nuevo estilo. Gracias a esto se crea una clase que implementa
        el patron de diseño singleton.
        '''
        if not hasattr(cls, '_instance'):
            orig = super(Core, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
            cls._instance.importadores = {}
            cls._instance.importadores_invalidos = {}
        return cls._instance
    
    #def __init__(self, *args, **kwargs):
    #    self.plugins = {}





