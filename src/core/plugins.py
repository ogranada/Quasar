#!/usr/bin/python
# -*- coding:utf-8 -*-

import os,sys
import zipimport as zi
import io

io.LOG = True

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
        dir_plugins= []
        sys.path.append(filepath)
        plugins = os.listdir(filepath)
        core.instancia = self.instancia
        for pluginName in plugins:
            if pluginName[0:3].lower()=="dis":
                continue
            if os.path.isdir(filepath+os.sep+pluginName):
                TYPE = "DIR"
            else:
                try:
                    TYPE = open(filepath+os.sep+pluginName).read(10)
                except IOError as err:
                    TYPE = "UNDEFINED"
            if 'PK' in TYPE:
                importador = zi.zipimporter(filepath+os.sep+pluginName)
                try:
                    init = importador.load_module('__init__')
                    ctc = self.cumple_terminos_contractuales(init)
                    if ctc==True:
                        core.importadores[ init.contrato['nombre'] ] = importador
                    else:
                        io.log(init.contrato['nombre'],'no cumple el contrato, <ro>falta {0}</ro>'.format(ctc))
                except Exception as ex1:
                    io.e("Error %s al importar %s"%(str(ex1),pluginName),)
            elif TYPE=='DIR':
                dir_plugins.append( pluginName )
            else:
                io.log("<ro>'%s'"%pluginName,"no es un componente valido</ro>")
        ###################################################################################
        for importador in core.importadores:
            modulo = self.modulo(importador)
            resp = self.cumple_dependencias(modulo,core.importadores)
            if resp[0]:
                io.log('<ve>cargado</ve>',init.contrato['nombre'])
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
        ###################################################################################
        print "load modules"
        dir_plugins_mods = []
        for plugin in dir_plugins:
            mod = __import__(plugin)
            dir_plugins_mods.append(mod)
            
        dir_plugins_mods = sorted(dir_plugins_mods, key=lambda mod: mod.contrato['prioridad'])
            
        for mod in dir_plugins_mods:
            ctc = self.cumple_terminos_contractuales(mod)
            if ctc==True:
                core.importadores[ mod.contrato['nombre'] ] = mod
            else:
                io.log(mod.contrato['nombre'],'no cumple el contrato, <ro>falta {0}</ro>'.format(ctc))
            inst = self.instancia(mod)
            try:
                inst.al_finalizar_carga = mod.contrato["al_finalizar_carga"]
                inst.orden = mod.contrato["prioridad"]
                instancias.append( inst )
            except AttributeError as ae:
                io.w( "objeto %s del plugin %s no puede puede ser usado."%(str(inst), mod.contrato['nombre']) )
            except Exception as w:
                raise w
        #####################################
        instancias.reverse()
        for instancia in instancias:
            instancia.al_finalizar_carga(core,instancia)
            
    def modulo(self, importador):
        mod = self.__core.importadores[importador].load_module('__init__')
        return mod
            
    def instancia(self, modulo=None):
        if modulo==None:
            return None
        elif type(modulo)==type(""):
            try:
                inst = self.modulo(modulo).init(self.__core)
            except:
                inst = self.__core.importadores[modulo].init(self.__core)
            return inst
        else:
            return modulo.contrato['inicio'](self.__core)
                
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
            
        






