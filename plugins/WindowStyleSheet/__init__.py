

baseStyle = '''QWidget_{
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(74, 63, 61, 255), stop:1 rgba(84, 84, 84, 255));
}
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


def a(core):
    #print dir(core.objetos["App"].app)
    core.objetos["App"].app.setStyleSheet(baseStyle)
    return None
    
def b(core,inst):
    #core.objetos["App"].app.setStyleSheet(baseStyle)
    pass

contrato = {
        "nombre":"WindowStyleSheet",
        "dependencias":["ventana"],
        "librerias":[],
        "inicio": a,
        "al_finalizar_carga":b,
        "prioridad":1.1
}
        
