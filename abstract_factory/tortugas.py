from interfaces import *

class TortugaN1(ITortuga):
    def velocidadTortuga(self):
        return "lenta"

class TortugaN2(ITortuga):
    def velocidadTortuga(self):
        return "rapida"
    
class TortugaN3(ITortuga):
    def velocidadTortuga(self):
        return "super rapida"
