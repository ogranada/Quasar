
from core import io

class X:
    def __init__(self):
        io.write("hola")



def a(*args):
    return X()
    
def b(*args):
    io.write("adios")


contrato = {
        "nombre":"a",
        "dependencias":[],
        "librerias":[],
        "inicio": a,
        "al_finalizar_carga":b,
        "prioridad":-1
}
