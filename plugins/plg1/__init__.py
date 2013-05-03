

class X:
    def __init__(self):
        print "hola"



def a(*args):
    return X()
    
def b(*args):
    print "adios"


contrato = {
        "nombre":"a",
        "dependencias":[],
        "librerias":[],
        "inicio": a,
        "al_finalizar_carga":b,
        "prioridad":-1
}
        
