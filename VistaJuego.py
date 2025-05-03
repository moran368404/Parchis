from Tablero import Tablero
from Dado import Dado

class VistaJuego:
    def mostrar_tablero(self, tablero: Tablero):
        print("\nTablero:")
        for i, casilla in enumerate(tablero.casillas):
            if casilla.fichas:
                fichas_ids = ', '.join(str(f.id) for f in casilla.fichas)
                print(f"Casilla {i}: {fichas_ids}")

    def mostrar_dado(self, resultado: int):
        print(f"Dado: {resultado}")

    def mostrar_mensaje(self, mensaje: str):
        print(mensaje)

    def actualizar_tablero(self):
        pass  # Podría implementarse en interfaz gráfica

