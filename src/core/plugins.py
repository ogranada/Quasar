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
        librerias: librerias necesarias para ejecutar el modulo
        inicio(core): metodo de inicialización de complemento, retorna el objeto
        al_finalizar_carga(core,instancia):se ejecuta despues de que se han instanciado todos los complementos
        prioridad: prioridad del complemento
        
    
'''

class PluginManager(object):

    __plugins = {}
    
    __llaves_de_contrato = "nombre,dependencias,librerias,inicio,al_finalizar_carga".split(',')

    def __init__(self, core, filepath):
        self.__core = core
        plugins = os.listdir(filepath)
        for pluginName in plugins:
            TYPE = open(filepath+os.sep+pluginName).read(10)
            if 'PK' in TYPE:
                importador = zi.zipimporter(filepath+os.sep+pluginName)
                init = importador.load_module('__init__')
                ctc = self.cumple_terminos_contractuales(init)
                if ctc==True:
                    core.importadores[ init.contrato['nombre'] ] = importador
                else:
                    io.log(init.contrato['nombre'],'no cumple el contrato, <ro>falta {0}</ro>'.format(ctc))
            else:
                io.log(pluginName,"isn't a plugin")
        for importador in core.importadores:
            modulo = self.modulo(importador)
            resp = self.cumple_dependencias(modulo,core.importadores)
            if resp[0]:
                io.log(init.contrato['nombre'],'cargado')
            else:
                io.log("dependencias incumplidas para","%s,"%init.contrato['nombre'],"<am>falta",'%s</am>'%resp[1])
                core.importadores_invalidos[init.contrato['nombre']] = core.importadores[ init.contrato['nombre'] ]
        for importador in core.importadores_invalidos:
            core.importadores.pop(importador)
        #####################################
        instancias = []
        importtadoresOrd = []        
        #####################################
        for importador in core.importadores:
            mod = self.modulo(importador)
            pri = mod.contrato["prioridad"]
            importtadoresOrd.append( (pri, importador) )
        importtadoresOrd = sorted(importtadoresOrd, key=lambda tupla: tupla[0])
        for tupla in importtadoresOrd:
            importador = tupla[1]
            mod = self.modulo(importador)
            inst = self.instancia(mod)
            inst.al_finalizar_carga = mod.contrato["al_finalizar_carga"]
            inst.orden = mod.contrato["prioridad"]
            instancias.append( inst )
        #####################################
        instancias.reverse()
        for instancia in instancias:
            print instancia
            instancia.al_finalizar_carga(core,instancia)
            
        
            
    def modulo(self, importador):
        mod = self.__core.importadores[importador].load_module('__init__')
        return mod
            
    def instancia(self, modulo):
        return modulo.init(self.__core)
                
    def cumple_terminos_contractuales(self,init):
        for termino in self.__llaves_de_contrato:
            if not init.contrato.has_key(termino):
                return termino
        return True
        
    def cumple_dependencias(self,plugin,plugins):
        for dependencia in plugin.contrato['dependencias']:
            if dependencia not in plugins.keys():
                return False, dependencia
        for dependencia in plugin.contrato['librerias']:
            try:
                m = __import__(dependencia)
            except ImportError as ie:
                return False, dependencia
        return True, True
            
        






