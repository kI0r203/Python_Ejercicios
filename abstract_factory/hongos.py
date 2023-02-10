from interfaces import *

class HongoN1(IHongo):
    def cantidadHongos(self):
        return "aparecen de 2 en 2"

class HongoN2(IHongo):
    def cantidadHongos(self):
        return "aparecen de 4 en 4"
        
class HongoN3(IHongo):
    def cantidadHongos(self):
        return "aparecen de 6 en 6"