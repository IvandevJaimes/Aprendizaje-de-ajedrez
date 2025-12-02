import time 
import os
from colorama import*
import sys
import json
from TEORIA1 import*
from TEORIA2 import*
from TEORIA3 import*
from TEORIA4 import*
from TEORIA5 import*
from NIVEL1 import*
from NIVEL2 import *
from NIVEL3 import*
from NIVEL4 import*
from NIVEL5 import *



def LIBRE():

    


    def PCT ():
        print()
        print()
        print()
        print()
        for char in "Presiona cualquier tecla para volver... ":
            print(char, end='', flush=True),time.sleep(0.001)
        msvcrt.getch()
        os.system('cls' if os.name == 'nt' else 'clear')


    

    def LIMPIAR():
        sys.stdout.write('\033[F\033[K')
        
    def T():
        print()
        print(Fore.LIGHTGREEN_EX+"""  ---------------------------------------------------------------- Bienvenido al modo libre -------------------------------------------------------------------------"""+RESET)   
        print()
        print()


    while True:
        T()

        for char in """Este es el modo libre, aqui puedes jugar cualquier nivel, o elegir el aprendizaje que desees. """:
                print(char, end='', flush=True),time.sleep(0.02)
        print()
        print()
        print(Fore.LIGHTMAGENTA_EX+"#############################################################################  NIVELES  ############################################################################# "+RESET)
        print()
        print(Fore.LIGHTGREEN_EX+"-----1."+RESET+"  NIVEL 1                     "+Fore.LIGHTGREEN_EX+"-----2."+RESET+"  NIVEL 2")
        print()
        print()
        print(Fore.LIGHTGREEN_EX+"-----3."+RESET+"  NIVEL 3                     "+Fore.LIGHTGREEN_EX+"-----4."+RESET+"  NIVEL 4")
        print()
        print()
        print(Fore.LIGHTGREEN_EX+"-----5."+RESET+"  NIVEL 5")
        print()
        print(Fore.LIGHTBLUE_EX+"###########################################################################  APRENDIZAJE  ########################################################################### "+RESET)
        print()
        print(Fore.LIGHTCYAN_EX+"-----6."+RESET+"  APRENDIZAJE 1                "+Fore.LIGHTCYAN_EX+"-----7."+RESET+"  APRENDIZAJE 2")
        print()
        print()
        print(Fore.LIGHTCYAN_EX+"-----8."+RESET+"  APRENDIZAJE 3                "+Fore.LIGHTCYAN_EX+"-----9."+RESET+"  APRENDIZAJE 4")
        print()
        print()
        print(Fore.LIGHTCYAN_EX+"-----10."+RESET+"  APRENDIZAJE 5 ")
        print()
        print()
        print(Fore.LIGHTYELLOW_EX+"-----11. SALIR -----"+RESET)
        print()
        print(Fore.LIGHTMAGENTA_EX+"#################################################################################################################################################################### "+RESET)
        print()
        while True:
                    try:
                            R=input(Fore.GREEN+"Elige una opción: "+RESET)
                            
                            if R not in ["1","2","3","4","5","6","7","8","9",'10','11']:
                                raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                            break
                                        
                            
                    except:
                            
                            LIMPIAR()
                            print(Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                            print ("",end='', flush=True),time.sleep(2)
                            LIMPIAR()    
        
        if R== "1":
            LIMPIAR()
            for char in "¡Vamos a jugar el nivel 1":
                print(char, end='', flush=True),time.sleep(0.02)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            nivel1()
            print()
            PCT()
            
        elif R== "2":
            LIMPIAR()
            for char in "¡Vamos a jugar el nivel 2":
                print(char, end='', flush=True),time.sleep(0.02)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            nivel2()
            PCT()
            

        elif R== "3":
            LIMPIAR()
            for char in "¡Vamos a jugar el nivel 3":
                print(char, end='', flush=True),time.sleep(0.02)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            nivel3()
            PCT()

        elif R== "4":
            LIMPIAR()
            for char in "¡Vamos a jugar el nivel 4":
                print(char, end='', flush=True),time.sleep(0.02)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            nivel4()
            PCT()

        elif R== "5":
            LIMPIAR()
            for char in "¡Vamos a jugar el nivel 5":
                print(char, end='', flush=True),time.sleep(0.02)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            nivel5()
            PCT()


        elif R== "6":
            LIMPIAR()
            for char in "¡Vamos a ver la teoria del nivel 1":
                print(char, end='', flush=True),time.sleep(0.02)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            t01()
            PCT()

        
        elif R== "7":
            LIMPIAR()
            for char in "¡Vamos a ver la teoria del nivel 2":
                print(char, end='', flush=True),time.sleep(0.02)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            t02()
            PCT()

        
        elif R== "8":
            LIMPIAR()
            for char in "¡Vamos a ver la teoria del nivel 3":
                print(char, end='', flush=True),time.sleep(0.02)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            t03()
            PCT()

        elif R== "9":
            LIMPIAR()
            for char in "¡Vamos a ver la teoria del nivel 4":
                print(char, end='', flush=True),time.sleep(0.02)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            t04()
            PCT()

        elif R== "10":
            LIMPIAR()
            for char in "¡Vamos a ver la teoria del nivel 5":
                print(char, end='', flush=True),time.sleep(0.02)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            t05()
            PCT()


        
        elif R== "11":
            LIMPIAR()
            for char in "Volviendo al menú principal...":
                print(char, end='', flush=True),time.sleep(0.02)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            break
            

            
            

            
            

            
            

            


            