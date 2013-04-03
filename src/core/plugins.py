#!/usr/bin/python
# -*- coding:utf-8 -*-

import os,sys
import zipimport as zi
import io
from utils import Nodo



'''
Contrato:
    Cada uno de los plugins debe contener un fichero que se llame __init__.py
    este debe tener un diccionario llamado contrato, el cual debe tener datos
    como:
        nombre:nombre del complemento
        dependencias: complementos de los que depende
        init: metodo de inicialización de complemento
    
'''

class PluginManager(object):

    __plugins = {}

    def __init__(self, core, filepath):
        plugins = os.listdir(filepath)
        for pluginName in plugins:
            TYPE = open(filepath+os.sep+pluginName).read(10)
            if 'PK' in TYPE:
                pluginImporter = zi.zipimporter(filepath+os.sep+pluginName)
                init = pluginImporter.load_module('__init__')
                if init.contrato.has_key('init'):
                    core.plugins[ init.contrato['nombre'] ] = init
                else:
                    io.log(init.contrato['nombre'],'no cunple el contrato, falta \033[1;33m{0}\033[0m'.format('init'))
                    continue
                io.log(init.contrato['nombre'],'cargado')                
            else:
                io.log(pluginName,"isn't a plugin")
        for plugin in core.plugins.values():
            
                







