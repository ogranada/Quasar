#!/usr/bin/python
# -*- coding:utf-8 -*-

import core.io as io
import core.paths as paths
import json
import os
import sys


class Map(object):

    def __init__(self, data={}):
        self.data = data

    def __getitem__(self, key):
        '''Sobrecarga del operador [] para obtener el dato de una posición dada.'''
        if key in self.data:
            return self.data[key]
        else:
            return None

    def __setitem__(self, index, item):
        '''Sobrecarga del operador [] para cambiar el dato de una posición dada.'''
        self.data[index] = item

    def __str__(self):
        return str(self.data.keys())


class ConfigFile(object):

    def __new__(cls, *args, **kwargs):
        orig = super(ConfigFile, cls)
        cls._instance = orig.__new__(cls)
        cls._instance.config = {}
        return cls._instance

    def __init__(self, name):
        try:
            self.name = name
            if not os.path.exists(name):
                from datetime import datetime
                with open(name, 'w') as f:
                    f.write("""{\n\t"UPDATED":"%s/%s/%s","PLUGINS":{},\n\t"PERMI
SSIONS":{}\n}\n'""" %
                            datetime.isocalendar(datetime.now()))
            with open(name) as configFile:
                content = configFile.read()
                self.config = json.loads(content)
            io.log('loaded', name.split(os.sep)[-1])
        except Exception as error:
            io.error(error)

    def __str__(self):
        '''Sobrecarga del metodo de conversion a cadena str.'''
        return str(self.config.keys())

    def __unicode__(self):
        '''Sobrecarga del metodo de conversion a cadena str.'''
        return unicode(self.config.keys())

    def __getitem__(self, section):
        '''Sobrecarga del operador [] para obtener el dato de una posición dada.'''
        if section in self.config:
            data = self.config[section]
            return Map(data)
        else:
            return None

    def __setitem__(self, index, items):
        '''Sobrecarga del operador [] para cambiar el dato de una posición dada.'''
        self.config.set(index, items[0], items[1])
        self.config["UPDATED"] = '"%s/%s/%s"'%datetime.isocalendar(datetime.now())
        with open(self.name, 'w') as f:
            strjson = json.dumps( self.config, sort_keys=True,indent=4, separators=(',', ': ') )
            f.write(strjson)
