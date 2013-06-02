
from PySide import QtCore, QtGui
import os
from pcef.editors.generic import GenericEditor
from pcef import openFileInEditor
from pcef import saveFileFromEditor

class Editor(GenericEditor):
    
    def __init__(self,core,*args,**kwargs):
        GenericEditor.__init__(self,*args,**kwargs)
        self.core = core
        self.filename = None
        
        self.actionMoveline = QtGui.QAction(self)
        self.actionMoveline.setText("Move Line Down")
        self.actionMoveline.setShortcut("Ctrl+Shift+Down")
        QtCore.QObject.connect(self.actionMoveline, QtCore.SIGNAL("triggered()"), self.TextEditEvent)
        #QtGui.QShortcut("Ctrl+Shift+Down",self,self.TextEditEvent)
        
        self.actionMoveline2 = QtGui.QAction(self)
        self.actionMoveline.setText("Move Line Down")
        self.actionMoveline2.setShortcut("Ctrl+Shift+Up")
        QtCore.QObject.connect(self.actionMoveline2, QtCore.SIGNAL("triggered()"), self.TextEditEvent2)        
        #QtGui.QShortcut("Ctrl+Shift+Down",self,self.TextEditEvent2)
        
        self.codeEdit.addAction(self.actionMoveline)
        self.codeEdit.addAction(self.actionMoveline2)
        
        
        self.codeEdit.contextMenu.removeAction( self.actionMoveline )
        self.codeEdit.contextMenu.removeAction( self.actionMoveline2 )
        
        
    def TextEditEvent(self):
        cursor = self.codeEdit.textCursor()                 # obtiene el cursor
        cursor.beginEditBlock()                             # inicia edicion
        cursor.movePosition(QtGui.QTextCursor.StartOfLine)  # va al inicio de la linea
        cursor.select(QtGui.QTextCursor.LineUnderCursor)    # selecciona la linea
        text = cursor.selectedText()                        # copia el texto de la linea seleccionada
        cursor.removeSelectedText()                         # elimina el texto seleccionado
        cursor.deleteChar()                                 # elimina el siguiente caracter (\n)
        cursor.movePosition(QtGui.QTextCursor.EndOfLine)    # se mueve al fin de la linea
        cursor.insertText('\n'+text)                        # pega el texto copiado
        cursor.endEditBlock()                               # termina edicion
        self.codeEdit.setTextCursor(cursor)                 # establece el cursor
        
    def TextEditEvent2(self):
        cursor = self.codeEdit.textCursor()                 # obtiene el cursor
        cursor.beginEditBlock()                             # inicia edicion
        cursor.movePosition(QtGui.QTextCursor.StartOfLine)  # va al inicio de la linea
        cursor.select(QtGui.QTextCursor.LineUnderCursor)    # selecciona la linea
        text = cursor.selectedText()                        # copia el texto de la linea seleccionada
        cursor.removeSelectedText()                         # elimina el texto seleccionado
        cursor.deletePreviousChar()                         # elimina el anterior caracter (\n)
        cursor.movePosition(QtGui.QTextCursor.StartOfLine)  # se mueve al fin de la linea
        cursor.insertText(text+'\n')                        # pega el texto copiado
        cursor.movePosition(QtGui.QTextCursor.Up)  # se mueve a la linea de arriba
        cursor.endEditBlock()                               # termina edicion
        self.codeEdit.setTextCursor(cursor)                 # establece el cursor

    def __del__(self):
        try:
            del(self.codeEdit)
        except:
            pass
        
    def save(self):
        if not self.filename:
            filename = QtGui.QFileDialog.getSaveFileName(self, 'Guardar Archivo', '.')
            filename = filename[0]
            self.filepath = filename
            self.filename = filename.split(os.sep)[-1]
        else:
            filename = self.filepath
        if filename:
            saveFileFromEditor(self, filename)
            
    def open(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        filename = filename[0]
        if filename:
            self.filepath = filename
            openFileInEditor(self, filename)
            self.filename = filename.split(os.sep)[-1]
            return True
        else:
            return False
        

def init(core):
    return Editor(core)
    

def alFinalizar(core, instancia):
    pass


contrato = {
    'nombre':'editor',
    'dependencias':['guiStarter','Ventana','resaltador'],
    'librerias':['PySide','pcef'],
    'inicio':init,
    'al_finalizar_carga':alFinalizar,
    'prioridad':1.5,
}





