#!/usr/bin/python
# -*- coding:utf-8 -*-

import ConfigParser
import os
import io
import sys
import paths


class Map(object):

    def __init__(self, data={}):
        self.data = data
    
    def __getitem__(self, key):
        '''Sobrecarga del operador [] para obtener el dato de una posición dada.'''
        if self.data.has_key(key):            
            return self.data[key]
        else:
            return None

    def __setitem__(self, index,item):
        '''Sobrecarga del operador [] para cambiar el dato de una posición dada.'''
        self.data[index]=item
        
    def __str__(self):
        return str(self.data.keys())
    

class ConfigFile(object):

    def __new__(cls,*args,**kwargs):
        orig = super(ConfigFile, cls)
        cls._instance = orig.__new__(cls, *args, **kwargs)
        cls._instance.config = ConfigParser.ConfigParser()
        return cls._instance
        
    def __init__(self,name):
        try:
            self.name = name
            self.config.readfp(open(paths.get_base()+name))
            io.log('cargado',paths.get_base()+name)
        except Exception as error:
            io.error(error)
        
    
    def __str__(self):
        '''Sobrecarga del metodo de conversion a cadena str.'''
        return str(self.config.sections())

    
    def __getitem__(self, section):
        '''Sobrecarga del operador [] para obtener el dato de una posición dada.'''
        if self.config.has_section(section):
            data = self.config.items(section)
            res = {}
            for i in data:
                res[i[0]]=i[1]
            return Map(res)
        else:
            return None

    def __setitem__(self, index,items):
        '''Sobrecarga del operador [] para cambiar el dato de una posición dada.'''
        self.config.set(index , items[0], items[1])
        f = open(self.name,'w')
        self.config.write(f)
        

