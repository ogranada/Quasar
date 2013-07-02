# -*- coding:utf-8 -*-
from PySide import QtCore, QtGui
from core import io

from DarkStyle import qdarkstyle


baseStyle = '''

QTabBar::tab{
    border-top-right-radius: 10px 28px;
    border-top-left-radius: 10px 28px;
    padding : 0 25px 0 10px;
    margin : 0 1px 0 -5px;
    position:relative;
    border: 1px solid #aaa;
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(74, 63, 61, 255), stop:1 rgba(84, 84, 84, 255));
    color:#fff;
    left:5px;
    height:26px;
}
QTabBar::tab:selected{
    border-top-right-radius: 10px 28px;
    border-top-left-radius: 10px 28px;
    padding : 0 25px 0 10px;
    margin : 0 1px 0 -5px;
    position:relative;
    /*border: 1px solid #fff;*/
    border-bottom: 1px solid; /*1px solid #fff;*/
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(128, 133, 152, 255), stop:1 rgba(84, 84, 84, 255));
    color:#fff;
    left:5px;
    height:26px;
}

'''


class StyleSelector:

    estilos = {"Dark Style":qdarkstyle.load_stylesheet(pyside=True), "Light And Shadow":baseStyle}

    def __init__(self, core):
        self.core = core
        self.ventana = core.objetos['Ventana']
        self.core.objetos["App"].app.setStyleSheet(self.estilos["Light And Shadow"])

    def select(self):
        data = QtGui.QInputDialog.getItem(self.ventana, "selección de estilo", "Seleccione el estilo que desea", [x for x in self.estilos.keys()], editable=False)
        if data[1]:
            self.core.objetos["App"].app.setStyleSheet(self.estilos[data[0]])


def a(core):
    return StyleSelector(core)
    
def b(core,instance):
    ventana = core.objetos['Ventana']
    ventana.makeMenu("ventana")
    ventana.makeAction("estilo", label=u"&Estilo", shortcut="Ctrl+Y", menuname="ventana",separator=0)
    ventana.menuBind("ventana","estilo",instance.select)


contrato = {
        "nombre":"DarkStyle",
        "dependencias":[],
        "librerias":[],
        "inicio": a,
        "al_finalizar_carga":b,
        "prioridad":1.1
}
        
