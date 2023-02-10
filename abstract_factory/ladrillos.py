from interfaces import *

class LadrilloN1(ILadrillo):
    def pintarLadrillo(self):
        return "Amarillo"
    def golpesRuptura(self):
        return 1

class LadrilloN2(ILadrillo):
    def pintarLadrillo(self):
        return "Rojo"
    def golpesRuptura(self):
        return 2

class LadrilloN3(ILadrillo):
    def pintarLadrillo(self):
        return "Azul"
    def golpesRuptura(self):
        return 3