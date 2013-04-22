
from PySide import QtCore, QtGui


class TabManager(QtGui.QWidget):
    
    def __init__(self,*args,**kwargs):
        QtGui.QWidget.__init__(self,*args,**kwargs)
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
        textEdit = QtGui.QTextEdit(tab)
        gridLayout.addWidget(textEdit, 0, 0, 1, 1)
        self.tabs.append(tab)
        self.tabWidget.addTab(tab, "Nuevo")
        return tab
        
        
    def embed(self,ventana):            
        ventana.makeMenu("archivo")
        ventana.makeAction("nuevo_modulo", label=u"&Nuevo Modulo", shortcut="Ctrl+N", menuname="archivo",separator=0)
        ventana.menuBind("archivo","nuevo_modulo",self.addTab)
        ventana.setCentralWidget(self)
        

def init(core):
    return TabManager()
    

def alFinalizar(core, instancia):
    instancia.embed(core.objetos['Ventana'])


contrato = {
    'nombre':'Editor',
    'dependencias':['guiStarter','Ventana'],
    'librerias':['PySide'],
    'inicio':init,
    'al_finalizar_carga':alFinalizar,
    'prioridad':2,
}





