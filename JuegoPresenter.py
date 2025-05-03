from Jugador import Jugador
from Tablero import Tablero
from Dado import Dado

class JuegoPresenter:
    def __init__(self, jugadores : list[Jugador], tablero: Tablero, dado: Dado):
        self.jugadores = jugadores
        self.tablero = tablero
        self.dado = dado
        self.turnoActual = 0

    def iniciarJuego(self):
        print("Comenzando el juego")

    def lanzar_Dado(self):
        print("Lanzando dado...")

    def mover_ficha(self):
        print("Moviendo ficha...")

    def verificar_Ganador(self):
        print("Verificando ganador...")

    def siguiente_turno(self):
        print("Que?")