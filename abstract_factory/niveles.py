from interfaces import *
from hongos import *
from tortugas import *
from ladrillos import *

class FNivel1(IFabricaNiveles):
    ladrillo = None
    tortuga = None
    hongo = None
    def crearFabrica(self):
        self.hongo = HongoN1()
        self.ladrillo = LadrilloN1()
        self.tortuga = TortugaN1()
    
    def mostrarDetalles(self):
        print(f'Hongos: {self.hongo.cantidadHongos()}\nVelocidad de la Tortuga: {self.tortuga.velocidadTortuga()}\nColor Ladrillo: {self.ladrillo.pintarLadrillo()} y se rompe de {self.ladrillo.golpesRuptura()} golpes')

    def verDificultad(self):
        print("Nivel 1")

class FNivel2(IFabricaNiveles):
    ladrillo = None
    tortuga = None
    hongo = None
    def crearFabrica(self):
        self.hongo = HongoN2()
        self.ladrillo = LadrilloN2()
        self.tortuga = TortugaN2()
    
    def mostrarDetalles(self):
        print(f'Hongos: {self.hongo.cantidadHongos()}\nVelocidad de la Tortuga: {self.tortuga.velocidadTortuga()}\nColor Ladrillo: {self.ladrillo.pintarLadrillo()} y se rompe de {self.ladrillo.golpesRuptura()} golpes')

    def verDificultad(self):
        print("Nivel 2")

class FNivel3(IFabricaNiveles):
    ladrillo = None
    tortuga = None
    hongo = None
    def crearFabrica(self):
        self.hongo = HongoN3()
        self.ladrillo = LadrilloN3()
        self.tortuga = TortugaN3()
    
    def mostrarDetalles(self):
        print(f'Hongos: {self.hongo.cantidadHongos()}\nVelocidad de la Tortuga: {self.tortuga.velocidadTortuga()}\nColor Ladrillo: {self.ladrillo.pintarLadrillo()} y se rompe de {self.ladrillo.golpesRuptura()} golpes')

    def verDificultad(self):
        print("Nivel 3")