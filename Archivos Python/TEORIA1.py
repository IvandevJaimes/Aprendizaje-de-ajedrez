from colorama import *
import time
import os
import msvcrt
import sys
import json
RESET="\033[0m"



def t01():
    def PCT():
        print()
        for char in "Presiona cualquier tecla para continuar... ":
            print(char, end='', flush=True)
            time.sleep(0.001)
        msvcrt.getch()
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
    
    def LIMPIAR():
        sys.stdout.write('\033[F\033[K')
    
    init(autoreset=True)
    
    def print_title(title, color=Fore.YELLOW):
        print(color + Style.BRIGHT + title)
        print(Fore.WHITE + "-" * len(title))
    
    def slow_print(text, delay=0.02):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()  
    
    def print_theory():
        def titulo():
            print()
            print(Fore.CYAN + Style.BRIGHT + "♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟"+RESET+Fore.LIGHTWHITE_EX+"     Teoría del Ajedrez Nivel 1    "+RESET+Fore.LIGHTCYAN_EX+"♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  " + Style.RESET_ALL)
            print()
            print()
        




        def L():
            print()
            print(Fore.LIGHTMAGENTA_EX+"_____________________________________________________________________________________________________________________________________________________________________"+RESET)
            print()

        titulo()
        print_title("AJEDREZ", Fore.GREEN)
        
        print("""
    | ♖ | ♘ | ♗ | ♔ | ♕ | ♗ | ♘ | ♖ |
    | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ |        
    |   |   |   |   |   |   |   |   |      
    |   |   |   |   |   |   |   |   |      
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |      
    | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ |
    | ♜ | ♞ | ♝ | ♚ | ♛ | ♝ | ♞ | ♜ | 
              

        ♟ \ ♙ ------> Peón
              
        ♝ \ ♗ ------> Alfil
              
        ♞ \ ♘ ------> Caballo
              
        ♚ \ ♔ ------> Rey
              
        ♛ \ ♕ ------> Reina
              
        ♜ \ ♖ ------> Torre
""")
        print()
        slow_print("""El Ajdrez en un juego por turnos de esrategia que se juega haitualmente de a dos personas, el talero cuenta con casillas negras y blancas donde si situan las piezas, cada jugador cunenta con 16 pieezas cada uno:\n""")
        
                     

        L()
        PCT()



        titulo()
        print_title("Movimiento del Peón", Fore.GREEN)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    | ^ |   |   |   |   |   |   |   |
    | ^ | ^ |   |   |   |   |   |   |
    | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ |
    |   |   |   |   |   |   |   |   |
    """)
        print()
        L()
        slow_print("""El peón se mueve normalmente una casilla hacia adelante en su turno. Sin embargo, en su primer movimiento, tiene la opción de avanzar dos casillas hacia adelante. 
Esta capacidad de avanzar dos casillas solo está disponible para su primer movimiento desde su posición inicial.\n""")
        PCT()
        
        titulo()
        print_title("Movimiento de la Torre", Fore.RED)
        print("""
    |   |   |   |   |   |   |   |   |
    | ^ |   |   |   |   |   |   |   |
    | ^ |   |   |   |   |   |   |   |
    | ^ |   |   |   |   |   |   |   |
    | ^ |   |   |   |   |   |   |   |
    | ^ |   |   |   |   |   |   |   |
    | ^ |   |   |   |   |   |   |   |
    | ♖ | > | > | > | > | > | > | > |
    """)
        print()
        L()
        slow_print("""La torre se mueve en líneas rectas, tanto horizontalmente como verticalmente, cualquier número de casillas. 
No puede moverse en diagonal ni saltar sobre otras piezas.\n""")
        PCT()
        
        titulo()
        print_title("Movimiento del Caballo", Fore.MAGENTA)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   | < | ^ |   |   |   |
    |   |   |   |   | ^ |   |   |   |
    |   |   |   |   | ♞ |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    """)
        print()
        L()
        slow_print("""El caballo se mueve en forma de 'L', que consiste en mover dos casillas en una dirección (horizontal o vertical) 
y luego una casilla en perpendicular a esa dirección. Es la única pieza que puede saltar sobre otras piezas en su camino.\n""")
        PCT()
        
        titulo()
        print_title("Movimiento de la Reina", Fore.BLUE)
        print("""
    |   |   |   | ^ |   |   |   |   |
    |   |   |   | ^ |   |   |   |   |
    |   |   |   | ^ |   |   |   |   |
    |   |   |   | ^ |   |   |   | / |
    |   |   |   | ^ |   |   | / |   |
    |   |   |   | ^ |   | / |   |   |
    |   |   |   | ^ | / |   |   |   |
    | < | < | < | ♕ |   |   |   |   |
    """)
        print()
        L()
        slow_print("""La reina puede moverse en cualquier dirección (horizontal, vertical o diagonal) y puede cubrir cualquier número de casillas en esa dirección. 
Esto la convierte en una de las piezas más poderosas del tablero.\n""")
        PCT()
        
        titulo()
        print_title("Movimiento del Rey", Fore.GREEN)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   | \ | ^ | / |   |   |
    |   |   |   | < | ♔ | > |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    """)
        print()
        L()
        slow_print("El rey se mueve una casilla en cualquier dirección: horizontal, vertical o diagonal. Es crucial proteger al rey en todo momento para evitar el jaque mate.\n")
        PCT()
        
        titulo()
        print_title("Movimiento del Alfil", Fore.RED)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    | \ |   |   |   |   |   |   |   |
    |   | \ |   |   |   |   |   | / |
    |   |   | \ |   |   |   | / |   |
    |   |   |   | \ |   | / |   |   |
    |   |   |   |   | ♗ |   |   |   |
    |   |   |   |   |   |   |   |   |
    """)
        print()
        L()
        slow_print("""El alfil se mueve exclusivamente en diagonal y puede recorrer cualquier número de casillas en esa dirección. 
Cada alfil comienza en un color de casilla y siempre se mantiene en ese color durante toda la partida.\n""")
        PCT()
        
        titulo()
        print_title("Primer Movimiento del Peón", Fore.MAGENTA)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   | ^ |   |   |   |   |   |   |
    |   | ^ |   |   |   |   |   |   |
    | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ |
    """)
        print()
        L()
        slow_print("En su primer movimiento, el peón puede avanzar dos casillas hacia adelante. Después de su primer movimiento, solo puede avanzar una casilla por turno.\n")
        PCT()
        
        titulo()
        print_title("Salto del Caballo", Fore.BLUE)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   | < | ^ |   |   |   |
    |   |   |   |   | ♙ |   |   |   |
    |   |   |   |   | ♞ |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    """)
        print()
        L()
        slow_print("El caballo puede saltar sobre otras piezas en su camino gracias a su movimiento en forma de 'L'. Esto le permite superar obstáculos y atacar piezas que no están directamente en su camino.\n")
        PCT()
        
        titulo()
        print_title("Objetivo del Ajedrez", Fore.GREEN)
        print("""
    |   | ♕ | > | > | ♔ |   |   |   |
    | ♕ | > | > | > | > | > | > |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    """)
        print()
        L()
        slow_print("""El objetivo principal del ajedrez es colocar al rey del oponente en una posición de jaque mate, donde está amenazado y no tiene movimientos legales para escapar. 
Capturar todas las piezas del oponente no es el objetivo principal, sino asegurar la victoria mediante el jaque mate.\n""")
        PCT()
        
        titulo()
        print_title("Color de las Piezas para el Primer Movimiento", Fore.RED)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   | ♞ |   |   |   |   |   |   |
    """)
        print()
        L()
        slow_print("""Al inicio de una partida de ajedrez, las piezas blancas siempre mueven primero. 
Este es un estándar en todas las partidas de ajedrez y está diseñado para darle una ligera ventaja a las blancas.\n""")


    
    
    print_theory()
   










