from Tablero import Tablero
from Dado import Dado

class VistaJuego:
    def __init__(self, tablero: Tablero, dado: Dado):
        self.tablero = tablero
        self.dado = dado

    def mostrar_Tablero(self):
        print("Imprimiendo tablero")

    def mostrar_Dado(self):
        print("Mostrando Dado")

    def mostrar_mensaje(self):
        print("Mostrando Mensaje")

    def actualizar_tablero(self):
        print("Actualizado!")

