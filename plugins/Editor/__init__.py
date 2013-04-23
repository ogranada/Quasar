
from PySide import QtCore, QtGui

import os

class Editor(QtGui.QTextEdit):
    
    def __init__(self,core,*args,**kwargs):
        QtGui.QTextEdit.__init__(self,*args,**kwargs)
        self.core = core
        self.setupEditor()
        self.filename = None
        
        
    def setupEditor(self):
        font = QtGui.QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(12)
        self.setFont(font)
        # self.highlighter = Highlighter(self.document())
        self.highlighterCreator = self.core.instancia("resaltador")
        self.highlighter = self.highlighterCreator.getHighlighter( self.document() )
        
    def save(self):
        if not self.filename:
            filename = QtGui.QFileDialog.getSaveFileName(self, 'Guardar Archivo', '.')
            filename = filename[0]
            self.filepath = filename
            self.filename = filename.split(os.sep)[-1]
        else:
            filename = self.filepath
        if filename:
            fname = open(filename, 'w')
            fname.write(self.toPlainText())
            fname.close() 
            
    def open(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        filename = filename[0]
        self.filepath = filename
        self.setText(open(self.filepath,'r').read())
        self.filename = filename.split(os.sep)[-1]
        

def init(core):
    return Editor(core)
    

def alFinalizar(core, instancia):
    pass


contrato = {
    'nombre':'editor',
    'dependencias':['guiStarter','Ventana','resaltador'],
    'librerias':['PySide'],
    'inicio':init,
    'al_finalizar_carga':alFinalizar,
    'prioridad':1.5,
}





