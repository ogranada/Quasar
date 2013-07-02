
from PySide import QtCore, QtGui
from core import io


class TabManager(QtGui.QWidget):
    
    def __init__(self,core,*args,**kwargs):
        QtGui.QWidget.__init__(self,*args,**kwargs)
        self.setObjectName("ContentWidget")
        self.core = core
        self.tabs = []
        self.create_tab_widget()
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL("tabCloseRequested(int)"), self.closeTab)
        QtGui.QShortcut("Ctrl+W",self,self.closeActualTab)
        QtGui.QShortcut("Ctrl+Shift+PgDown",self,self.moveTabToRight)
        QtGui.QShortcut("Ctrl+Shift+PgUp",self,self.moveTabToLeft)
        QtGui.QShortcut("Ctrl+PgDown",self,self.goToNextTab)
        QtGui.QShortcut("Ctrl+PgUp",self,self.goToLastTab)
        # self.addTab()
    
    def goToNextTab(self):
        index = self.tabWidget.currentIndex()
        if index < self.tabWidget.count()-1:
            self.tabWidget.setCurrentIndex(index+1)
            
    def goToLastTab(self):
        index = self.tabWidget.currentIndex()
        if index > 0:
            self.tabWidget.setCurrentIndex(index-1)
        
    def moveTabToRight(self):
        index = self.tabWidget.currentIndex()
        if index < self.tabWidget.count()-1:
            widget = self.tabWidget.widget(index)
            self.tabWidget.removeTab(index)
            self.tabWidget.insertTab(index+1,widget,u"")
            self.tabWidget.setCurrentIndex(index+1)
            index = self.tabWidget.currentIndex()
            self.tabWidget.setTabText(index, self.tabWidget.currentWidget().editor.filename)
        
    def moveTabToLeft(self):
        index = self.tabWidget.currentIndex()
        if index > 0:
            widget = self.tabWidget.widget(index)
            self.tabWidget.removeTab(index)
            self.tabWidget.insertTab(index-1,widget,u"")
            self.tabWidget.setCurrentIndex(index-1)
            index = self.tabWidget.currentIndex()
            self.tabWidget.setTabText(index, self.tabWidget.currentWidget().editor.filename)
        
    def closeActualTab(self):
        index = self.tabWidget.currentIndex()
        if index>=0:
            self.closeTab(index)
        
    def closeTab(self, index):
        # print index
        # print dir(self.tabWidget)
        #for i in [x for x in dir( self.tabWidget.widget(index).editor ) if 'close' in x.lower() ]:
        #    print i
        self.tabWidget.removeTab(index)
        
    def create_tab_widget(self):
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(self)
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
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
        tab.editor.setFocus()
        return tab
        
    def save(self):
        self.tabWidget.currentWidget().editor.save()
        if self.tabWidget.currentWidget().editor.filename:
            index = self.tabWidget.currentIndex()
            self.tabWidget.setTabText(index, self.tabWidget.currentWidget().editor.filename)
        
    def openFile(self):
        #if self.tabWidget.currentWidget() != None:
        widget = self.addTab()
        self.tabWidget.setCurrentWidget(widget)
        if self.tabWidget.currentWidget().editor.open():
            index = self.tabWidget.currentIndex()
            self.tabWidget.setTabText(index, self.tabWidget.currentWidget().editor.filename)
            return True
        else:
            self.closeActualTab()
        #else:
        #    self.addTab()
        #    if not self.openFile():
        #        self.tabWidget.removeTab(self.tabWidget.currentIndex())
        
    def embed(self,ventana):
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        [io.write(x) for x in dir(self.gridLayout) if 'setContent' in x]
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
    #instancia.setStyleSheet('''background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(43, 75, 75), stop:1 rgb(86, 150, 150));''')
    #instancia.setStyleSheet('''background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgb(43, 75, 75), stop:1 rgb(86, 150, 150));padding-top:10px''')


contrato = {
    'nombre':'TabManager',
    'dependencias':['guiStarter','Ventana','editor','resaltador'],
    'librerias':['PySide'],
    'inicio':init,
    'al_finalizar_carga':alFinalizar,
    'prioridad':2,
}





