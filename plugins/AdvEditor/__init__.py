
from PySide import QtCore, QtGui
import os
try:
    from pcef.editors.generic import GenericEditor # old pcef
    from pcef import openFileInEditor
    from pcef import saveFileFromEditor
except:
    from pcef.core import QGenericCodeEdit as GenericEditor

from core import io

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
        
        try:
            self.codeEdit.addAction(self.actionMoveline)
            self.codeEdit.addAction(self.actionMoveline2)
            
            
            self.codeEdit.contextMenu.removeAction( self.actionMoveline )
            self.codeEdit.contextMenu.removeAction( self.actionMoveline2 )
            def hola(*a):
                io.write(a)
            self.actionCur = QtGui.QAction(self)
            self.actionCur.setText("Cursor Event")
            self.actionMoveline2.setShortcut("Ctrl+LeftClick")
            QtCore.QObject.connect(self.actionCur, QtCore.SIGNAL("triggered()"), hola)
            #QtGui.QShortcut("Ctrl+Shift+Down",self,self.TextEditEvent)
            self.codeEdit.addAction(self.actionCur)
        except:
            self.codeEdit = self
            self.addAction(self.actionMoveline)
            self.addAction(self.actionMoveline2)
            
            
            self.contextMenu.removeAction( self.actionMoveline )
            self.contextMenu.removeAction( self.actionMoveline2 )
            def hola(*a):
                io.write(a)
            self.actionCur = QtGui.QAction(self)
            self.actionCur.setText("Cursor Event")
            self.actionMoveline2.setShortcut("Ctrl+LeftClick")
            QtCore.QObject.connect(self.actionCur, QtCore.SIGNAL("triggered()"), hola)
            #QtGui.QShortcut("Ctrl+Shift+Down",self,self.TextEditEvent)
            self.addAction(self.actionCur)


        
        
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
            try:
                saveFileFromEditor(self, filename)
            except:
                self.saveFile(filename)
            
    def open(self):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '.')
        filename = filename[0]
        if filename:
            self.filepath = filename
            try:
                openFileInEditor(self, filename)
            except:
                self.openFile(filename)
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





