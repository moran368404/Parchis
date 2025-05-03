from typing import List
from jugador import Jugador
from ficha import Ficha
from tablero import Tablero
from dado import Dado

class Juego:
    def __init__(self, jugadores: List[Jugador], tablero: Tablero, dado: Dado):
        self.jugadores = jugadores
        self.tablero = tablero
        self.dado = dado
        self.turno_actual = 0
        self.jugador_actual = self.jugadores[self.turno_actual]

    def jugar_turno(self):
        print(f"\nTurno de {self.jugador_actual.nombre}")
        pasos = self.dado.lanzar()
        print(f"{self.jugador_actual.nombre} lanzó un {pasos}")

        # Buscar fichas que se puedan mover
        fichas_movibles = self.jugador_actual.fichas_movibles(pasos)

        if not fichas_movibles:
            print("No hay fichas que se puedan mover.")
            self.cambiar_turno()
            return

        # Por simplicidad, mover la primera ficha posible
        ficha = fichas_movibles[0]

        nueva_casilla = self.tablero.obtener_siguiente_casilla(ficha.casilla_actual, pasos)
        self.tablero.colocar_ficha(ficha, nueva_casilla)
        print(f"Ficha {ficha.id} movida a casilla {nueva_casilla.posicion}")

        # Verificar si ganó
        if self.juego_terminado():
            print(f"¡{self.jugador_actual.nombre} ha ganado!")
        else:
            self.cambiar_turno()

    def cambiar_turno(self):
        self.turno_actual = (self.turno_actual + 1) % len(self.jugadores)
        self.jugador_actual = self.jugadores[self.turno_actual]

    def juego_terminado(self) -> bool:
        return self.jugador_actual.fichas_en_meta()