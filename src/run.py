
from core import config_manager as cm
from core import memory as mem
from core import io


        
if __name__=='__main__':
    c = cm.ConfigFile("config.cfg")
    print type( c['HOLA'] )
    print mem.get_size( c['HOLA'] )





