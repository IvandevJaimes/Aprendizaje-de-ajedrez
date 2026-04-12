
import time 
import os
from colorama import*
import sys
import json
from TEORIA1 import*
from TEORIA2 import*
from TEORIA3 import*
from TEORIA4 import*
from TEORIA5 import *

from NIVEL1 import*
from NIVEL2 import *
from NIVEL3 import*
from NIVEL5 import*
from NIVEL4 import *
RESET="\033[0m"
def NIVELES():
  
    
    salir=0

    def LIMPIAR():
        sys.stdout.write('\033[F\033[K')
    
    
    with open('DIFICULTAD.json', 'r') as file:
            D=json.load(file)



    with open('usuario.json', 'r') as file:
            cargarU=json.load(file)

    try:
        with open('nivel_jugado.json', 'r') as file:
                nivel_jugado=json.load(file)

    except:
        nivel_jugado="0"

    try:
        with open('flag.json', 'r') as file:
            flag=json.load(file)

    except:
        flag="0"



               
               

    while nivel_jugado=="0":
        if D=="3":
            while flag =="0":
                t01()
                print()
                print()
                print()
                RE = Fore.LIGHTGREEN_EX+cargarU+" Ya has alcanzado los conocimientos necesarios para responder la trivia. Recuerda que estás en modo dificil asi que esta teoria se mostrará una sola vez"+RESET
                for char in RE :
                        print(char, end='', flush=True),time.sleep(0.02)
                print()
                print()
                for char in "Presiona cualquier tecla para continuar a la trivia... ":
                 print(char, end='', flush=True),time.sleep(0.001)
                msvcrt.getch()
                os.system('cls' if os.name == 'nt' else 'clear')
                flag="1"
                
                with open ('flag.json' , 'w') as file:
                    json.dump(flag, file)
                break

        else:
                t01()
                print()
                print()
                print()
                RE = Fore.LIGHTGREEN_EX+cargarU+" Ya has alcanzado los conocimientos necesarios para responder la trivia."+RESET

                for char in RE :
                        print(char, end='', flush=True),time.sleep(0.02)
                print()
                print()
                for char in "Presiona cualquier tecla para continuar a la trivia... ":
                    print(char, end='', flush=True),time.sleep(0.001)
                msvcrt.getch()
                os.system('cls' if os.name == 'nt' else 'clear')
                
        puntaje1 =nivel1()
                


        if puntaje1 > 4:
            nivel_jugado="1"
                    
            with open ('puntaje1.json' , 'w') as file:
                    json.dump(puntaje1, file)
            
            
            with open ('nivel_jugado.json' , 'w') as file:
                json.dump(nivel_jugado, file)

            REQ = Fore.LIGHTGREEN_EX+"¡EN HORABUENA ' "+cargarU+" ' has alcanzado el puntaje necesario para continuar con el siguiente nivel"+RESET
            for char in REQ :
                print(char, end='', flush=True),time.sleep(0.02)
            print()
            print()
            print(Fore.LIGHTBLUE_EX+"-------- 1. "+RESET+"Jugar siguiente nivel")
            print()
            print(Fore.LIGHTBLUE_EX+"-------- 2. "+RESET+"Salir")
            print()
            print()
            while True:
                try:
                        R=input(Fore.GREEN+"Elige una opción: "+RESET)
                        
                        if R not in ["1","2"]:
                            raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        break
                                    
                        
                except:
                        
                        LIMPIAR()
                        print(Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        print ("",end='', flush=True),time.sleep(2)
                        LIMPIAR()    

            if R=="1":
                
                LIMPIAR()
                for char in "De acuerdo. vamos a continuar con el siguiente nivel ":
                    print(char, end='', flush=True),time.sleep(0.02)
                print ("",end='', flush=True),time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                
                break
                    

            elif R=="2":
                salir=1
                LIMPIAR()
                for char in "Volviendo al menú principal...":
                    print(char, end='', flush=True),time.sleep(0.02)
                print ("",end='', flush=True),time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                break
     

           

        else:
            REQ = Fore.LIGHTRED_EX+"No has alcanzado los puntos necesarios para jugar el siguente nivel, deberás repetir el nivel "+RESET
            for char in REQ :
                print(char, end='', flush=True),time.sleep(0.02)
            print()
            print()
            print(Fore.LIGHTYELLOW_EX+"-------- 1. "+RESET+"Repetir nivel")
            print()
            print(Fore.LIGHTYELLOW_EX+"-------- 2. "+RESET+"Salir")
            print()
            print()
        
            while True:  
                try:
                    R=input(Fore.GREEN+"Elige una opción: "+RESET)
                    
                    if R not in ["1","2"]:
                        raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                    break
                                    
                        
                except:
                        
                        LIMPIAR()
                        print(Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        print ("",end='', flush=True),time.sleep(2)
                        LIMPIAR()    

            if R=="1":
                
                    LIMPIAR()
                    for char in "De acuerdo. vamos a repetir el nivel ":
                        print(char, end='', flush=True),time.sleep(0.02)
                    print ("",end='', flush=True),time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                



            elif R=="2":
                LIMPIAR()
                salir=1
                for char in "Volviendo al menú principal...":
                    print(char, end='', flush=True),time.sleep(0.02)
                print ("",end='', flush=True),time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                break

           

    
    while salir == 0 and nivel_jugado=="1":

        if D=="3":
            while flag =="1":
                t02()
                print()
                print()
                print()
                RE = Fore.LIGHTGREEN_EX+cargarU+" Ya has alcanzado los conocimientos necesarios para responder la trivia. Recuerda que estás en modo dificil asi que esta teoria se mostrará una sola vez"+RESET
                for char in RE :
                        print(char, end='', flush=True),time.sleep(0.02)
                print()
                print()
                for char in "Presiona cualquier tecla para continuar a la trivia... ":
                 print(char, end='', flush=True),time.sleep(0.001)
                msvcrt.getch()
                os.system('cls' if os.name == 'nt' else 'clear')
                flag="2"
                
                with open ('flag.json' , 'w') as file:
                    json.dump(flag, file)
                break

        else:
                t02()
                print()
                print()
                print()
                RE = Fore.LIGHTGREEN_EX+cargarU+" Ya has alcanzado los conocimientos necesarios para responder la trivia."+RESET

                for char in RE :
                        print(char, end='', flush=True),time.sleep(0.02)
                print()
                print()
                for char in "Presiona cualquier tecla para continuar a la trivia... ":
                    print(char, end='', flush=True),time.sleep(0.001)
                msvcrt.getch()
                os.system('cls' if os.name == 'nt' else 'clear')
                
        puntaje=nivel2()
        

        if puntaje > 4:
            
            with open ('puntaje.json' , 'w') as file:
                    json.dump(puntaje, file)
            
            nivel_jugado="2"
            with open ('nivel_jugado.json' , 'w') as file:
                json.dump(nivel_jugado, file)

            REQ = Fore.LIGHTGREEN_EX+"¡EN HORABUENA ' "+cargarU+" ' has alcanzado el puntaje necesario para continuar con el siguiente nivel"+RESET
            for char in REQ :
                print(char, end='', flush=True),time.sleep(0.02)
            print()
            print()
            print(Fore.LIGHTBLUE_EX+"-------- 1. "+RESET+"Jugar siguiente nivel")
            print()
            print(Fore.LIGHTBLUE_EX+"-------- 2. "+RESET+"Salir")
            print()
            print()
            while True:
                try:
                        R=input(Fore.GREEN+"Elige una opción: "+RESET)
                        
                        if R not in ["1","2"]:
                            raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        break
                                    
                        
                except:
                        
                        LIMPIAR()
                        print(Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        print ("",end='', flush=True),time.sleep(2)
                        LIMPIAR()    

            if R=="1":
                
                LIMPIAR()
                for char in "De acuerdo. vamos a continuar con el siguiente nivel ":
                    print(char, end='', flush=True),time.sleep(0.02)
                print ("",end='', flush=True),time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                
                break
                    

            elif R=="2":
                salir=1
                LIMPIAR()
                for char in "Volviendo al menú principal...":
                    print(char, end='', flush=True),time.sleep(0.02)
                print ("",end='', flush=True),time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                break
     

           

        else:
            REQ = Fore.LIGHTRED_EX+"No has alcanzado los puntos necesarios para jugar el siguente nivel, deberás repetir el nivel "+RESET
            for char in REQ :
                print(char, end='', flush=True),time.sleep(0.02)
            print()
            print()
            print(Fore.LIGHTYELLOW_EX+"-------- 1. "+RESET+"Repetir nivel")
            print()
            print(Fore.LIGHTYELLOW_EX+"-------- 2. "+RESET+"Salir")
            print()
            print()
        
            while True:  
                try:
                    R=input(Fore.GREEN+"Elige una opción: "+RESET)
                    
                    if R not in ["1","2"]:
                        raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                    break
                                    
                        
                except:
                        
                        LIMPIAR()
                        print(Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        print ("",end='', flush=True),time.sleep(2)
                        LIMPIAR()    

            if R=="1":
                
                    LIMPIAR()
                    for char in "De acuerdo. vamos a repetir el nivel ":
                        print(char, end='', flush=True),time.sleep(0.02)
                    print ("",end='', flush=True),time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                



            elif R=="2":
                LIMPIAR()
                salir=1
                for char in "Volviendo al menú principal...":
                    print(char, end='', flush=True),time.sleep(0.02)
                print ("",end='', flush=True),time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                break


    while salir == 0 and nivel_jugado=="2":

        if D=="3":
            while flag =="2":
                t03()
                print()
                print()
                print()
                RE = Fore.LIGHTGREEN_EX+cargarU+" Ya has alcanzado los conocimientos necesarios para responder la trivia. Recuerda que estás en modo dificil asi que esta teoria se mostrará una sola vez"+RESET
                for char in RE :
                        print(char, end='', flush=True),time.sleep(0.02)
                print()
                print()
                for char in "Presiona cualquier tecla para continuar a la trivia... ":
                 print(char, end='', flush=True),time.sleep(0.001)
                msvcrt.getch()
                os.system('cls' if os.name == 'nt' else 'clear')
                flag="3"
                
                with open ('flag.json' , 'w') as file:
                    json.dump(flag, file)
                break
        else:
                t03()
                print()
                print()
                print()
                RE = Fore.LIGHTGREEN_EX+"""' "+cargarU+" ' Ya has alcanzado los conocimientos necesarios para responder la trivia."""+RESET

                for char in RE :
                        print(char, end='', flush=True),time.sleep(0.02)
                print()
                print()
                for char in "Presiona cualquier tecla para continuar a la trivia... ":
                    print(char, end='', flush=True),time.sleep(0.001)
                msvcrt.getch()
                os.system('cls' if os.name == 'nt' else 'clear')
         
        puntaje3=nivel3()
        
        


        if puntaje3 > 4:
            with open ('puntaje3.json' , 'w') as file:
                    json.dump(puntaje3, file)                    


            nivel_jugado="3"
            with open ('nivel_jugado.json' , 'w') as file:
                 json.dump(nivel_jugado, file)
            REQ = Fore.LIGHTGREEN_EX+"¡EN HORABUENA ' "+cargarU+" ' has alcanzado el puntaje necesario para continuar con el siguiente nivel"+RESET
            for char in REQ :
                print(char, end='', flush=True),time.sleep(0.02)
            print()
            print()
            print(Fore.LIGHTBLUE_EX+"-------- 1. "+RESET+"Jugar siguiente nivel")
            print()
            print(Fore.LIGHTBLUE_EX+"-------- 2. "+RESET+"Salir")
            print()
            print()
            while True:
                try:
                        R=input(Fore.GREEN+"Elige una opción: "+RESET)
                        
                        if R not in ["1","2"]:
                            raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        break
                                    
                        
                except:
                        
                        LIMPIAR()
                        print(Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        print ("",end='', flush=True),time.sleep(2)
                        LIMPIAR()    

            if R=="1":
                
                LIMPIAR()
                for char in "De acuerdo. vamos a continuar con el siguiente nivel ":
                    print(char, end='', flush=True),time.sleep(0.02)
                print ("",end='', flush=True),time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                
                break
                    

            elif R=="2":
                salir=1
                LIMPIAR()
                for char in "Volviendo al menú principal...":
                    print(char, end='', flush=True),time.sleep(0.02)
                print ("",end='', flush=True),time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                break
     

           

        else:
            REQ = Fore.LIGHTRED_EX+"No has alcanzado los puntos necesarios para jugar el siguente nivel, deberás repetir el nivel "+RESET
            for char in REQ :
                print(char, end='', flush=True),time.sleep(0.02)
            print()
            print()
            print(Fore.LIGHTYELLOW_EX+"-------- 1. "+RESET+"Repetir nivel")
            print()
            print(Fore.LIGHTYELLOW_EX+"-------- 2. "+RESET+"Salir")
            print()
            print()
        
            while True:  
                try:
                    R=input(Fore.GREEN+"Elige una opción: "+RESET)
                    
                    if R not in ["1","2"]:
                        raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                    break
                                    
                        
                except:
                        
                        LIMPIAR()
                        print(Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        print ("",end='', flush=True),time.sleep(2)
                        LIMPIAR()    

            if R=="1":
                
                    LIMPIAR()
                    for char in "De acuerdo. vamos a repetir el nivel ":
                        print(char, end='', flush=True),time.sleep(0.02)
                    print ("",end='', flush=True),time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                



            elif R=="2":
                LIMPIAR()
                salir=1
                for char in "Volviendo al menú principal...":
                    print(char, end='', flush=True),time.sleep(0.02)
                print ("",end='', flush=True),time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                break








    while salir == 0 and nivel_jugado=="3":

        if D=="3":
            while flag =="3":
                t04()
                print()
                print()
                print()
                RE = Fore.LIGHTGREEN_EX+cargarU+" Ya has alcanzado los conocimientos necesarios para responder la trivia. Recuerda que estás en modo dificil asi que esta teoria se mostrará una sola vez"+RESET
                for char in RE :
                        print(char, end='', flush=True),time.sleep(0.02)
                print()
                print()
                for char in "Presiona cualquier tecla para continuar a la trivia... ":
                 print(char, end='', flush=True),time.sleep(0.001)
                msvcrt.getch()
                os.system('cls' if os.name == 'nt' else 'clear')
                flag="4"
                
                with open ('flag.json' , 'w') as file:
                    json.dump(flag, file)
                break
        else:
                t04()
                print()
                print()
                print()
                RE = Fore.LIGHTGREEN_EX+"""' "+cargarU+" ' Ya has alcanzado los conocimientos necesarios para responder la trivia."""+RESET

                for char in RE :
                        print(char, end='', flush=True),time.sleep(0.02)
                print()
                print()
                for char in "Presiona cualquier tecla para continuar a la trivia... ":
                    print(char, end='', flush=True),time.sleep(0.001)
                msvcrt.getch()
                os.system('cls' if os.name == 'nt' else 'clear')
         
        puntaje4=nivel4()
        
        


        if puntaje4 > 4:

            with open ('puntaje4.json' , 'w') as file:
                    json.dump(puntaje4, file)
            nivel_jugado="4"
            with open ('nivel_jugado.json' , 'w') as file:
                 json.dump(nivel_jugado, file)
            REQ = Fore.LIGHTGREEN_EX+"¡EN HORABUENA ' "+cargarU+" ' has alcanzado el puntaje necesario para continuar con el siguiente nivel"+RESET
            for char in REQ :
                print(char, end='', flush=True),time.sleep(0.02)
            print()
            print()
            print(Fore.LIGHTBLUE_EX+"-------- 1. "+RESET+"Jugar siguiente nivel")
            print()
            print(Fore.LIGHTBLUE_EX+"-------- 2. "+RESET+"Salir")
            print()
            print()
            while True:
                try:
                        R=input(Fore.GREEN+"Elige una opción: "+RESET)
                        
                        if R not in ["1","2"]:
                            raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        break
                                    
                        
                except:
                        
                        LIMPIAR()
                        print(Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        print ("",end='', flush=True),time.sleep(2)
                        LIMPIAR()    

            if R=="1":
                
                LIMPIAR()
                for char in "De acuerdo. vamos a continuar con el siguiente nivel ":
                    print(char, end='', flush=True),time.sleep(0.02)
                print ("",end='', flush=True),time.sleep(3)
                os.system('cls' if os.name == 'nt' else 'clear')
                
                break
                    

            elif R=="2":
                salir=1
                LIMPIAR()
                for char in "Volviendo al menú principal...":
                    print(char, end='', flush=True),time.sleep(0.02)
                print ("",end='', flush=True),time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                break
     

           

        else:
            REQ = Fore.LIGHTRED_EX+"No has alcanzado los puntos necesarios para jugar el siguente nivel, deberás repetir el nivel "+RESET
            for char in REQ :
                print(char, end='', flush=True),time.sleep(0.02)
            print()
            print()
            print(Fore.LIGHTYELLOW_EX+"-------- 1. "+RESET+"Repetir nivel")
            print()
            print(Fore.LIGHTYELLOW_EX+"-------- 2. "+RESET+"Salir")
            print()
            print()
        
            while True:  
                try:
                    R=input(Fore.GREEN+"Elige una opción: "+RESET)
                    
                    if R not in ["1","2"]:
                        raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                    break
                                    
                        
                except:
                        
                        LIMPIAR()
                        print(Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        print ("",end='', flush=True),time.sleep(2)
                        LIMPIAR()    

            if R=="1":
                
                    LIMPIAR()
                    for char in "De acuerdo. vamos a repetir el nivel ":
                        print(char, end='', flush=True),time.sleep(0.02)
                    print ("",end='', flush=True),time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                



            elif R=="2":
                LIMPIAR()
                salir=1
                for char in "Volviendo al menú principal...":
                    print(char, end='', flush=True),time.sleep(0.02)
                print ("",end='', flush=True),time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                break





    while salir == 0 and nivel_jugado=="4":

        if D=="3":
            while flag =="4":
                t05()
                print()
                print()
                print()
                RE = Fore.LIGHTGREEN_EX+cargarU+" Ya has alcanzado los conocimientos necesarios para responder la trivia. Recuerda que estás en modo dificil asi que esta teoria se mostrará una sola vez"+RESET
                for char in RE :
                        print(char, end='', flush=True),time.sleep(0.02)
                print()
                print()
                for char in "Presiona cualquier tecla para continuar a la trivia... ":
                 print(char, end='', flush=True),time.sleep(0.001)
                msvcrt.getch()
                os.system('cls' if os.name == 'nt' else 'clear')
                flag="5"
                
                with open ('flag.json' , 'w') as file:
                    json.dump(flag, file)
                break
        else:
                t05()
                print()
                print()
                print()
                RE = Fore.LIGHTGREEN_EX+"""' "+cargarU+" ' Ya has alcanzado los conocimientos necesarios para responder la trivia."""+RESET

                for char in RE :
                        print(char, end='', flush=True),time.sleep(0.02)
                print()
                print()
                for char in "Presiona cualquier tecla para continuar a la trivia... ":
                    print(char, end='', flush=True),time.sleep(0.001)
                msvcrt.getch()
                os.system('cls' if os.name == 'nt' else 'clear')
         
        puntaje5=nivel5()
        
        


        if puntaje5 > 4:
            
            with open ('puntaje5.json' , 'w') as file:
                    json.dump(puntaje5, file)
            nivel_jugado="5"
            with open ('nivel_jugado.json' , 'w') as file:
                 json.dump(nivel_jugado, file)
            REQ = Fore.LIGHTGREEN_EX+"¡EN HORABUENA ' "+cargarU+" ' has completado todos los niveles del modo desafio"+RESET
            for char in REQ :
                print(char, end='', flush=True),time.sleep(0.02)
            print()
            print()
                        
            for char in "Presiona cualquier tecla para ver tu devolución final... ":
                print(char, end='', flush=True),time.sleep(0.002)
            msvcrt.getch()
            os.system('cls' if os.name == 'nt' else 'clear')


        else:
            REQ = Fore.LIGHTRED_EX+"No has alcanzado los puntos necesarios para ganar, deberás repetir el nivel "+RESET
            for char in REQ :
                print(char, end='', flush=True),time.sleep(0.02)
            print()
            print()
            print(Fore.LIGHTYELLOW_EX+"-------- 1. "+RESET+"Repetir nivel")
            print()
            print(Fore.LIGHTYELLOW_EX+"-------- 2. "+RESET+"Salir")
            print()
            print()
        
            while True:  
                try:
                    R=input(Fore.GREEN+"Elige una opción: "+RESET)
                    
                    if R not in ["1","2"]:
                        raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                    break
                                    
                        
                except:
                        
                        LIMPIAR()
                        print(Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        print ("",end='', flush=True),time.sleep(2)
                        LIMPIAR()    

            if R=="1":
                
                    LIMPIAR()
                    for char in "De acuerdo. vamos a repetir el nivel ":
                        print(char, end='', flush=True),time.sleep(0.02)
                    print ("",end='', flush=True),time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    
                



            elif R=="2":
                LIMPIAR()
                salir=1
                for char in "Volviendo al menú principal...":
                    print(char, end='', flush=True),time.sleep(0.02)
                print ("",end='', flush=True),time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                break





    while nivel_jugado=="5":
        with open('puntaje.json', 'r') as file:
                puntaje=json.load(file)

        with open('puntaje1.json', 'r') as file:
                puntaje1=json.load(file)

        with open('puntaje.json', 'r') as file:
                puntaje2=json.load(file)

        with open('puntaje3.json', 'r') as file:
                puntaje3=json.load(file)

        with open('puntaje4.json', 'r') as file:
                puntaje4=json.load(file)
    
        with open('puntaje5.json', 'r') as file:
                puntaje5=json.load(file)

        PF=puntaje+puntaje1+puntaje2+puntaje3+puntaje4+puntaje5
        with open ('PF.json' , 'w') as file:
                    json.dump(PF, file)

        print()
        print(Fore.LIGHTMAGENTA_EX+" ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)
        print()
        print(Fore.LIGHTWHITE_EX+"                                                                 ¡ MODO DESAFIO COMPLETADO !"+RESET)
        print()
        print(Fore.LIGHTMAGENTA_EX+" ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"+RESET)
        print()
        print()
        print(Fore.LIGHTGREEN_EX+"----------------------------------------------------------------------------------------------------------------------------------------------------------"+RESET)
        print()
        print(Fore.LIGHTYELLOW_EX+"       DEVOLUCIÖN FINAL: "+RESET)
        print()
        print(Fore.LIGHTBLUE_EX+"---- USUARIO: "+RESET+cargarU)
        print()
        print()
        print(Fore.LIGHTBLUE_EX+"---- PUNTOS TOTALES: "+RESET+str(PF))
        print()
        print()
        print(Fore.LIGHTGREEN_EX+"¡Gracias por jugar!"+RESET)
        print()
        print()
        print()
        print()
        print()
        for char in "Presiona cualquier tecla para salir... ":
            print(char, end='', flush=True),time.sleep(0.002)
        msvcrt.getch()
        os.system('cls' if os.name == 'nt' else 'clear')
        break




