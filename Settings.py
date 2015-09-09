import os

__author__ = 'Estacion1'

class Settings():

    def validatePath(self, path):
        if os.path.isfile(path):
            return True
        else:
            return False
