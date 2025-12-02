import sys
import time 
import os
import msvcrt
from colorama import*
import json
import threading
import keyboard




RESET = "\033[0m"


def nivel2():
    
    puntaje=0


    
        
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
                
      
      



        

    

    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)
    print()
    print("           Pregunta 1: ¿Cuántas casillas tiene un tablero de ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "64")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "72")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "100")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()
    opcioncorrecta = "1"
    explicacion = "Explicación: Un tablero de ajedrez está compuesto por 64 casillas."

    R=evaluar()        
    if R== opcioncorrecta :
        puntaje +=1
    



    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)
    print()
    print("           Pregunta 2: ¿Cómo se lee una casilla en el tablero de ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Número seguido de letra (ej. 3ª)")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Letra seguida de número (ej. A3)")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Solo letra (ej. A)")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()

    
    opcioncorrecta = "2"
    explicacion = "Explicación: Las casillas se leen con la letra de la columna seguida del número de la fila (por ejemplo, A3)."
    R=evaluar()
     
    if R== opcioncorrecta :
       puntaje +=1

    else: 
        
        if D=="3":
            puntaje-=1

            
  

    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)    
    print()
    print("           Pregunta 3: ¿Para qué sirven las aperturas en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)    
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Para ganar rápidamente")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Para desarrollar las piezas y controlar el centro")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Para proteger al rey")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()


    
    opcioncorrecta = "2"
    explicacion = "Explicación: Las aperturas en ajedrez se utilizan para desarrollar las piezas y controlar el centro del tablero en las primeras jugadas de la partida."
    R=evaluar()
    if R== opcioncorrecta :
       puntaje +=1

    else: 
        
        if D=="3":
            puntaje-=1

    

    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET) 
    print()
    print("           Pregunta 4: ¿Qué es el jaque en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)    
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Cuando una pieza es capturada")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Cuando el rey está bajo ataque")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Cuando un peón corona")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()

    
    opcioncorrecta = "2"
    explicacion = "Explicación: El jaque en ajedrez es cuando el rey está bajo amenaza de ser capturado en el siguiente movimiento."

    R=evaluar()        
    if R== opcioncorrecta :
       puntaje +=1

    else: 
        
        if D=="3":
            puntaje-=1




    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)
    print()
    print("           Pregunta 5: ¿Qué es el jaque mate? / 1 punto")
    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)    
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Cuando el rey está bajo ataque y no puede escapar")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Cuando el rey se mueve dos casillas")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Cuando el peón corona")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()

    # Variables actualizadas
    opcioncorrecta = "1"
    explicacion = "Explicación: El jaque mate ocurre cuando el rey está en jaque y no tiene movimientos legales para escapar."
    
    R=evaluar()        
    if R== opcioncorrecta :
       puntaje +=1

    else: 
        
        if D=="3":
            puntaje-=1

    


    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)
    print()
    print("           Pregunta 6: ¿Qué es el rey ahogado? / 1 punto")
    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET) 
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Cuando el rey está en jaque y no tiene ningún movimiento legal posible")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Cuando el rey está en jaque y tiene una sola casilla para escapar")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Cuando el rey ya no tiene ninguna casilla legal para moverse")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()

    # Variables actualizadas
    opcioncorrecta = "3"
    explicacion = "Explicación: El rey ahogado ocurre cuando el rey no está en jaque, pero no tiene ningún movimiento legal para realizar."

    
    R=evaluar()        
    if R== opcioncorrecta :
       puntaje +=1

    else: 
        
        if D=="3":
            puntaje-=1

    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET) 
    print()
    print("           Pregunta 7: ¿Qué es un enroque en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)    
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Cuando el rey se mueve dos casillas hacia un lado y una torre se coloca al lado")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Cuando el rey se mueve dos casillas hacia un lado y la torre se mueve hacia el otro lado")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Cuando el rey se mueve una casilla y la torre se mueve al otro lado del rey")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()

    # Variables actualizadas
    opcioncorrecta = "1"
    explicacion = "Explicación: El enroque es una jugada especial en ajedrez donde el rey se mueve dos casillas hacia una torre y esa torre se mueve al otro lado del rey."


    R=evaluar()        
    if R== opcioncorrecta :
       puntaje +=1

    else: 
        
        if D=="3":
            puntaje-=1


    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET) 
    print()
    print("           Pregunta 8: ¿Qué significa 'tablas' ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)   
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Una posición de empate")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Una apertura especial")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Una jugada ilegal")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()

    # Variables actualizadas
    opcioncorrecta = "1"
    explicacion = "Explicación: 'Tablas' en ajedrez indica una posición de la partida donde ninguno de los jugadores puede ganar, resultando en un empate."

    R=evaluar()        
    if R== opcioncorrecta :
       puntaje +=1

    else: 
        
        if D=="3":
            puntaje-=1


    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)    
    print()
    print("           Pregunta 9: ¿Qué condiciones se deben presentar para que se desarrolle correctamente el enroque? / 1 punto")
    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)   
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Que el rey debe haberse movido al menos una casilla de su posición inicial.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Que el rey no puede estar en jaque y no puede pasar por casillas amenazadas por una pieza enemiga durante el enroque.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Que el rey y la torre no se deben haber movido de su posición inicial y que la fila entre estas dos piezas debe estar despejada de cualquier pieza.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()

    # Variables actualizadas
    opcioncorrecta = "3"
    explicacion = "Explicacón: Para realizar el enroque, tanto el rey como la torre no deben haberse movido previamente en la partida, y la fila entre ellos debe estar despejada de cualquier pieza."


    R=evaluar()        
    if R== opcioncorrecta :
       puntaje +=1

    else: 
        
        if D=="3":
            puntaje-=1


    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)    
    print()
    print("           Pregunta 10: : ¿Qué es la captura al paso en ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTGREEN_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)   
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Mover un peón dos casillas hacia adelante desde su posición inicial.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Un movimiento especial de la reina.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Capturar un peón enemigo que haya avanzado dos casillas desde su posición inicial, y que ambos estén enfrentados.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()

    # Variables actualizadas
    opcioncorrecta = "3"
    explicacion = "Explicacón: La captura al paso en ajedrez permite a un peón capturar a otro peón enemigo que haya avanzado dos casillas desde su posición inicial y se encuentre al lado del peón que realiza la captura."


    R=evaluar()        
    
    if R== opcioncorrecta :
       puntaje +=1
  
       

    else: 
        
        if D=="3":
            puntaje-=1

        

    if puntaje <0:
         puntaje=0


       
        

        


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

            
                    RI= 10-puntaje
                    T()
                    print()
                    print()
                    print(Fore.LIGHTYELLOW_EX+"----------------------------    has completado el nivel: 2   -------------------------------------------- "+RESET)
                    print()
                    print()
                    print(Fore.BLUE+"___ DIFICULTAD ELEGIDA: "+RESET+" >>>  "+str(D)+"  <<<")
                    print()
                    print()
                    print(Fore.BLUE+"___ Puntos obtenidos ---> "+RESET+str(puntaje))
                    print()
                    print()
                    print(Fore.BLUE+"___ Respuestas incorrectas ---> "+RESET+str(RI))
                    print()
                    print(Fore.LIGHTYELLOW_EX+"---------------------------------------------------------------------------------------------------------------"+RESET)
                    print()
                    

        else:
            
                    RI= 10-puntaje
                    T()
                    print()
                    print()
                    print(Fore.LIGHTYELLOW_EX+"----------------------------    has completado el nivel: 2   -------------------------------------------- "+RESET)
                    print()
                    print()
                    print(Fore.RED+"___ DIFICULTAD ELEGIDA: "+RESET+" >>>  "+str(D)+" (PUNTAJE NEGATIVO)  <<<")
                    print()
                    print()
                    print(Fore.BLUE+"___ Puntos obtenidos ---> "+RESET+str(puntaje))
                    print()
                    print()
                    print(Fore.BLUE+"___ Respuestas incorrectas ---> "+RESET+str(RI))
                    print()
                    print(Fore.LIGHTYELLOW_EX+"---------------------------------------------------------------------------------------------------------------"+RESET)
                    print()
                    

    except:
                    RI= 10-puntaje
                    T()
                    print()
                    print()
                    print(Fore.LIGHTYELLOW_EX+"----------------------------    has completado el nivel: 2   -------------------------------------------- "+RESET)
                    print()
                    print()
                    print(Fore.BLUE+"___ DIFICULTAD ELEGIDA: "+RESET+" >>>    <<<")
                    print()
                    print()
                    print(Fore.BLUE+"___ Puntos obtenidos ---> "+RESET+str(puntaje))
                    print()
                    print()
                    print(Fore.BLUE+"___ Respuestas incorrectas ---> "+RESET+str(RI))
                    print()
                    print(Fore.LIGHTYELLOW_EX+"---------------------------------------------------------------------------------------------------------------"+RESET)
                    print()
                    

    return puntaje


