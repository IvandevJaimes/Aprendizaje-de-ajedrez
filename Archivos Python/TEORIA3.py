
from colorama import *
import time
import os
import msvcrt
import sys
import json
from NIVEL1 import *
RESET="\033[0m"
init(autoreset=True)


def t03():

    def L():
            print()
            print(Fore.LIGHTMAGENTA_EX+"_____________________________________________________________________________________________________________________________________________________________________"+RESET)
            print()

    def PCT ():
            
            print()
            print()
            print()
            for char in "Presiona cualquier tecla para continuar... ":
                print(char, end='', flush=True),time.sleep(0.001)
            msvcrt.getch()
            os.system('cls' if os.name == 'nt' else 'clear')
            print()

    def print_title(title, color=Fore.YELLOW):
        print(color + Style.BRIGHT + title)
        print(Fore.WHITE + "-" * len(title))

    def slow_print(text, delay=0.02):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()  

    def print_theory_level_3():
        def titulo():
                
                print(Fore.CYAN + Style.BRIGHT + "♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟"+RESET+Fore.LIGHTWHITE_EX+"     Teoría del Ajedrez Nivel 3    "+RESET+Fore.LIGHTCYAN_EX+"♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  " + Style.RESET_ALL)
                print()
        
        titulo()
        print_title("Jaque Doble", Fore.BLUE)
        print("""
    | ♖ |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♔ |   |   |   |
    |   |   |   |   |   |   |   |   |
    | ♗ |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    """)
        slow_print("Un jaque doble ocurre cuando dos piezas atacan al rey simultáneamente, y este no puede moverse para escapar de ambos ataques.")
        slow_print("Esto fuerza al rey a reaccionar de manera inmediata y a menudo resulta en la pérdida de material significativo para el defensor.\n")
        L()
        PCT()
        titulo()
        print_title("Desviación", Fore.RED)
        print("""
    | ♖ |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♔ |   |   |   |
    |   |   |   |   | ↓ |   |   |   |
    | ♗ |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    """)
        slow_print("Una desviación es un movimiento que aleja una pieza de su función defensiva, exponiéndola a ser capturada o comprometiendo la posición del jugador.")
        slow_print("Es una técnica táctica utilizada para explotar debilidades en la defensa del oponente.\n")
        L()
        PCT()
        titulo()
        print_title("Cadeneta", Fore.MAGENTA)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♔ |   |   |   |
    |   |   |   |   | ↓ |   |   |   |
    |   |   |   |   | ♖ |   |   |   |
    |   |   |   |   | ↓ |   |   |   |
    |   |   |   |   | ♖ |   |   |   |
    """)
        slow_print("La cadeneta es una serie de jugadas consecutivas en las que una pieza ataca repetidamente al rey contrario, generalmente con la intención de forzar un jaque mate o ganar material.")
        slow_print("Es una táctica avanzada utilizada para mantener la presión sobre el rey enemigo.\n")
        L()
        PCT()
        titulo()
        print_title("Opuesto de la Oposición", Fore.BLUE)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♔ |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♔ |   |   |   |
    """)
        slow_print("El opuesto de la oposición es una situación en la que los reyes se enfrentan en casillas adyacentes con un número impar de casillas entre ellos.")
        slow_print("Esto garantiza que el jugador que no tiene el turno pueda avanzar y tomar control del territorio.\n")
        L()
        PCT()
        titulo()
        print_title("Partida a la Italiana", Fore.GREEN)
        print("""
    | ♖ | ♘ | ♗ | ♔ | ♗ | ♘ | ♖ | ♙ |
    | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ |
    | ♖ | ♘ | ♗ | ♔ | ♗ | ♘ | ♖ | ♙ |
    """)
        slow_print("Una partida a la italiana es una partida caracterizada por un juego agresivo y táctico desde las primeras jugadas.")
        slow_print("Ambos jugadores buscan activamente oportunidades tácticas y sacrificios para obtener ventaja.\n")
        L()
        PCT()
        titulo()
        print_title("Jugada Intermedia", Fore.RED)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♔ |   |   |   |
    |   |   |   |   | ↓ |   |   |   |
    |   |   |   |   | ♙ |   |   |   |
    |   |   |   |   | ↓ |   |   |   |
    |   |   |   |   | ♖ |   |   |   |
    """)
        slow_print("Una jugada intermedia, también conocida como 'intermezzo' o 'zwischenzug', es un movimiento sorpresivo que altera el curso esperado de la partida.")
        slow_print("A menudo aprovecha una oportunidad táctica en medio de una secuencia de jugadas.\n")
        L()
        PCT()
        titulo()
        print_title("Ataque Doble", Fore.MAGENTA)
        print("""
    | ♖ |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♔ |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    | ♗ |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    """)
        slow_print("Un ataque doble es un ataque en el que dos piezas cooperan para amenazar una misma casilla o pieza enemiga.")
        slow_print("Forza al oponente a elegir cuál amenaza contrarrestar, generalmente resultando en la pérdida de material.\n")
        L()
        PCT()
        titulo()
        print_title("Miniatura", Fore.YELLOW)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♔ |   |   |   |
    |   |   |   |   | ↓ |   |   |   |
    |   |   |   |   | ♙ |   |   |   |
    |   |   |   |   | ↓ |   |   |   |
    |   |   |   |   | ♖ |   |   |   |
    |   |   |   |   | ↓ |   |   |   |
    |   |   |   |   | ♖ |   |   |   |
    """)
        slow_print("Una miniatura es una partida de ajedrez en la que se produce un mate en menos de 15 movimientos.")
        slow_print("Generalmente es el resultado de errores tácticos graves por parte de uno de los jugadores.\n")
        L()
        PCT()
        titulo()
        print_title("Perpetua", Fore.BLUE)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♔ |   |   |   |
    |   |   |   |   | ↔ |   |   |   |
    |   |   |   |   | ♖ |   |   |   |
    """)
        slow_print("Una perpetua es una situación en la que un jugador repite una secuencia de jugadas sin avanzar en la partida.")
        slow_print("Esto resulta en un empate por repetición, ya que ninguna de las partes puede progresar.\n")
        L()
        PCT()
        titulo()
        print_title("Tablas por Falta de Material", Fore.GREEN)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♔ |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♔ |   |   |   |
    """)
        slow_print("Las tablas por falta de material se producen cuando ambos jugadores tienen una cantidad igual de material y ninguno puede forzar un jaque mate.")
        slow_print("Esto ocurre típicamente cuando solo quedan los reyes en el tablero.\n")

        
    print_theory_level_3()

