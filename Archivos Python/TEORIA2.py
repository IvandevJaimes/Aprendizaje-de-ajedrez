from colorama import *
import time
import os
import msvcrt
import sys
RESET="\033[0m"
def t02():
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
            print(Fore.CYAN + Style.BRIGHT + "♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟"+RESET+Fore.LIGHTWHITE_EX+"     Teoría del Ajedrez Nivel 2    "+RESET+Fore.LIGHTCYAN_EX+"♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  " + Style.RESET_ALL)
            print()
            print()
        
        def L():
            print()
            print(Fore.LIGHTMAGENTA_EX+"_____________________________________________________________________________________________________________________________________________________________________"+RESET)
            print()
        
        titulo()
        print_title("Número de Casillas en el Tablero", Fore.GREEN)
        print("""
            | A | B | C | D | E | F | G | H |
            |---|---|---|---|---|---|---|---|
          1 |   |   |   |   |   |   |   |   |
            |---|---|---|---|---|---|---|---|
          2 |   |   |   |   |   |   |   |   |
            |---|---|---|---|---|---|---|---|
          3 |   |   |   |   |   |   |   |   |
            |---|---|---|---|---|---|---|---|
          4 |   |   |   |   |   |   |   |   |
            |---|---|---|---|---|---|---|---|
          5 |   |   |   |   |   |   |   |   |
            |---|---|---|---|---|---|---|---|
          6 |   |   |   |   |   |   |   |   |
            |---|---|---|---|---|---|---|---|
          7 |   |   |   |   |   |   |   |   |
            |---|---|---|---|---|---|---|---|
          8 |   |   |   |   |   |   |   |   |
    """)
        print()
        L()
        slow_print("Un tablero de ajedrez tiene un total de 64 casillas, organizadas en 8 filas y 8 columnas. Esto forma una cuadrícula de 8x8 casillas.\n")
        PCT()
        
        titulo()
        print_title("Lectura de Casillas", Fore.RED)
        print("""
    |  A1 |  B1 |  C1 |  D1 |  E1 |  F1 |  G1 |  H1 |
    
    |  A2 |  B2 |  C2 |  D2 |  E2 |  F2 |  G2 |  H2 |
   
    |  A3 |  B3 |  C3 |  D3 |  E3 |  F3 |  G3 |  H3 |

    |  A4 |  B4 |  C4 |  D4 |  E4 |  F4 |  G4 |  H4 |

    |  A5 |  B5 |  C5 |  D5 |  E5 |  F5 |  G5 |  H5 |
    
    |  A6 |  B6 |  C6 |  D6 |  E6 |  F6 |  G6 |  H6 |
   
    |  A7 |  B7 |  C7 |  D7 |  E7 |  F7 |  G7 |  H7 |
  
    |  A8 |  B8 |  C8 |  D8 |  E8 |  F8 |  G8 |  H8 |
    """)
        print()
        L()
        slow_print("En ajedrez, las casillas se leen con la letra de la columna seguida del número de la fila. Por ejemplo, la casilla en la esquina inferior izquierda se lee como A1.\n")
        PCT()
        
        titulo()
        print_title("Aperturas en Ajedrez", Fore.MAGENTA)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   | ♙ |   |   |   |   |
    | ♙ | ♙ | ♙ |   | ♙ | ♙ | ♙ | ♙ |
    | ♖ | ♘ | ♗ | ♕ | ♔ | ♗ | ♘ | ♖ |
                        
    """)
        print()
        L()
        slow_print("""Las aperturas son las primeras jugadas de la partida y tienen el propósito de desarrollar las piezas y controlar el centro del tablero. 
No son para ganar rápidamente, sino para establecer una posición sólida.\n""")
        PCT()
        
        titulo()
        print_title("Concepto de Jaque", Fore.BLUE)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♔ |   |   |   |
    |   |   |   | / |   |   |   |   |
    |   |   | ♝ |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    """)
        print()
        L()
        slow_print("El jaque ocurre cuando el rey está bajo amenaza de ser capturado en el siguiente movimiento. Debe ser respondido inmediatamente para proteger al rey.\n")
        PCT()
        
        titulo()
        print_title("Concepto de Jaque Mate", Fore.GREEN)
        print("""
    |   |   |   |   |   |   |   |   |
    | ♜ | > | > | > | > | > |   |   |
    |   |   |   |   | ♔ |   |   |   |
    | ♜ | > | > | / | > | > | > |   |
    |   |   | ♝ |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   | ♚ |   |   |   |   |   |   |
    """)
        print()
        L()
        slow_print("El jaque mate se produce cuando el rey está en jaque y no tiene ningún movimiento legal para escapar. Es la forma de ganar una partida de ajedrez.\n")
        PCT()
        
        titulo()
        print_title("Rey Ahogado", Fore.MAGENTA)
        print("""
    |   |   |   |   |   |   |   |   |
    | ♕ |   |   |   |   |   |   |   |
    |   |   |   |   | ♔ |   |   |   |
    | ♕ |   | ♟ |   |   |   | ♟ |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   | ♚ |   |   |   |   |   |   |
    """)
        print()
        L()
        slow_print("El rey ahogado ocurre cuando el rey no está en jaque pero no tiene ningún movimiento legal posible. En este caso, la partida termina en empate.\n")
        PCT()
        
        titulo()
        print_title("Coronación de Peón", Fore.RED)
        print("""
    | ♕ |   |   |   |   |   |   |   |
    | ^ |   |   |   |   |   |   |   |
    | ^ |   |   |   |   |   |   |   |
    | ^ |   |   |   |   |   |   |   |
    | ^ |   |   |   |   |   |   |   |
    | ^ |   |   |   |   |   |   |   |
    | ^ |   |   |   |   |   |   |   |
    | ♙ |   |   |   |   |   |   |   |
    """)
        print()
        L()
        slow_print("La coronación de peón ocurre cuando un peón llega a la última fila del tablero y puede transformarse en cualquier otra pieza, típicamente una dama, torre, alfil o caballo.\n")
        PCT()
        
        titulo()
        print_title("Significado de 'Tablas'", Fore.BLUE)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   | ♚ |   |   |   |   |   |
    | ♔ |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    """)
        print()
        L()
        slow_print("En ajedrez, 'tablas' indica un empate. Puede ocurrir en diversas situaciones como falta de material para dar jaque mate, acuerdo entre los jugadores o repetición de movimientos.\n")
        PCT()
        
        titulo()
        print_title("Captura al Paso", Fore.RED)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   | / |   |   |   |   |
    |   |   | ♙ | ♟ |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    """)
        print()
        L()
        slow_print("La captura al paso permite a un peón capturar a otro peón enemigo que ha avanzado dos casillas desde su posición inicial y se encuentra al lado del peón que realiza la captura.\n")
    
    
    # Execute the theory printing
    print_theory()
