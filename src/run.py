from core import Core
from core import config_manager as cm
from core import memory as mem
from core import io
from core import plugins

import core
from core.decorators import *

io.LOG = True


    
@validar(str,b=int,c=float)
def func(a,c=0.0,b=1):
    pass

        
if __name__=='__main__':
    c = cm.ConfigFile("config.cfg")
    func('1',2.0,3)
    pm = plugins.PluginManager(Core(),"/home/andres/plugins")





