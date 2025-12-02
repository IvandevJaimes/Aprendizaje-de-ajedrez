from colorama import *
import time
import os
import msvcrt
import sys
RESET="\033[0m"

def t05():

    def PCT():
     

        print()
        print()
        print()
        for char in "Presiona cualquier tecla para continuar... ":
            print(char, end='', flush=True)
            time.sleep(0.001)
        msvcrt.getch()
        os.system('cls' if os.name == 'nt' else 'clear')
        print()

    def LIMPIAR():
        
        sys.stdout.write('\033[F\033[K')   

  

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
            print(Fore.CYAN + Style.BRIGHT + "♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟"+RESET+Fore.LIGHTWHITE_EX+"     Teoría del Ajedrez Nivel 5    "+RESET+Fore.LIGHTCYAN_EX+"♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  ♟  " + Style.RESET_ALL)
            print()
            print()

        def L():
            print()
            print(Fore.LIGHTMAGENTA_EX+"_____________________________________________________________________________________________________________________________________________________________________"+RESET)
            print()

        titulo()
        
        print_title("Origen del Ajedrez", Fore.GREEN)
        slow_print(
            """El ajedrez, conocido inicialmente como 'chaturanga', tiene sus raíces en la India alrededor del siglo VI d.C. Este antiguo juego, jugado sobre un tablero de 8x8 
casillas, era una representación simbólica de las batallas y estrategias militares. El 'chaturanga' se jugaba con cuatro tipos de piezas: 
infantería (peones), caballería (caballos), elefantes (alfiles) y carros de guerra (torres), cada uno con movimientos específicos. 
A medida que el juego se extendió a Persia, donde se convirtió en 'shatranj', sus reglas y piezas evolucionaron hasta adoptar la forma que conocemos hoy. 
La llegada del ajedrez a Europa durante la Edad Media y su posterior popularización marcó el comienzo de una larga tradición de competencia y estudio en todo el mundo."""
        )
       
        print()
        print()
        print_title("Difusión del Ajedrez", Fore.RED)
        slow_print(
            """El ajedrez comenzó su expansión fuera de la India gracias a la influencia del Imperio Persa. Durante el período de la conquista árabe en el siglo VII, 
el juego llegó a los territorios árabes, donde se mantuvo bajo el nombre de 'shatranj'. Los persas refinaron el juego y lo llevaron a Europa a través de la Península Ibérica durante la Reconquista. 
A partir de allí, el ajedrez se extendió por el continente europeo, ganando popularidad rápidamente y adaptándose a las tradiciones y culturas locales. 
El desarrollo de la imprenta en el siglo XV facilitó aún más la diseminación de las reglas y estrategias del ajedrez, consolidándolo como un juego internacionalmente reconocido."""
        )
        L()
        PCT()
        
        titulo()
        print_title("Primer Campeón Mundial", Fore.MAGENTA)
        slow_print(
            """Emanuel Lasker, un gran maestro alemán, se convirtió en el primer campeón mundial de ajedrez oficialmente reconocido por la Federación Internacional de Ajedrez (FIDE) en 1921. 
Lasker, conocido por su enfoque sólido y su habilidad para adaptarse a diferentes estilos de juego, mantuvo su título hasta 1946. Su reinado fue notable por su capacidad para defender su 
título contra los mejores jugadores de su tiempo y su contribución al desarrollo de la teoría ajedrecística. 
La inclusión de Lasker como campeón mundial estableció un precedente para la organización formal del campeonato mundial de ajedrez."""
        )
        
        print()
        print()
        print_title("Inicio de la Era Moderna", Fore.BLUE)
        slow_print(
            """El primer Campeonato Mundial de Ajedrez se celebró en 1886, enfrentando a Wilhelm Steinitz contra Johannes Zukertort. Este evento marcó el inicio de la era moderna del ajedrez 
al establecer un título de campeón mundial reconocido oficialmente. La partida, disputada en varias ciudades europeas, destacó por la calidad de juego y la organización formal, 
sentando las bases para futuros campeonatos. El enfrentamiento no solo mostró el alto nivel competitivo de los jugadores, sino que también ayudó a estandarizar las reglas y 
la estructura de los torneos internacionales."""
        )
        L()
        PCT()

        titulo()
        print_title("Ruptura de Barreras Raciales", Fore.GREEN)
        slow_print(
            """El Match del Siglo entre Bobby Fischer de los Estados Unidos y Boris Spassky de la Unión Soviética en 1972 fue un evento crucial en la historia del ajedrez. 
Este match no solo fue significativo por su alta calidad competitiva, sino también por sus implicaciones políticas y sociales. Fischer, con su estilo innovador y su enfoque psicológico, 
rompió barreras raciales y políticas al derrotar a Spassky, desafiando la supremacía soviética en el ajedrez y capturando la atención mundial. 
El match simbolizó un cambio en la dinámica del ajedrez y en la percepción global del juego."""
        )
      
        print()
        print()
        print_title("Primer Campeón Mundial Oficial", Fore.RED)
        slow_print(
            """Wilhelm Steinitz, quien ascendió al estrellato en 1886 al derrotar a Johannes Zukertort, es reconocido como el primer campeón mundial de ajedrez oficial. 
Su enfoque analítico y su capacidad para evaluar con precisión las posiciones en el tablero establecieron nuevos estándares para el juego. 
Steinitz introdujo conceptos fundamentales en la teoría del ajedrez, como la importancia de la estructura de peones y el equilibrio en la posición. 
Su éxito y su enfoque metodológico en el juego sentaron las bases para futuros campeones y contribuyeron a la evolución del ajedrez moderno."""
        )
        L()
        PCT()

        titulo()
        print_title("Estilo Agresivo", Fore.MAGENTA)
        slow_print(
            """Mikhail Tal, conocido como el 'Mago de Riga', es famoso por su estilo de juego agresivo y sus sacrificios audaces. A lo largo de su carrera, Tal sorprendió a sus oponentes con 
combinaciones tácticas brillantes y una capacidad para tomar riesgos calculados. Su enfoque innovador y su habilidad para crear complicaciones en el tablero lo convirtieron en uno de los jugadores más fascinantes 
de la historia del ajedrez. Tal fue campeón mundial en 1960, y su estilo sigue influyendo en jugadores y estudios de ajedrez hasta hoy."""
        )
       
        print()
        print()
        print_title("Campeón Mundial en Ajedrez Clásico y Rápido", Fore.BLUE)
        slow_print(
            """Viswanathan Anand, un gran maestro indio, logró un hito significativo al convertirse en campeón mundial en ajedrez clásico y rápido. Anand ganó el título de campeón mundial en ajedrez clásico en 2007 
y defendió con éxito su título en 2008. Además, demostró su versatilidad al ganar el campeonato mundial de ajedrez rápido en 2009.
Su capacidad para adaptarse a diferentes formatos y su habilidad en el juego rápido destacaron su maestría y versatilidad como jugador de ajedrez de élite."""
        )
        L()
        PCT()

        titulo()
        print_title("Dominio en la Década de 1960", Fore.GREEN)
        slow_print(
         """Bobby Fischer, un prodigio del ajedrez estadounidense, dominó la década de 1960 con un rendimiento excepcional. Fischer fue conocido por su habilidad técnica, su enfoque innovador y su preparación exhaustiva. 
Su dominio culminó en la conquista del Campeonato Mundial en 1972, donde derrotó a Boris Spassky en el Match del Siglo. Fischer también es recordado por su papel en popularizar el ajedrez en 
Estados Unidos y por su influencia duradera en la teoría y estrategia del juego."""
        )
     
        print()
        print()
        print_title("Actual Campeón Mundial", Fore.RED)
        slow_print(
            """Magnus Carlsen, de Noruega, ha sido el campeón mundial de ajedrez desde 2013. Conocido por su estilo de juego versátil y su capacidad para manejar una amplia variedad de posiciones, 
Carlsen ha establecido nuevos estándares en la técnica y la estrategia ajedrecística. Su enfoque dinámico y su habilidad para adaptarse a diferentes oponentes y situaciones le han permitido
mantenerse en la cima del ajedrez mundial. Carlsen continúa siendo una figura influyente en el ajedrez y un referente para jugadores de todos los niveles."""
        )
        L()
       

    print_theory()
