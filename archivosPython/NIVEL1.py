
RESET="\033[0m"




import sys
import time 
import os
import msvcrt
from colorama import*
import json
import threading
import keyboard


def nivel1():
    puntaje1=0
    
    




    
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
    print(Fore.LIGHTMAGENTA_EX +"▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)
    print()
    print("           Pregunta 1: ¿Cuál es el movimiento correcto del peón? / 1 punto")
    print()
    print(Fore.LIGHTMAGENTA_EX +"▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX+"         .......... OPCIONES .......... "+RESET)
    print()
    print(Fore.LIGHTBLUE_EX+"      ______ 1: "+RESET+"Una casilla hacia adelante")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX+"      ______ 2: "+RESET+"Dos casillas hacia adelante siempre")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX+"      ______ 3: "+RESET+"En diagonal hacia adelante")
    print()
    print(Fore.LIGHTYELLOW_EX+"♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ "+RESET)
    print()
    
    opcioncorrecta = "1"
    explicacion="Explicación: El peón normalmente se mueve una casilla hacia adelante." 
    

   
    


    R=evaluar()        
      
    if R== opcioncorrecta :
       puntaje1 +=1
    

    
        
  
    
     
    
   
    




    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 2: ¿Cómo se mueve la torre? / 1 punto")
    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Diagonal")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Horizontal y vertical")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "En L")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()

    opcioncorrecta = "2"
    explicacion = "Explicación: La torre se mueve en líneas rectas, tanto en horizontal como en vertical, cualquier número de casillas."


    R=evaluar()        
      
    if R== opcioncorrecta :
       puntaje1 +=1
       

    else: 
        
        if D=="3":
            puntaje1-=1
    
    

    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 3: ¿Cuál es el movimiento del caballo? / 1 punto")
    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Diagonal")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Horizontal y vertical")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "En L")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()
    opcioncorrecta = "3"
    explicacion = "Explicación: El caballo se mueve en forma de 'L', dos casillas en una dirección y una casilla en perpendicular."



    R=evaluar()        
      
     
    if R== opcioncorrecta :
       puntaje1 +=1
       

    else: 
        
        if D=="3":
            puntaje1-=1
      
    


    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 4: ¿Qué pieza puede moverse en cualquier dirección cualquier número de casillas? / 1 punto")
    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Reina")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Rey")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Alfil")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()


    opcioncorrecta = "1"
    explicacion = "Explicación: La reina puede moverse en líneas rectas (horizontal, vertical y diagonal) cualquier número de casillas."



    R=evaluar()        
      
 
    if R== opcioncorrecta :
       puntaje1 +=1
       

    else: 
        
        if D=="3":
            puntaje1-=1
        
    

    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 5: ¿Qué pieza se mueve solo una casilla en cualquier dirección? / 1 punto")
    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Rey")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Peón")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Caballo")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()

    opcioncorrecta = "1"
    explicacion = "Explicación: El rey se mueve una casilla en cualquier dirección: vertical, horizontal o diagonal."


    R=evaluar()        
      
    if R== opcioncorrecta :
       puntaje1 +=1
       

    else: 
        
        if D=="3":
            puntaje1-=1

    


    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 6: ¿Qué pieza puede saltar sobre otras piezas? / 1 punto")
    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Reina")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Torre")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Caballo")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()
    opcioncorrecta = "3"
    explicacion = "Explicación: El caballo es la única pieza que puede saltar sobre otras en su movimiento en forma de 'L'."


    R=evaluar()        
      
   
    if R== opcioncorrecta :
       puntaje1 +=1
       

    else: 
        
        if D=="3":
            puntaje1-=1
    
    

    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀" + RESET)
    print()
    print("           Pregunta 7: ¿Cuál es el movimiento del alfil? / 1 punto")
    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Horizontal y vertical")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Diagonal")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "En L")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()
    opcioncorrecta = "2"
    explicacion = "Explicación: El alfil se mueve únicamente en diagonal, cualquier número de casillas."


    R=evaluar()        
       
    if R== opcioncorrecta :
       puntaje1 +=1
       

    else: 
        
        if D=="3":
            puntaje1-=1
     


    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 8: ¿Cuántas casillas puede moverse el peón en su primer movimiento? / 1 punto")
    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Una casilla")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Tres casillas")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Dos casillas")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()
    opcioncorrecta = "3"
    explicacion = "Explicación: En su primer movimiento, el peón puede avanzar dos casillas en lugar de una."


    R=evaluar()        
      
    if R== opcioncorrecta :
       puntaje1 +=1
       

    else: 
        
        if D=="3":
            puntaje1-=1
     
    


    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 9: ¿Cuál es el objetivo principal del ajedrez? / 1 punto")
    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Capturar todas las piezas del oponente")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Colocar al rey del oponente en jaque mate")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Mover todas las piezas a la última fila")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()

    opcioncorrecta = "2"
    explicacion = "Explicación: El objetivo principal es colocar al rey del oponente en jaque mate, lo que significa que está amenazado y no tiene movimientos legales para escapar."


    R=evaluar()        
      
    if R== opcioncorrecta :
       puntaje1 +=1
       

    else: 
        
        if D=="3":
            puntaje1-=1
  
    


    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print("           Pregunta 10: ¿Al momento de empezar la partida, qué color de piezas debe mover primero? / 1 punto")
    print()
    print(Fore.LIGHTMAGENTA_EX + "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄" + RESET)
    print()
    print()
    print()
    print(Fore.LIGHTGREEN_EX + "         .......... OPCIONES .......... " + RESET)
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 1: " + RESET + "Negras")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 2: " + RESET + "Se decide por sorteo")
    print()
    print()
    print()
    print(Fore.LIGHTBLUE_EX + "      ______ 3: " + RESET + "Blancas")
    print()
    print(Fore.LIGHTYELLOW_EX + "♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘ " + RESET)
    print()

    opcioncorrecta = "3"
    explicacion = "Explicación: Las blancas siempre tienen el primer turno en una partida de ajedrez."

    R=evaluar()        
      
    if R== opcioncorrecta :
       puntaje1 +=1
       

    else: 
        if D=="3":
            puntaje1-=1
       
        
            
    if puntaje1 <0:
        puntaje1=0
  
    



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

            
                    RI= 10-puntaje1
                    T()
                    print()
                    print()
                    print(Fore.LIGHTYELLOW_EX+"----------------------------    has completado el nivel: 1   -------------------------------------------- "+RESET)
                    print()
                    print()
                    print(Fore.BLUE+"___ DIFICULTAD ELEGIDA: "+RESET+" >>>  "+str(D)+"  <<<")
                    print()
                    print()
                    print(Fore.BLUE+"___ Puntos obtenidos ---> "+RESET+str(puntaje1))
                    print()
                    print()
                    print(Fore.BLUE+"___ Respuestas incorrectas ---> "+RESET+str(RI))
                    print()
                    print(Fore.LIGHTYELLOW_EX+"---------------------------------------------------------------------------------------------------------------"+RESET)
                    print()
                    

        else:
            
                    RI= 10-puntaje1
                    T()
                    print()
                    print()
                    print(Fore.LIGHTYELLOW_EX+"----------------------------    has completado el nivel: 1   -------------------------------------------- "+RESET)
                    print()
                    print()
                    print(Fore.RED+"___ DIFICULTAD ELEGIDA: "+RESET+" >>>  "+str(D)+" (PUNTAJE NEGATIVO)  <<<")
                    print()
                    print()
                    print(Fore.BLUE+"___ Puntos obtenidos ---> "+RESET+str(puntaje1))
                    print()
                    print()
                    print(Fore.BLUE+"___ Respuestas incorrectas ---> "+RESET+str(RI))
                    print()
                    print(Fore.LIGHTYELLOW_EX+"---------------------------------------------------------------------------------------------------------------"+RESET)
                    print()
                    

    except:
                    RI= 10-puntaje1
                    T()
                    print()
                    print()
                    print(Fore.LIGHTYELLOW_EX+"----------------------------    has completado el nivel: 1   -------------------------------------------- "+RESET)
                    print()
                    print()
                    print(Fore.BLUE+"___ DIFICULTAD ELEGIDA: "+RESET+" >>>    <<<")
                    print()
                    print()
                    print(Fore.BLUE+"___ Puntos obtenidos ---> "+RESET+str(puntaje1))
                    print()
                    print()
                    print(Fore.BLUE+"___ Respuestas incorrectas ---> "+RESET+str(RI))
                    print()
                    print(Fore.LIGHTYELLOW_EX+"---------------------------------------------------------------------------------------------------------------"+RESET)
                    print()
                        

    return puntaje1
    
        

