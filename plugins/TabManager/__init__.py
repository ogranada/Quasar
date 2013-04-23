
from PySide import QtCore, QtGui

global Highlighter


class TabManager(QtGui.QWidget):
    
    def __init__(self,core,*args,**kwargs):
        QtGui.QWidget.__init__(self,*args,**kwargs)
        self.core = core
        self.tabs = []
        self.create_tab_widget()
        self.addTab()
        
    def create_tab_widget(self):
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(self)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        
    def addTab(self):
        tab = QtGui.QWidget()
        tab.setObjectName("tab"+str(len(self.tabs)))
        gridLayout = QtGui.QGridLayout(tab)
        #textEdit = QtGui.QTextEdit(tab)
        textEdit = self.core.instancia("editor")
        gridLayout.addWidget(textEdit, 0, 0, 1, 1)
        tab.editor = textEdit
        self.tabs.append(tab)
        self.tabWidget.addTab(tab, "Nuevo")
        return tab
        
    def save(self):
        self.tabWidget.currentWidget().editor.save()
        if self.tabWidget.currentWidget().editor.filename:
            index = self.tabWidget.currentIndex()
            self.tabWidget.setTabText(index, self.tabWidget.currentWidget().editor.filename)
        
    def openFile(self):
        self.tabWidget.currentWidget().editor.open()
        index = self.tabWidget.currentIndex()
        self.tabWidget.setTabText(index, self.tabWidget.currentWidget().editor.filename)
        
    def embed(self,ventana):     
        ventana.makeMenu("archivo")
        ventana.makeAction("nuevo_modulo", label=u"&Nuevo Modulo", shortcut="Ctrl+N", menuname="archivo",separator=0)
        ventana.menuBind("archivo","nuevo_modulo",self.addTab)
        ventana.makeAction("guardar", label=u"&Guardar", shortcut="Ctrl+S", menuname="archivo",separator=0)
        ventana.menuBind("archivo","guardar",self.save)
        ventana.makeAction("abrir", label=u"&Abrir", shortcut="Ctrl+O", menuname="archivo",separator=0)
        ventana.menuBind("archivo","abrir",self.openFile)
        ventana.setCentralWidget(self)
        

def init(core):
    return TabManager(core)
    

def alFinalizar(core, instancia):
    instancia.embed(core.objetos['Ventana'])


contrato = {
    'nombre':'TabManager',
    'dependencias':['guiStarter','Ventana','editor','resaltador'],
    'librerias':['PySide'],
    'inicio':init,
    'al_finalizar_carga':alFinalizar,
    'prioridad':2,
}





