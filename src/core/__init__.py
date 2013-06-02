#!/usr/bin/python
# -*- coding:utf-8 -*-

import os,sys,user

from core import config_manager
from core import memory as mem
from core import plugins
from core import paths
from core import io
from core.decorators import *



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
            cls._instance.objetos = {}
            cls._instance.dir_mods = {}
        return cls._instance
    
    def __init__(self, *args, **kwargs):
        config_file = kwargs.get("config_file", paths.store_from_base( "config.cfg" ) )
        self.config_manager = config_manager.ConfigFile(config_file)
        self.plugin_manager = plugins.PluginManager(self,paths.get_path(self.config_manager['PLUGINS']["path"]))





