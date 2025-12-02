from colorama import *
import time
import os
import msvcrt
import sys
import json
RESET="\033[0m"



def t04():

    def PCT ():
            
            print()
            print()
            print()
            for char in "Presiona cualquier tecla para continuar... ":
                print(char, end='', flush=True),time.sleep(0.001)
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
            print(Fore.CYAN + Style.BRIGHT + "♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟"+RESET+Fore.LIGHTWHITE_EX+"     Teoría del Ajedrez Nivel 4    "+RESET+Fore.LIGHTCYAN_EX+"♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  " + Style.RESET_ALL)
            print()
            print()

        def L():
            print()
            print(Fore.LIGHTMAGENTA_EX+"_____________________________________________________________________________________________________________________________________________________________________"+RESET)
            print()
        titulo()
        print_title("Ahogado de Fort Knox", Fore.GREEN)
        print("""
    |   |   |   |   |   |   |   |   |
    |   | ♙ |   |   |   | ♙ |   |   |
    | ♙ | ♘ | ♙ |   | ♙ | ♘ | ♙ |   |
    | ♖ |   |   |   |   |   |   | ♖ |
    | ♗ |   | ♔ |   |   | ♔ |   | ♗ |
    |   | ♙ | ♘ |   | ♙ | ♘ | ♙ |   |
    |   | ♙ |   |   |   | ♙ |   |   |
    |   |   |   |   |   |   |   |   |
    """)
        print()
        L()
        slow_print("""El 'ahogado de Fort Knox' es una táctica avanzada en la que el rey enemigo se encuentra completamente rodeado por sus propias piezas, impidiéndole moverse y, en consecuencia, no puede escapar de un jaque mate inminente. 
Este patrón es una variante más restringida del jaque mate por ahogado, donde las piezas defensoras no están solo bloqueando la salida, sino también bloqueando la propia captura de las piezas que impedirían el jaque mate.\n""")
        PCT()
        titulo()
        print_title("Iniciativa", Fore.RED)
        print("""
    | ♜ |   | ♝ |   | ♛ | ♝ |   | ♜ |
    | ♟ | ♟ | ♟ | ♟ |   | ♟ | ♟ | ♟ |
    |   |   |   |   | ♟ |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   | ♙ |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    | ♙ | ♙ | ♙ |   | ♙ | ♙ | ♙ | ♙ |
    | ♖ | ♘ | ♗ | ♕ | ♔ | ♗ | ♘ | ♖ |
    """)
        print()
        L()
        slow_print("""En ajedrez, tener la 'iniciativa' significa que un jugador tiene la capacidad de dictar el ritmo y el flujo del juego. 
Esto se logra generalmente mediante jugadas activas que amenazan o generan complicaciones para el adversario, forzándolo a responder en lugar de ejecutar su propio plan. 
Mantener la iniciativa permite a un jugador controlar la partida y crear oportunidades tácticas y estratégicas.\n""")
        PCT()
        titulo()
        print_title("Cegada", Fore.MAGENTA)
        print("""
    |   |   |   |   | ♜ |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♗ |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    | ♗ |   |   |   |   |   |   |   |
    | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ |
    | ♖ | ♘ | ♗ | ♕ | ♔ | ♗ | ♘ | ♖ |
    """)
        print()
        L()
        slow_print("""El término 'cegada' en ajedrez se refiere a una maniobra en la que un jugador sacrifica una pieza o hace una jugada que aparentemente es desfavorable para desviar la atención del oponente de una amenaza más importante o para abrir nuevas oportunidades. 
Esta táctica puede llevar a un desequilibrio en la partida, creando oportunidades para combinaciones tácticas y estrategias a largo plazo.\n""")
        PCT()
        titulo()
        print_title("Remate", Fore.BLUE)
        print("""
    |   |   |   |   | ♚ |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♖ |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♙ |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♔ |   |   |   |
    """)
        print()
        L()
        slow_print("""Un 'remate' en ajedrez se refiere a una combinación de movimientos finales diseñada para asegurar el jaque mate. Es una serie de jugadas que llevan al oponente a una posición en la que no puede evitar el jaque mate en el siguiente movimiento. 
Los remates suelen ser muy calculados y dependen de la precisión en la ejecución de las jugadas finales.\n""")
        PCT()
        titulo()
        print_title("Ataque de Karpov", Fore.GREEN)
        print("""
    | ♜ |   |   |   | ♚ |   |   | ♜ |
    |   | ♟ |   | ♟ |   | ♟ |   | ♟ |
    | ♟ |   | ♟ |   |   |   | ♟ |   |
    |   |   |   |   | ♙ |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   | ♗ |   |   |   |   |
    | ♙ |   |   |   |   | ♙ |   | ♙ |
    | ♖ | ♘ | ♗ |   | ♔ |   |   | ♖ |
    """)
        print()
        L()
        slow_print("""El 'ataque de Karpov' es una estrategia inspirada en el estilo de juego de Anatoly Karpov, conocido por su enfoque metódico y preciso en el ajedrez. 
Este ataque se caracteriza por una presión constante y un control detallado del tablero, donde el jugador mantiene una serie de amenazas y presiones que limitan las opciones del oponente. 
Karpov usaba esta estrategia para ganar ventaja poco a poco y aprovechar los errores de sus rivales.\n""")
        PCT()
        titulo()
        print_title("Sacrificio de Calidad", Fore.RED)
        print("""
    | ♖ |   |   |   | ♚ |   |   | ♜ |
    | ♟ |   | ♟ | ♟ |   | ♟ |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   | ♗ |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    | ♙ | ♙ | ♙ |   |   | ♙ | ♙ | ♙ |
    | ♖ | ♘ | ♗ | ♕ | ♔ | ♗ | ♘ | ♖ |
    """)
        print()
        L()
        slow_print("""Un 'sacrificio de calidad' en ajedrez es una táctica en la que un jugador sacrifica una pieza de mayor valor, generalmente una torre o un alfil, para obtener una posición más ventajosa, abrir líneas de ataque
 o crear desequilibrio en la posición del oponente. A menudo, este sacrificio busca crear una ventaja estratégica significativa que compense la pérdida material.\n""")
        PCT()
        titulo()
        print_title("Zugzwang", Fore.MAGENTA)
        print("""
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♚ |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♘ |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   | ♔ |   |   |   |
    """)
        print()
        L()
        slow_print("""El término 'zugzwang' se refiere a una situación en la que un jugador se ve obligado a realizar un movimiento que empeora su posición. En esta circunstancia, cualquier jugada que haga deteriorará su situación, 
lo que puede ser aprovechado por el adversario para obtener una ventaja decisiva.\n""")
        PCT()
        titulo()
        print_title("Sobrecarga", Fore.BLUE)
        print("""
    | ♜ |   |   |   |   |   |   | ♜ |    |
    | ♟ | ♟ | ♟ | ♟ | ♚ | ♟ | ♟ | ♟ |
    |   |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |   | 
    |   |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |   |
    | ♙ | ♙ | ♙ | ♙ |   | ♙ | ♙ | ♙ |
    | ♖ | ♘ | ♗ | ♕ |   | ♗ | ♘ | ♖ |
    """)
        print()
        L()
        slow_print("""La 'sobrecarga' en ajedrez ocurre cuando una pieza está asignada para defender varias amenazas simultáneamente, lo que puede sobrecargar su capacidad de defender efectivamente. 
Como resultado, esta pieza puede ser capturada o se puede debilitar la posición del jugador que la controla. La sobrecarga puede ser una táctica útil para explotar debilidades en la posición del oponente.\n""")
        PCT()
        titulo()
        print_title("Partida de Correspondencia", Fore.GREEN)
        print("""
    |   | ♛ |   | ♚ |   |   | ♜ |
    | ♟ | ♟ | ♟ |   | ♟ | ♟ | ♟ |
    |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |
    | ♙ | ♙ | ♙ |   | ♙ | ♙ | ♙ |
    | ♖ | ♘ | ♗ | ♕ | ♔ | ♗ | ♘ | 
    """)
        print()
        L()
        slow_print("""Una 'partida de correspondencia' es un formato de juego donde los jugadores se enfrentan a través de correspondencia postal o electrónica, con un tiempo prolongado para pensar y responder cada movimiento. 
Este formato permite a los jugadores analizar profundamente cada jugada, planificar estrategias complejas y considerar las consecuencias a largo plazo de sus decisiones.\n""")
        PCT()
        titulo()
        print_title("Elo", Fore.RED)
        print("""
    | ♜ |   |   |   | ♚ |   |   | ♜ |
    | ♟ | ♟ | ♟ | ♟ | ♛ | ♟ | ♟ | ♟ |
    |   |   |   |   |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    |   |   |   | ♔ |   |   |   |   |
    |   |   |   |   |   |   |   |   |
    | ♙ | ♙ | ♙ |   |   | ♙ | ♙ | ♙ |
    | ♖ | ♘ | ♗ | ♕ |   | ♗ | ♘ | ♖ |
    """)
        print()
        L()
        slow_print("""El sistema de puntuación 'Elo' es un método para calcular el nivel de habilidad de los jugadores de ajedrez, desarrollado por Arpad Elo. 
La puntuación Elo se basa en el rendimiento de los jugadores en partidas, ajustando sus calificaciones en función de los resultados y la fuerza de sus oponentes. 
Es utilizado en torneos y competiciones para determinar la clasificación y comparar las habilidades de los jugadores a nivel internacional.\n""")

    print_theory()

