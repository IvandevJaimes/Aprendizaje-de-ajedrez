RESET="\033[0m"


import sys
import time 
import os
import msvcrt
from colorama import*
import json
import threading
import keyboard


def nivel5():
    puntaje5=0
    
    




    
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
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 1: ¿En qué siglo se originó el ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Siglo V a.C.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Siglo I d.C.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Siglo VI d.C.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "3"

    explicacion = "Explicación: El ajedrez se originó en el siglo VI d.C., en la India."
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje5 +=1
        


        
    # Pregunta 2
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 2: ¿Qué civilización contribuyó significativamente a la difusión del ajedrez desde la India a otras partes del mundo? / 1 punto")
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "El Imperio Romano")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "El Imperio Persa")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "El Imperio Chino")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "2"

    explicacion = "Explicación: El Imperio Persa fue fundamental en la difusión del ajedrez desde la India a otras partes del mundo."
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje5 +=1
        

    else: 
        if D=="3":
            puntaje5-=1
        
        
    # Pregunta 3
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 3: ¿Quién fue el primer campeón mundial oficialmente reconocido por la Federación Internacional de Ajedrez (FIDE)? / 1 punto")
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Emanuel Lasker")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Wilhelm Steinitz")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Bobby Fischer")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "2"

    explicacion = "Explicación: Wilhelm Steinitz fue el primer campeón mundial oficialmente reconocido por la FIDE en 1921."
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje5 +=1
        

    else: 
        if D=="3":
            puntaje5-=1
        
        
    # Pregunta 4
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 4: ¿Qué evento marcó el inicio de la era moderna del ajedrez en 1886? / 1 punto")
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "La fundación de la Federación Internacional de Ajedrez (FIDE).")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "La creación del primer reloj de ajedrez.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "El primer Campeonato Mundial de Ajedrez.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "3"

    explicacion = "Explicación: El primer Campeonato Mundial de Ajedrez, disputado entre Steinitz y Zukertort, marcó el inicio de la era moderna del ajedrez."
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje5 +=1
        

    else: 
        if D=="3":
            puntaje5-=1
        
        
    # Pregunta 5
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 5: ¿Qué hito histórico rompió las barreras raciales en el ajedrez en 1972? / 1 punto")
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "El Match del Siglo entre Bobby Fischer y Boris Spassky.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "La victoria de Bobby Fischer en el Torneo de Candidatos.")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "La creación de la FIDE.")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "1"

    explicacion = "Explicación: El Match del Siglo entre Bobby Fischer y Boris Spassky en 1972 rompió las barreras raciales en el ajedrez."
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje5 +=1
        

    else: 
        if D=="3":
            puntaje5-=1
        
        
    # Pregunta 6
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 6: ¿Quién fue el primer campeón mundial de ajedrez reconocido oficialmente? / 1 punto")
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Wilhelm Steinitz")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Bobby Fischer")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Garry Kasparov")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "1"

    explicacion = "Explicación: Wilhelm Steinitz fue el primer campeón mundial de ajedrez oficialmente reconocido."
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje5 +=1
        

    else: 
        if D=="3":
            puntaje5-=1
        
        
    # Pregunta 7
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 7: ¿Quién es considerado uno de los mejores jugadores de ajedrez de todos los tiempos y conocido por su estilo agresivo? / 1 punto")
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Bobby Fischer")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Mikhail Tal")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Anatoly Karpov")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "2"

    explicacion = "Explicación: Mikhail Tal es conocido por su estilo agresivo y es considerado uno de los mejores jugadores de ajedrez de todos los tiempos."
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje5 +=1
        

    else: 
        if D=="3":
            puntaje5-=1
        
        



    # Pregunta 8
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 8: ¿Quién fue el primer jugador en ser campeón mundial tanto en ajedrez clásico como en ajedrez rápido? / 1 punto")
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Viswanathan Anand")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Garry Kasparov")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Magnus Carlsen")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "1"

    explicacion = "Explicación: Viswanathan Anand fue el primer jugador en ser campeón mundial tanto en ajedrez clásico como en ajedrez rápido."
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje5 +=1
        

    else: 
        if D=="3":
            puntaje5-=1
        
        


    # Pregunta 9
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 9: ¿Qué jugador se destacó por su dominio en la década de 1960 y es considerado uno de los mejores jugadores de ajedrez de la historia? / 1 punto")
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Boris Spassky")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Tigran Petrosian")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Bobby Fischer")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "2"

    explicacion = "Explicación: Bobby Fischer se destacó por su dominio en la década de 1960 y es considerado uno de los mejores jugadores de ajedrez de la historia."
    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje5 +=1
        

    else: 
        if D=="3":
            puntaje5-=1
        
        


    # Pregunta 10
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 10: ¿Quién es el acual capeón munidal de ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTRED_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "José Raúl Capablanca")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Alexander Alekhine")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Magnus Carlsen")
    print()
    print(Fore.LIGHTYELLOW_EX + "♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   " + RESET)
    print()
    opcioncorrecta = "3"

    explicacion = "Explicación: El actual campeón mundial es el noruego Magnus Carlsen, que ha mantenido su titulo desde 2013."

    R=evaluar()        
        
    if R== opcioncorrecta :
        puntaje5 +=1
        

    else: 
        if D=="3":
            puntaje5-=1
        
        
            
    if puntaje5 <0:
        puntaje5=0



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

            
                    RI= 10-puntaje5
                    T()
                    print()
                    print()
                    print(Fore.LIGHTYELLOW_EX+"----------------------------    has completado el nivel: 5   -------------------------------------------- "+RESET)
                    print()
                    print()
                    print(Fore.BLUE+"___ DIFICULTAD ELEGIDA: "+RESET+" >>>  "+str(D)+"  <<<")
                    print()
                    print()
                    print(Fore.BLUE+"___ Puntos obtenidos ---> "+RESET+str(puntaje5))
                    print()
                    print()
                    print(Fore.BLUE+"___ Respuestas incorrectas ---> "+RESET+str(RI))
                    print()
                    print(Fore.LIGHTYELLOW_EX+"---------------------------------------------------------------------------------------------------------------"+RESET)
                    print()
                    

        else:
            
                    RI= 10-puntaje5
                    T()
                    print()
                    print()
                    print(Fore.LIGHTYELLOW_EX+"----------------------------    has completado el nivel: 5   -------------------------------------------- "+RESET)
                    print()
                    print()
                    print(Fore.RED+"___ DIFICULTAD ELEGIDA: "+RESET+" >>>  "+str(D)+" (PUNTAJE NEGATIVO)  <<<")
                    print()
                    print()
                    print(Fore.BLUE+"___ Puntos obtenidos ---> "+RESET+str(puntaje5))
                    print()
                    print()
                    print(Fore.BLUE+"___ Respuestas incorrectas ---> "+RESET+str(RI))
                    print()
                    print(Fore.LIGHTYELLOW_EX+"---------------------------------------------------------------------------------------------------------------"+RESET)
                    print()
                    

    except:
                    RI= 10-puntaje5
                    T()
                    print()
                    print()
                    print(Fore.LIGHTYELLOW_EX+"----------------------------    has completado el nivel: 5   -------------------------------------------- "+RESET)
                    print()
                    print()
                    print(Fore.BLUE+"___ DIFICULTAD ELEGIDA: "+RESET+" >>>    <<<")
                    print()
                    print()
                    print(Fore.BLUE+"___ Puntos obtenidos ---> "+RESET+str(puntaje5))
                    print()
                    print()
                    print(Fore.BLUE+"___ Respuestas incorrectas ---> "+RESET+str(RI))
                    print()
                    print(Fore.LIGHTYELLOW_EX+"---------------------------------------------------------------------------------------------------------------"+RESET)
                    print()
                    


    return puntaje5

        

