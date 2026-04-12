RESET="\033[0m"


import sys
import time 
import os
import msvcrt
from colorama import*
import json
import threading
import keyboard


def nivel4():
    puntaje4=0
    
    




    
    def PCT ():
        for char in "Presiona cualquier tecla para continuar... ":
            print(char, end='', flush=True),time.sleep(0.001)
        msvcrt.getch()
        os.system('cls' if os.name == 'nt' else 'clear')
    

    def LIMPIAR():
        sys.stdout.write('\033[F\033[K')

    try:

        with open('DIFICULTAD.json', 'r') as file:
            D=json.load(file)
        if D == "1" :

            def evaluar():
            
                while (True):
                    
                    
                    R=input("Ingrese su respuesta: ")
                    if R=="1" or R== "2" or R== "3":
                        if R== opcioncorrecta:
                                LIMPIAR()
                                
                                print(Fore.GREEN+" --------------------  ¡Correcto!  --------------------"+RESET)
                                print()
                                for char in explicacion:
                                    print(char, end='', flush=True),time.sleep(0.02)
                                print("\n" * 7)
                                PCT()
                                
                                break
                                
                                
                        else:
                                LIMPIAR()
                                print(Fore.RED+" >>>>>>>>>>>>    Incorrecto, la opcion correcta es "+ str(opcioncorrecta)+ "    <<<<<<<<<<<<" +RESET)
                                print("\n" * 7)
                                PCT()
                                break  


                    else:
                        LIMPIAR()
                        print(Fore.YELLOW+"Ingresar respuesta valida. Porfavor vuelve a intentarlo"+RESET)
                        time.sleep(2)
                        LIMPIAR()
                return(R)
            
        elif D == "2":
            def evaluar():
                stop_event = threading.Event()
                R = None

                def countdown():
                    for i in range(10, 0, -1):
                        if stop_event.is_set():
                            break
                        print(f"\r{Fore.GREEN}TIEMPO >>>>>   {i} segundos   <<<<<  {RESET} Ingrese su respuesta: ", end="")
                        time.sleep(1)
                        
                    if not stop_event.is_set():
                        stop_event.set()
                        
                        
                        print(f"\r{Fore.RED}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   ¡Tiempo agotado!   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{RESET}")
                    
                        print()
                        print()
                        print()
                        print("Presiona enter para continuar...")
                        keyboard.wait('enter')
                        os.system('cls' if os.name == 'nt' else 'clear')

                        
                def stop_input():
                    nonlocal R
                    while not stop_event.is_set():
                        R = input()
                        
                        if R in ["1", "2", "3"]:
                            if R == opcioncorrecta:
                                stop_event.set()
                                LIMPIAR()
                                print(Fore.GREEN + " --------------------  ¡Correcto!  --------------------" + RESET)
                                print()
                                for char in explicacion:
                                    print(char, end='', flush=True)
                                    time.sleep(0.02)
                                print("\n" * 7)
                                PCT()
                                break
                            else:
                                stop_event.set()
                                LIMPIAR()
                                print(Fore.RED + " >>>>>>>>>>>>    Incorrecto, la opción correcta es " + str(opcioncorrecta) + "    <<<<<<<<<<<" + RESET)
                                print("\n" * 7)
                                PCT()
                                break
                        else:
                            LIMPIAR()
                        
                            
                            
                            
                            
                    return R

                
                timer_thread = threading.Thread(target=countdown)
                input_thread = threading.Thread(target=stop_input)

                
                timer_thread.start()
                input_thread.start()

                
                timer_thread.join()
                input_thread.join()

                return R   
            
        elif D =="3":

                def evaluar():
                    stop_event = threading.Event()
                    R = None

                    def countdown():
                        for i in range(5, 0, -1):
                            if stop_event.is_set():
                                break
                            print(f"\r{Fore.GREEN}TIEMPO >>>>>   {i} segundos   <<<<<  {RESET} Ingrese su respuesta: ", end="")
                            time.sleep(1)
                            
                        if not stop_event.is_set():
                            stop_event.set()
                            
                            
                            print(f"\r{Fore.RED}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<   ¡Tiempo agotado! \ -1 PUNTO   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{RESET}")
                        
                            print()
                            print()
                            print()
                            print("Presiona enter para continuar...")
                            keyboard.wait('enter')
                            os.system('cls' if os.name == 'nt' else 'clear')

                            
                    def stop_input():
                        nonlocal R
                        while not stop_event.is_set():
                            R = input()
                            
                            if R in ["1", "2", "3"]:
                                if R == opcioncorrecta:
                                    stop_event.set()
                                    LIMPIAR()
                                    print(Fore.GREEN + " --------------------  ¡Correcto!  --------------------" + RESET)
                                    print()
                                    for char in explicacion:
                                        print(char, end='', flush=True)
                                        time.sleep(0.02)
                                    print("\n" * 7)
                                    PCT()
                                    break
                                else:
                                    stop_event.set()
                                    LIMPIAR()
                                    print(Fore.RED + " >>>>>>>>>>>>    Incorrecto, la opción correcta es " + str(opcioncorrecta) + "  \ -1 PUNTO  <<<<<<<<<<<" + RESET)
                                    print("\n" * 7)
                                    PCT()
                                    break
                            else:
                                LIMPIAR()
                            
                                
                                
                                
                                
                        return R

                    
                    timer_thread = threading.Thread(target=countdown)
                    input_thread = threading.Thread(target=stop_input)

                    
                    timer_thread.start()
                    input_thread.start()

                    
                    timer_thread.join()
                    input_thread.join()

                    return R   
    except:
          def evaluar():
            
                while (True):
                    
                    
                    R=input("Ingrese su respuesta: ")
                    if R=="1" or R== "2" or R== "3":
                        if R== opcioncorrecta:
                                LIMPIAR()
                                
                                print(Fore.GREEN+" --------------------  ¡Correcto!  --------------------"+RESET)
                                print()
                                for char in explicacion:
                                    print(char, end='', flush=True),time.sleep(0.02)
                                print("\n" * 7)
                                PCT()
                                
                                break
                                
                                
                        else:
                                LIMPIAR()
                                print(Fore.RED+" >>>>>>>>>>>>    Incorrecto, la opcion correcta es "+ str(opcioncorrecta)+ "    <<<<<<<<<<<<" +RESET)
                                print("\n" * 7)
                                PCT()
                                break  


                    else:
                        LIMPIAR()
                        print(Fore.YELLOW+"Ingresar respuesta valida. Porfavor vuelve a intentarlo"+RESET)
                        time.sleep(2)
                        LIMPIAR()
                return(R)
                
        

            
    # Pregunta 1
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 1: ¿Qué es el “ahogado de Fort Knox” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Una estrategia en la que se bloquea el desarrollo del oponente mediante una formación defensiva sólida.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Una táctica en la que un rey enemigo queda atrapado entre sus propias piezas y no puede escapar del jaque mate.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Una maniobra en la que se sacrifican múltiples piezas para abrir líneas de ataque hacia el rey enemigo.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   " + RESET)
    print()
    opcioncorrecta = "2"
    explicacion = "Explicación: El “ahogado de Fort Knox” es una táctica en la que un rey enemigo queda atrapado entre sus propias piezas y no puede escapar del jaque mate, similar a la táctica de 'ahogado', pero con una posición más restringida."

    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje4 +=1


    # Pregunta 2
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 2: ¿Qué es la “iniciativa” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "La ventaja que tiene un jugador al tener el turno de mover.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "La habilidad de realizar jugadas sorpresivas que desconcierten al oponente.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "El control del centro del tablero desde las primeras jugadas.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   " + RESET)
    print()
    opcioncorrecta = "1"
    explicacion = "Explicación: La 'iniciativa' en ajedrez se refiere a la ventaja que tiene un jugador al tener el turno de mover, lo que le permite dictar el curso de la partida y mantener la presión sobre el oponente."

    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje4 +=1
        

    else: 
        
        if D=="3":
            puntaje4-=1

    # Pregunta 3
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 3: ¿Qué es una “cegada” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Una maniobra en la que se bloquea la visión del oponente sobre el tablero para confundirlo.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Una situación en la que un jugador no puede encontrar una jugada adecuada debido a la presión del tiempo.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Una jugada que sacrifica una pieza para desviar la atención del oponente de una amenaza más fuerte.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   " + RESET)
    print()
    opcioncorrecta = "3"
    explicacion = "Explicación: Una 'cegada' en ajedrez es una jugada que sacrifica una pieza para desviar la atención del oponente de una amenaza más fuerte, generalmente utilizada para crear oportunidades tácticas o para desequilibrar la posición."
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje4 +=1
        

    else: 
        
        if D=="3":
            puntaje4-=1

    # Pregunta 4
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 4: ¿Qué es el “remate” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Una serie de jugadas finales que conducen a un jaque mate inevitable.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Una situación en la que un jugador no puede continuar la partida debido a una posición desfavorable.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Un movimiento decisivo que asegura la victoria al consolidar una ventaja material o posicional.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   " + RESET)
    print()
    opcioncorrecta = "1"
    explicacion = "Explicación: El 'remate' en ajedrez se refiere a una serie de jugadas finales que conducen a un jaque mate inevitable, cerrando con éxito la partida."
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje4 +=1
        

    else: 
        
        if D=="3":
            puntaje4-=1

    # Pregunta 5
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 5: ¿Qué es el “ataque de Karpov” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Un estilo de juego caracterizado por una presión constante y un control meticuloso del tablero.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Una estrategia agresiva de apertura desarrollada por el Gran Maestro Anatoly Karpov.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Una serie de maniobras tácticas que buscan debilitar la estructura de peones del oponente.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   " + RESET)
    print()
    opcioncorrecta = "1"
    explicacion = "Explicación: El “ataque de Karpov” en ajedrez se refiere a un estilo de juego caracterizado por una presión constante y un control meticuloso del tablero, nombrado en honor al Gran Maestro Anatoly Karpov por su habilidad para implementar esta estrategia."
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje4 +=1
        

    else: 
        
        if D=="3":
            puntaje4-=1

    # Pregunta 6
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 6: ¿Qué es un “sacrificio de calidad” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "El sacrificio de una torre a cambio de una pieza menor para obtener una ventaja posicional o táctica.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Una táctica en la que se sacrifican varias piezas para obtener un ataque decisivo.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "La renuncia a una calidad (torre por caballo o alfil) para obtener una ventaja en la iniciativa o en la posición.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   " + RESET)
    print()
    opcioncorrecta = "3"
    explicacion = "Explicación: Un 'sacrificio de calidad' en ajedrez es la renuncia a una calidad (torre por caballo o alfil) para obtener una ventaja en la iniciativa o en la posición, buscando generar un beneficio estratégico o táctico."

    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje4 +=1
        

    else: 
        
        if D=="3":
            puntaje4-=1

    # Pregunta 7
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 7: ¿Qué es un “zugzwang” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Una táctica de apertura que busca controlar el centro del tablero con peones.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Una situación en la que cualquier movimiento realizado por un jugador empeora su posición.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Una maniobra defensiva en la que se protege una pieza clave para evitar su captura.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   " + RESET)
    print()
    opcioncorrecta = "2"
    explicacion = "Explicación: Un 'zugzwang' en ajedrez es una situación en la que cualquier movimiento realizado por un jugador empeora su posición, obligándolo a hacer una jugada que perjudique su situación en el tablero."
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje4 +=1
        

    else: 
        
        if D=="3":
            puntaje4-=1

    # Pregunta 8
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 8: ¿Qué es una 'sobrecarga' en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Una situación en la que una pieza es obligada a defender múltiples amenazas.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Una estrategia de apertura que se basa en el sacrificio de peones para obtener una ventaja en el centro del tablero.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Un tipo de jaque mate que se produce cuando el rey está atrapado en una esquina del tablero.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   " + RESET)
    print()
    opcioncorrecta = "1"
    explicacion = "Explicación: La 'sobrecarga' es ua situación en donde una pieza es forzada a defender múltiples amenazas lo que la convierte muy vulnerable a ser capturada."
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje4 +=1
        

    else: 
        
        if D=="3":
            puntaje4-=1

    # Pregunta 10
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 9: ¿Qué es una 'partida por correspondencia' en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Una partida rápida que dura 1 minuto.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Una partida donde los jugadores intercambian movimientos por mensajeria.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Una partida que se juega por correo postal o electrónico.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   " + RESET)
    print()
    opcioncorrecta = "3"
    explicacion = """Explicación: Una “partida de correspondencia” en ajedrez es una partida jugada entre dos jugadores por correspondencia postal o electrónica, donde los jugadores tienen un período prolongado para realizar
    cada movimiento y pueden planificar y analizar cuidadosamente sus estrategias y movimientos."""
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje4 +=1
        

    else: 
        
        if D=="3":
            puntaje4-=1

    #Pregunta10
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 10: ¿Qué es 'Elo' en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTCYAN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Un sacrificio de una pieza de menor valor para obtener una posición de ataque más favorable.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Un sistema de puntuación que calcula la habilidad relativa de los jugadores de ajedrez.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + " Una estrategia de apertura en la que se sacrifica una pieza menor para obtener ventaja posicional.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   " + RESET)
    print()
    opcioncorrecta = "2"
    explicacion = """El Elo es un sistema de puntuación utilizado para calcular la habilidad relativa de los jugadores de ajedrez y otros juegos de mesa. Desarrollado por el profesor de física Arpad Elo, 
    este sistema permite estimar la fortaleza de un jugador basado en sus resultados contra otros jugadores. Cuanto mayor sea el puntaje Elo de un jugador, mayor será su habilidad percibida."""
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje4 +=1
        

    else: 
        
        if D=="3":
            puntaje4-=1

    if puntaje4 <0:
        puntaje4 =0





    def T():
        print(Fore.LIGHTMAGENTA_EX+"####################################################################################################################################################################"+RESET)
        print(Fore.LIGHTWHITE_EX+"                                                                         NIVEL COMPLETADO"+RESET)
        print(Fore.LIGHTMAGENTA_EX+"####################################################################################################################################################################"+RESET)






    try:  


        with open('DIFICULTAD.json', 'r') as file:
            D=json.load(file)




        if D == "1":
            D="Fácil"
        if D == "2":
            D="Normal"
        if D=="3":
            D="Dificil"
        



            
            
        if D=="Fácil" or D=="Normal" :

            
                    RI= 10-puntaje4
                    T()
                    print()
                    print()
                    print(Fore.LIGHTYELLOW_EX+"----------------------------    has completado el nivel: 4   -------------------------------------------- "+RESET)
                    print()
                    print()
                    print(Fore.BLUE+"___ DIFICULTAD ELEGIDA: "+RESET+" >>>  "+str(D)+"  <<<")
                    print()
                    print()
                    print(Fore.BLUE+"___ Puntos obtenidos ---> "+RESET+str(puntaje4))
                    print()
                    print()
                    print(Fore.BLUE+"___ Respuestas incorrectas ---> "+RESET+str(RI))
                    print()
                    print(Fore.LIGHTYELLOW_EX+"---------------------------------------------------------------------------------------------------------------"+RESET)
                    print()
                    

        else:
            
                    RI= 10-puntaje4
                    T()
                    print()
                    print()
                    print(Fore.LIGHTYELLOW_EX+"----------------------------    has completado el nivel: 4   -------------------------------------------- "+RESET)
                    print()
                    print()
                    print(Fore.RED+"___ DIFICULTAD ELEGIDA: "+RESET+" >>>  "+str(D)+" (PUNTAJE NEGATIVO)  <<<")
                    print()
                    print()
                    print(Fore.BLUE+"___ Puntos obtenidos ---> "+RESET+str(puntaje4))
                    print()
                    print()
                    print(Fore.BLUE+"___ Respuestas incorrectas ---> "+RESET+str(RI))
                    print()
                    print(Fore.LIGHTYELLOW_EX+"---------------------------------------------------------------------------------------------------------------"+RESET)
                    print()
                    

    except:
                    RI= 10-puntaje4
                    T()
                    print()
                    print()
                    print(Fore.LIGHTYELLOW_EX+"----------------------------    has completado el nivel: 4   -------------------------------------------- "+RESET)
                    print()
                    print()
                    print(Fore.BLUE+"___ DIFICULTAD ELEGIDA: "+RESET+" >>>    <<<")
                    print()
                    print()
                    print(Fore.BLUE+"___ Puntos obtenidos ---> "+RESET+str(puntaje4))
                    print()
                    print()
                    print(Fore.BLUE+"___ Respuestas incorrectas ---> "+RESET+str(RI))
                    print()
                    print(Fore.LIGHTYELLOW_EX+"---------------------------------------------------------------------------------------------------------------"+RESET)
                    print()
                    


    return puntaje4

