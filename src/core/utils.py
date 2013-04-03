#!/usr/bin/python
# -*- coding:utf-8 -*-

class Nodo:

    def __init__(self,nombre, valor):
        self.nombre = nombre
        self.valor = valor
        self.nombres_dependencias = []
        self.dependencias = {}
        
    def add(self, nombre, valor=None):
        self.nombres_dependencias.append(nombre)
        if valor!=None:
            self.dependencias[nombre] = valor
            
    def verificar_dependencias_faltantes(self):
        faltantes = []
        for dep in self.nombres_dependencias:
            if not self.dependencias.has_key(dep):
                faltantes.append(dep)
        return faltantes


