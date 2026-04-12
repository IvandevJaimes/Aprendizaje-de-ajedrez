   
import sys
import time 
import os
import msvcrt
from colorama import*
import json
import threading
import keyboard




RESET = "\033[0m"


def nivel3():
    puntaje3= 0
    
 


     
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




        if D == "2":
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
        elif D=="1":
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
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 1: ¿Qué es un “jaque doble” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Un jaque que proviene de dos piezas diferentes en el mismo movimiento.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Un jaque que el rey puede evadir con dos movimientos distintos.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Un jaque que se produce cuando dos reyes están en posición de capturarse.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "1"
    explicacion = "Explicación: Un jaque doble ocurre cuando dos piezas atacan al rey simultáneamente, y este no puede moverse para escapar de ambos ataques."

    R=evaluar()        
    if R== opcioncorrecta :
        puntaje3+=1
    



    # Pregunta 2
    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print("           Pregunta 2: ¿Qué es una “desviación” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Un movimiento que aleja una pieza de su defensa.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Un movimiento que obliga al oponente a abandonar su estrategia.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Un movimiento que cambia el rumbo de la partida hacia un resultado imprevisto.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "1"
    explicacion = "Explicación: Una desviación es un movimiento que aleja una pieza de su función defensiva, exponiéndola a ser capturada o comprometiendo la posición del jugador."


    R=evaluar()        
    if R== opcioncorrecta :
       puntaje3 +=1

    else: 
        
        if D=="3":
            puntaje3-=1

    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print("           Pregunta 3: ¿Qué es la “cadeneta” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Una serie de jugadas consecutivas en las que una pieza ataca repetidamente al rey contrario.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Una situación en la que un jugador domina el centro del tablero con sus piezas.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Un error táctico que conduce a la pérdida de material.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "1"
    explicacion = "Explicación: La cadeneta es una serie de jugadas consecutivas en las que una pieza ataca repetidamente al rey contrario, generalmente con la intención de forzar un jaque mate o ganar material."



    R=evaluar()        
    if R== opcioncorrecta :
       puntaje3 +=1

    else: 
        
        if D=="3":
            puntaje3-=1


    # Pregunta 4
    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print("           Pregunta 4: ¿Qué es el “opuesto de la oposición” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Una situación en la que un jugador domina la posición del otro en el centro del tablero.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Una técnica utilizada en finales de peones para garantizar la promoción de un peón.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Una situación en la que los reyes se enfrentan en casillas adyacentes con un número impar de casillas entre ellos.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "3"
    explicacion = """Explicación: El opuesto de la oposición es una situación en la que los reyes se enfrentan en casillas adyacentes con un número impar de casillas entre ellos, 
lo que garantiza que el jugador que no tiene el turno pueda avanzar y tomar control del territorio."""


    R=evaluar()        
    if R== opcioncorrecta :
       puntaje3 +=1

    else: 
        
        if D=="3":
            puntaje3-=1


    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print("           Pregunta 5: ¿Qué es una “partida a la italiana” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Una partida caracterizada por un juego agresivo y táctico desde las primeras jugadas.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Una partida jugada siguiendo las reglas del ajedrez italiano clásico.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Una partida en la que se utilizan aperturas poco convencionales o variantes poco comunes.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "1"
    explicacion = "Explicación: La partida a la italiana se caracteriza por un juego agresivo y táctico desde las primeras jugadas, y suele involucrar aperturas que buscan el control del centro y un rápido desarrollo de las piezas."



    R=evaluar()        
    if R== opcioncorrecta :
       puntaje3 +=1

    else: 
        
        if D=="3":
            puntaje3-=1

    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print("           Pregunta 6: ¿Qué es una “jugada intermedia” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Un movimiento que se realiza entre dos jugadas tácticas consecutivas.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Un movimiento sorpresivo que altera el curso esperado de la partida.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Un movimiento que permite al jugador cambiar el curso de la partida a su favor.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "2"
    explicacion = """Explicación: Una jugada intermedia, también conocida como “intermezzo” o “zwischenzug”, es un movimiento sorpresivo que altera el curso esperado de la partida, 
a menudo aprovechando una oportunidad táctica en medio de una secuencia de jugadas."""



    R=evaluar()        
    if R== opcioncorrecta :
       puntaje3 +=1

    else: 
        
        if D=="3":
            puntaje3-=1


    # Imprimir la segunda pregunta
    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print("           Pregunta 7: ¿Qué es un “ataque doble” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Un ataque en el que dos piezas cooperan para amenazar una misma casilla o pieza enemiga.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Un ataque que puede ser repelido por una única defensa efectiva.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Un ataque que involucra a dos piezas del mismo color en diagonal.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "2"
    explicacion = "Explicación: Un ataque doble es un ataque en el que dos piezas cooperan para amenazar una misma casilla o pieza enemiga, forzando al oponente a elegir cuál amenaza contrarrestar."


    R=evaluar()        
    if R== opcioncorrecta :
       puntaje3 +=1

    else: 
        
        if D=="3":
            puntaje3-=1




    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print("           Pregunta 8: ¿Qué es una “miniatura” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Una partida de ajedrez rápida, generalmente de menos de 25 movimientos.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Una partida de ajedrez en la que se produce un mate en menos de 15 movimientos.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Una partida de ajedrez en la que uno de los jugadores sacrifica material para obtener una victoria rápida.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "2"
    explicacion = "Explicación: Una miniatura es una partida de ajedrez en la que se produce un mate en menos de 15 movimientos, generalmente como resultado de errores tácticos graves por parte de uno de los jugadores."


    R=evaluar()        
    if R== opcioncorrecta :
       puntaje3 +=1

    else: 
        
        if D=="3":
            puntaje3-=1


    # Imprimir la cuarta pregunta
    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print("           Pregunta 9: ¿Qué es una “perpetua” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Una situación en la que un jugador repite la misma jugada varias veces.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Una situación en la que un jugador abandona la partida debido a una posición desfavorable.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Una situación en la que un jugador repite una secuencia de jugadas sin avanzar en la partida.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "3"
    explicacion = "Explicación: Una perpetua es una situación en la que un jugador repite una secuencia de jugadas sin avanzar en la partida, resultando en un empate por repetición."


    R=evaluar()        
    if R== opcioncorrecta :
       puntaje3 +=1

    else: 
        
        if D=="3":
            puntaje3-=1



    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)    
    print()
    print("           Pregunta 10: ¿Qué significa “tablas por falta de material” en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTBLUE_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)   
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Una situación en la que ambos jugadores tienen una cantidad igual de material y ninguno puede forzar un jaque mate.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Una situación en la que uno de los jugadores no puede realizar movimientos legales y no está en jaque.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Una situación en la que un jugador abandona la partida debido a la escasez de material en el tablero.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "1"
    explicacion = """Explicación: Las tablas por falta de material se producen cuando ambos jugadores tienen una cantidad igual de material (por ejemplo, solo reyes en el tablero) 
y ninguno puede forzar un jaque mate debido a la falta de piezas para realizarlo."""
    R=evaluar()        
    if R== opcioncorrecta :
       puntaje3 +=1

       

    else: 
        
        if D=="3":
            puntaje3-=1

       

    if puntaje3 <0:
         puntaje3=0

            



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

            
                    RI= 10-puntaje3
                    T()
                    print()
                    print()
                    print(Fore.LIGHTYELLOW_EX+"----------------------------    has completado el nivel: 3   -------------------------------------------- "+RESET)
                    print()
                    print()
                    print(Fore.BLUE+"___ DIFICULTAD ELEGIDA: "+RESET+" >>>  "+str(D)+"  <<<")
                    print()
                    print()
                    print(Fore.BLUE+"___ Puntos obtenidos ---> "+RESET+str(puntaje3))
                    print()
                    print()
                    print(Fore.BLUE+"___ Respuestas incorrectas ---> "+RESET+str(RI))
                    print()
                    print(Fore.LIGHTYELLOW_EX+"---------------------------------------------------------------------------------------------------------------"+RESET)
                    print()
                    

        else:
            
                    RI= 10-puntaje3
                    T()
                    print()
                    print()
                    print(Fore.LIGHTYELLOW_EX+"----------------------------    has completado el nivel: 3   -------------------------------------------- "+RESET)
                    print()
                    print()
                    print(Fore.RED+"___ DIFICULTAD ELEGIDA: "+RESET+" >>>  "+str(D)+" (PUNTAJE NEGATIVO)  <<<")
                    print()
                    print()
                    print(Fore.BLUE+"___ Puntos obtenidos ---> "+RESET+str(puntaje3))
                    print()
                    print()
                    print(Fore.BLUE+"___ Respuestas incorrectas ---> "+RESET+str(RI))
                    print()
                    print(Fore.LIGHTYELLOW_EX+"---------------------------------------------------------------------------------------------------------------"+RESET)
                    print()
                    

    except:
                    RI= 10-puntaje3
                    T()
                    print()
                    print()
                    print(Fore.LIGHTYELLOW_EX+"----------------------------    has completado el nivel: 3   -------------------------------------------- "+RESET)
                    print()
                    print()
                    print(Fore.BLUE+"___ DIFICULTAD ELEGIDA: "+RESET+" >>>    <<<")
                    print()
                    print()
                    print(Fore.BLUE+"___ Puntos obtenidos ---> "+RESET+str(puntaje3))
                    print()
                    print()
                    print(Fore.BLUE+"___ Respuestas incorrectas ---> "+RESET+str(RI))
                    print()
                    print(Fore.LIGHTYELLOW_EX+"---------------------------------------------------------------------------------------------------------------"+RESET)
                    print()


    return puntaje3
    






        

