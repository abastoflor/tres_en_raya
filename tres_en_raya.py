import os
from tabulate import tabulate
import time


class TicTacToe:
    def __init__(self):
        self.tablero = []
        self.x = """
|  **   **   |
|   ** **    |
|    ***     |
|   ** **    |
|  **   **   |
--------------
        """
        self.o = """
|   *****    |
|  **   **   |
|  **   **   |
|  **   **   |
|   *****    |
--------------
            """
        self.v = """
|            |
|            |
|            |
|            |
|            |
--------------
            """
        self.jugador = self.x
        self.crear_tablero()

    def crear_tablero(self):
        for i in range(3):
            fila = []
            for j in range(3):
                fila.append(self.v)
            self.tablero.append(fila)

    def modificar_tablero(self):
        self.nuevo_tablero = [x for i in self.tablero for x in i]

    def verificar_tablero(self):
        self.modificar_tablero()
        for i in self.nuevo_tablero:
            if i == self.v:
                return True
        return False

    def elegir_casilla(self):
        while True:
            try:
                self.casilla = int(
                    input(
                        "Elija una casilla (del 1 al 9) para jugar. Otro para salir: "
                    )
                )
                if self.casilla in range(1, 10):
                    if self.nuevo_tablero[self.casilla - 1] != self.v:
                        print("Casilla ocupada...")
                    else:
                        print("")
                        return self.casilla - 1
                else:
                    print("Juego Terminado ...")
                    break
            except:
                print("")

    def cambiar_jugador(self):
        if self.jugador == self.x:
            self.jugador = self.o
        else:
            self.jugador = self.x
        return self.jugador

    def ganador(self):
        ganador = None
        for i in range(len(self.tablero)):
            ganador = True
            for j in range(len(self.tablero)):
                if self.tablero[i][j] != self.jugador:
                    ganador = False
                    break
            if ganador:
                return ganador

        for i in range(len(self.tablero)):
            ganador = True
            for j in range(len(self.tablero)):
                if self.tablero[j][i] != self.jugador:
                    ganador = False
                    break
            if ganador:
                return ganador

        ganador = True
        for i in range(len(self.tablero)):
            if self.tablero[i][i] != self.jugador:
                ganador = False
                break
        if ganador:
            return ganador

        ganador = True
        for i in range(len(self.tablero)):
            if self.tablero[i][len(self.tablero) - 1 - i] != self.jugador:
                ganador = False
                break
        if ganador:
            return ganador
        return False

    def jugar(self):
        while True:
            if self.ganador():
                os.system("clear")
                print(
                    f"""
                      {self.jugador}   HA GANADO!! """
                )
                print()
                print(tabulate(self.tablero))
                time.sleep(4)
                os.system("clear")
                self.tablero.clear()
                self.crear_tablero()
                print("Juego nuevo...")
                print(tabulate(self.tablero))
            if self.verificar_tablero():
                try:
                    self.c = self.elegir_casilla()
                    self.simb = self.cambiar_jugador()
                    self.nuevo_tablero[self.c] = self.simb
                    self.tablero = [
                        self.nuevo_tablero[i : i + 3]
                        for i in range(0, len(self.nuevo_tablero), 3)
                    ]
                    os.system("clear")
                    print(tabulate(self.tablero))
                except:
                    break
            else:
                os.system("clear")
                self.tablero.clear()
                self.crear_tablero()
                print("Juego nuevo...")
                print(tabulate(self.tablero))


t1 = TicTacToe()
print(tabulate(t1.tablero))
t1.jugar()
