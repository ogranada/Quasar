import os, sys
from core import Core
from core import paths


if __name__=='__main__':
    # print os.path.realpath('.')
    # cfpth = os.sep.join([user.home,".quasar","config.cfg"])
    # if os.path.exists(cfpth)
    # os.sep.join([user.home,".quasar","plugins"])
    # cfpth = os.sep.join([user.home,".quasar","config.cfg"])
    paths.set_base( os.path.realpath('..') )
    Core()






