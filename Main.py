from VistaJuego import VistaJuego
from Juego import Juego
from JuegoPresenter import JuegoPresenter

def ciclo_de_juego():
    vista = VistaJuego()
    juego = Juego()
    presentador = JuegoPresenter(vista, juego)
    presentador.iniciar()

    while True:
        jugador = juego.jugadores[juego.turno_actual]
        vista.mostrar_mensaje(f"\nTurno de {jugador.nombre}")
        input("Presiona Enter para lanzar el dado...")
        resultado = presentador.lanzar_dado()

        ficha_id = int(input(f"Selecciona la ficha (0-3) para mover {resultado} pasos: "))
        if presentador.mover_ficha(jugador, ficha_id, resultado):
            break

if __name__ == "__main__":
    ciclo_de_juego()