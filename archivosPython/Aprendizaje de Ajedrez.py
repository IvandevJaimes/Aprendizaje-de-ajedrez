

#colores
ROJO="\033[31m"
VERDE="\033[32m"
AMARILLO="\033[33m"
RESET="\033[0m"
NEGRITA_CIAN="\033[1;36m"



from TEORIA1 import *
from colorama import *
import time 
import os
import msvcrt
from DESAFIO import *
from NIVEL1 import*
import sys

from MLIBRE import*

print(os.getcwd())


init()

          
               








os.system('cls' if os.name == 'nt' else 'clear')
print()
for char in Fore.LIGHTYELLOW_EX+"Para disfrutar de una mejor experiencia de juego y evitar problemas asegurate de maximizar la pantalla. ¡Muchas gracias! "+RESET:
    print(char, end='', flush=True),time.sleep(0.02)
print()
print()
print()
print()
print()
for char in "Presiona cualquier tecla para continuar... ":
                print(char, end='', flush=True),time.sleep(0.001)
msvcrt.getch()
os.system('cls' if os.name == 'nt' else 'clear')









init()

def pantalla_inicio():
    
    print("\033c", end="")

            
    print(Fore.LIGHTWHITE_EX+"""         
        ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"""+RESET)
    titulo = """                                                                                      
                                 █████╗ ██████╗ ██████╗ ███████╗███╗   ██╗██████╗ ██╗███████╗ █████╗      ██╗███████╗    ██████╗ ███████╗     
                                ██╔══██╗██╔══██╗██╔══██╗██╔════╝████╗  ██║██╔══██╗██║╚══███╔╝██╔══██╗     ██║██╔════╝    ██╔══██╗██╔════╝    
                                ███████║██████╔╝██████╔╝█████╗  ██╔██╗ ██║██║  ██║██║  ███╔╝ ███████║     ██║█████╗      ██║  ██║█████╗       
                                ██╔══██║██╔═══╝ ██╔══██╗██╔══╝  ██║╚██╗██║██║  ██║██║ ███╔╝  ██╔══██║██   ██║██╔══╝      ██║  ██║██╔══╝        
                                ██║  ██║██║     ██║  ██║███████╗██║ ╚████║██████╔╝██║███████╗██║  ██║╚█████╔╝███████╗    ██████╔╝███████╗                                                                                                                                                                                                                                     
                                                         █████╗      ██╗███████╗██████╗ ██████╗ ███████╗███████╗
                                                        ██╔══██╗     ██║██╔════╝██╔══██╗██╔══██╗██╔════╝╚══███╔╝
                                                        ███████║     ██║█████╗  ██║  ██║██████╔╝█████╗    ███╔╝
                                                        ██╔══██║██   ██║██╔══╝  ██║  ██║██╔══██╗██╔══╝   ███╔╝
                                                        ██║  ██║╚█████╔╝███████╗██████╔╝██║  ██║███████╗███████╗
    """
    print(Fore.LIGHTYELLOW_EX + titulo + Style.RESET_ALL)
        
        
    print(Fore.LIGHTWHITE_EX+"""         ▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄"""+RESET)

    ver="                                                                                                                                               versión: 1.01"
    print(Fore.LIGHTYELLOW_EX + ver + RESET)      

    
    menu = """
         ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   

                                             ------------------------------------------------------------------------------
                                             |                                                                            |
                                             |  1. Nuevo juego Modo desafío                     5. Instrucciones          | 
                                             |                                                                            |
                                             |  2. Nuevo juego Modo adivinanzas                 6. Créditos               |
                                             |                                                                            |
                                             |  3. Modo libre                                   7. Salir                  |
                                             |                                                                            |
                                             |  4. Cargar o Borrar partida                                                |
                                             |                                                                            |
                                             ------------------------------------------------------------------------------    
                                                                                   
         ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛   ♚   ♝   ♞   ♜   ♟   ♜   ♞   ♝   ♛                                                         
"""
    print(Fore.LIGHTCYAN_EX + menu + Style.RESET_ALL)
    return pantalla_inicio
















def LIMPIAR():
    sys.stdout.write('\033[F\033[K')   

while(True):
    pantalla_inicio()
    print()
    print()
    R=input(Fore.GREEN + "Elige una opción: " + Style.RESET_ALL)
    try:

        
        if R not in ["1","2","3","4","5","6","7"]:
            raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        
            
    except:
            
            LIMPIAR()
            print(Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
            print ("",end='', flush=True),time.sleep(2)
            LIMPIAR()
            
            
            
            

      
    if R == "1":
        os.system('cls' if os.name == 'nt' else 'clear')

        inicio()
        
       
    if R=="2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print(Fore.LIGHTWHITE_EX+"                                                                    MODO ADIVINANZAS"+RESET)
        print(Fore.LIGHTMAGENTA_EX+"*********************************************************************************************************************************************************"+RESET)
        print()
        print()
        print()
        print(Fore.LIGHTGREEN_EX+"¡EL MODO ADIVINANZAS ESTARÁ DISPONIBLE EN UNA PRÓXIMA ACTUALIZACIÓN!")
        print()
        print()
        print()
        for char in "Presiona cualquier tecla para volver... ":
            print(char, end='', flush=True),time.sleep(0.001)
        msvcrt.getch()
            


    if R=="3":
        os.system('cls' if os.name == 'nt' else 'clear')
        LIBRE()
        
    
            
        


        
            

        


        

    
    if R=="5":


        os.system('cls' if os.name == 'nt' else 'clear')
        II=""">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> INSTRUCCIONES DEL JUEGO DE APRENDIZAJE DE AJEDREZ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<""" 
        
        instrucciones = """
            
            {}1. Modo desafío:{} Responde correctamente a preguntas de opción múltiple relacionadas con ajedrez
            para obtener la mayor puntuación posible. Antes de responder la trivia se mostrará la teoría de
            cada nivel para que adquieras el conocimiento necesario para responder las preguntas. Al final 
            del nivel se mostrará la puntuación obtenida siendo necesario una puntuación mayor a 4 para 
            poder desbloquear el siguiente nivel.

            {}2. Modo libre:{} En el modo libre podras seleccionar desde su mismo menú, cualquier nivel o
            cuialquier aprendizaje. Este modo de juego funciona sin guardado de partida.
           
            {}3. Modo adivinanzas:{} En este modo de juego deberás responder una serie de adivinanzas para
            obtener la mayor puntuación posible.
            
            {}4. Navegación:{} 
            - Usa los números del menú principal para navegar entre las opciones.
            - Selecciona 'Instrucciones' en cualquier momento para revisar estas instrucciones.

        
            """.format(Fore.YELLOW, Style.RESET_ALL, Fore.YELLOW, Style.RESET_ALL, Fore.YELLOW, Style.RESET_ALL, Fore.YELLOW, Style.RESET_ALL, Fore.YELLOW, Style.RESET_ALL)
        print()
        print(Fore.MAGENTA+II+RESET)
        print()
        print()
        for I2 in instrucciones:
            print(I2, end='', flush=True),time.sleep(0.004)
        
        print()
        print()
        print()
        print()
        for char in "Presiona cualquier tecla para volver... ":
                print(char, end='', flush=True),time.sleep(0.001)
        msvcrt.getch()
        os.system('cls' if os.name == 'nt' else 'clear')
        
    
            

        
                
    

                        
    if R=="6":
        os.system('cls' if os.name == 'nt' else 'clear')
        
        

    
        print(Fore.LIGHTBLUE_EX+ """
=====================================================================================================================================================================
                                                                            CRÉDITOS
====================================================================================================================================================================="""+RESET)


        print(Fore.LIGHTYELLOW_EX+"""
        Desarrollado por: Ivan Jaimes 
        Año: 2024""" +RESET)
        

        print(Fore.CYAN + Style.BRIGHT + """
        Diseño de Juego: Ivan Jaimes
    
            Arte: Ivan Jaimes"""+RESET)
        print()
        
        

        

        print(Fore.WHITE + Style.BRIGHT + """     Copyright © IVANJ. Todos los derechos reservados."""+RESET)
        print()
        
        print(Fore.LIGHTWHITE_EX+""" 
              

                   ██    ██ ████████  ███   ██
                   ██    ██    ██     ████  ██                         
                   ██    ██    ██     ██ ██ ██
                   ██    ██    ██     ██ ██ ██
                    ██████     ██     ██  ████
        
                        ██     ██     ██ 
                        ██     ██     ██                 
                          ██   ██   ██ 
                            ██ ██ ██ 
                        ████████████████
                            ██ ██ ██ 
                          ██   ██   ██ 
                        ██     ██     ██ 
                        ██     ██     ██ 
"""+RESET)


        
        for char in "Presiona cualquier tecla para volver... ":
                print(char, end='', flush=True),time.sleep(0.001)
        msvcrt.getch()
        os.system('cls' if os.name == 'nt' else 'clear')

          

            
    
        

    if R=="4":  
     
            try:
               
                with open('usuario.json', 'r') as file:
                                    cargarU=json.load(file)

                
                TT="t"
            except:
                 TT="f"

            

            if TT=="t":

                try:
                    with open('nivel_jugado.json', 'r') as file:
                     NJ=json.load(file)
                except:
                    NJ="0"

                if NJ =="0":
                     NPJ=5
                    
                if NJ=="1":
                     NPJ=4
                
                if NJ=="2":
                     NPJ=3
                if NJ=="3":
                     NPJ=2
                if NJ=="4":
                     NPJ=1
                if NJ=="5":
                     NPJ=0
                
                    
                    

                os.system('cls' if os.name == 'nt' else 'clear')
                def T():
                    print(Style.BRIGHT + Fore.CYAN + Back.BLACK + "====================================================================================================================================================================="+RESET )
                    print(Style.BRIGHT + Fore.WHITE + "                                                                    CARGAR \ BORRAR PARTIDA"+RESET)
                    print(Style.BRIGHT + Fore.CYAN + Back.BLACK + "====================================================================================================================================================================="+RESET )
                    print()
                T()
                print()
                print()
                print(Fore.LIGHTMAGENTA_EX+"-----------------------------------------------------------------------------------------------------------------------------------------------------"+RESET)
                print()
                print(Fore.LIGHTBLUE_EX+".... 1-"+RESET+" Cargar partida ")
                print()
                print()
                print(Fore.LIGHTBLUE_EX+".... 2-"+RESET+" Eliminar progreso ")
                print()
                print()
                print(Fore.LIGHTYELLOW_EX+".... 3- Volver "+RESET)
                print()
                print(Fore.LIGHTMAGENTA_EX+"-----------------------------------------------------------------------------------------------------------------------------------------------------"+RESET)               
                print()   
                while True:
                    try:
                            R=input(Fore.GREEN+"Elige una opción: "+RESET)
                            
                            if R not in ["1","2","3"]:
                                raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                            break
                                        
                            
                    except:
                            
                            LIMPIAR()
                            print(Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                            print ("",end='', flush=True),time.sleep(2)
                            LIMPIAR()    

                if R=="1":
                    
                    if NJ =="5":
                        os.system('cls' if os.name == 'nt' else 'clear')
                        try:
                             
                            with open('PF.json', 'r') as file:
                                PF=json.load(file)
                        except:
                             PF=0
                        print(Style.BRIGHT + Fore.CYAN + Back.BLACK + "====================================================================================================================================================================="+RESET )
                        print(Style.BRIGHT + Fore.WHITE + "                                                                                MENU DE CARGA DE PARTIDA"+RESET)
                        print(Style.BRIGHT + Fore.CYAN + Back.BLACK + "====================================================================================================================================================================="+RESET )
                        print()
                        print()
                        
                        print()
                        print()
                        print()
                        print(Fore.LIGHTGREEN_EX+">>>>>>>>>>>>>>>>>>>>>>>>>>>  Partida Guardada  <<<<<<<<<<<<<<<<<<<<<<<<<<"+RESET)
                        print()
                        print(Fore.BLUE+"Usuario 1: "+RESET+cargarU+" >>>  MODO DESAFIO COMPLETADO  <<<")
                        print()
                        print(Fore.BLUE+"---- Niveles ganados: "+RESET+str(NJ))
                        print()
                        print(Fore.BLUE+"---- Niveles por jugar: "+RESET+str(NPJ))
                        print()
                        print(Fore.BLUE+"---- PUNTAJE TOTAL: "+RESET+str(PF))
                        print()
                        print(Fore.LIGHTGREEN_EX+"-------------------------------------------------------------------------"+RESET)
                        print()
                        print()
                        for char in Fore.LIGHTYELLOW_EX+"Ya has completado el modo desafio. si deseas volver a jugarlo puedes inciar una nueva partida en modo desafio desde el menú principal "+RESET:
                            print(char, end='', flush=True),time.sleep(0.02)
                        print()
                        print()
                        print()
                        for char in "Presiona cualquier tecla para volver... ":
                            print(char, end='', flush=True),time.sleep(0.001)
                        msvcrt.getch()
                        os.system('cls' if os.name == 'nt' else 'clear')

                        

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        def TI():
                    
                            print(Style.BRIGHT + Fore.CYAN + Back.BLACK + "====================================================================================================================================================================="+RESET )
                            print(Style.BRIGHT + Fore.WHITE + "                                                                                MENU DE CARGA DE PARTIDA"+RESET)
                            print(Style.BRIGHT + Fore.CYAN + Back.BLACK + "====================================================================================================================================================================="+RESET )
                            print()
                            print()
                        
                        TI()
                
                                    
                        print()
                        print()
                        print()
                        print(Fore.LIGHTGREEN_EX+">>>>>>>>>>>>>>>>>>>>>>>>>>>  Partida Guardada  <<<<<<<<<<<<<<<<<<<<<<<<<<"+RESET)
                        print()
                        print(Fore.BLUE+"Usuario 1: "+RESET+cargarU+" >>>  MODO DESAFIO <<<")
                        print()
                        print(Fore.BLUE+"---- Niveles ganados: "+RESET+str(NJ))
                        print()
                        print(Fore.BLUE+"---- Niveles por jugar: "+RESET+str(NPJ))
                        print()
                        print(Fore.LIGHTGREEN_EX+"-------------------------------------------------------------------------"+RESET)
                        print()
                        print()

                        while (True):
                            try:
                                R1=input("¿Quieres cargar la partida y continuar donde lo dejaste? (Si/No): ")
                                R1=R1.upper()
                                if R1 not in ["SI","NO","S","N"]:
                                    raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                                    
                                break
                            except ValueError as E :
                                LIMPIAR()
                                print(E)
                                print ("",end='', flush=True),time.sleep(2)
                                LIMPIAR()
                        
                        if R1== "SI" or R1=="S":
                                print()
                                print()
                                for char in Fore.LIGHTYELLOW_EX+"¡De acuerdo! vamos a continuar donde lo dejaste la última vez  "+RESET:
                                    print(char, end='', flush=True),time.sleep(0.02)
                                print ("",end='', flush=True),time.sleep(2)

                                os.system('cls' if os.name == 'nt' else 'clear')
                                NIVELES()
                            
                        
                        elif R1=="NO" or R1=="N":
                            print()
                            print()
                            for char in Fore.LIGHTYELLOW_EX+"Volviendo al menú principal... "+RESET:
                                print(char, end='', flush=True),time.sleep(0.02)
                            print ("",end='', flush=True),time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            
                        
                        

                elif R=="2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    T()

        
                    for char in Fore.LIGHTRED_EX+"¡ADVERTENCIA! "+RESET+"Si eliminas tu progreso perderas tu partida guardada, tu usuario y tu contraseña":
                        print(char, end='', flush=True),time.sleep(0.001)
                    print()
                    print()
                    print()
                    print()
                    print()
                    while (True):
                        try:
                            R1=input("¿Quieres borrar tu progreso definitivamnete? (Si/No): ")
                            R1=R1.upper()
                            if R1 not in ["SI","NO","S","N"]:
                                raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                                
                            break
                        except ValueError as E :
                            LIMPIAR()
                            print(E)
                            print ("",end='', flush=True),time.sleep(2)
                            LIMPIAR()
                


                    if R1== "SI" or R1=="S":
                            print()
                            print()
                            ELIMINAR=['usuario.json','contra.json','nivel_jugado.json','DIFICULTAD.json','flag.json','puntaje.json','puntaje1.json','puntaje2.json','puntaje3.json','puntaje4.json','puntaje5.json','PF.json']
                            for filename in ELIMINAR:
                                if os.path.exists(filename):
                                    os.remove(filename)



                            for char in Fore.LIGHTYELLOW_EX+"BORRANDO PROGRESO... "+RESET:
                                print(char, end='', flush=True),time.sleep(0.01)
                            print ("",end='', flush=True),time.sleep(3)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print()
                            print(Fore.GREEN+"PROGRESO ELIMINADO CORRECTAMENTE"+RESET)
                            print ("",end='', flush=True),time.sleep(2)
                            os.system('cls' if os.name == 'nt' else 'clear')

                        
                        
                                
                                    
                    elif R1=="NO" or R1=="N":
                        print()
                        print()
                        for char in Fore.LIGHTYELLOW_EX+"Volviendo al menú principal... "+RESET:
                            print(char, end='', flush=True),time.sleep(0.02)
                        print ("",end='', flush=True),time.sleep(2)
                        os.system('cls' if os.name == 'nt' else 'clear')
            
                            
                elif R=="3":
                    print()
                    print()
                    for char in Fore.LIGHTYELLOW_EX+"Volviendo al menú principal... "+RESET:
                        print(char, end='', flush=True),time.sleep(0.02)
                    print ("",end='', flush=True),time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')
                



                



            else:

                os.system('cls' if os.name == 'nt' else 'clear')
                print(Style.BRIGHT + Fore.RED + Back.BLACK + "====================================================================================================================================================================="+RESET )
                print(Style.BRIGHT + Fore.WHITE + "                                                                      BORRAR PROGRESO"+RESET)
                print(Style.BRIGHT + Fore.RED + Back.BLACK + "====================================================================================================================================================================="+RESET )
                print()
                print()
                print()
                print(Fore.BLUE+"-----------     NO TIENES NIGUN PROGRESO GUARDADO    -----------"+RESET)
                print()
                print()
                print()
                print()
                print()
                print()
                for char in "Presiona cualquier tecla para volver... ":
                    print(char, end='', flush=True),time.sleep(0.001)
                msvcrt.getch()
            


   



   

    if R=="7":
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        for char in "Saliendo del programa... ":
                print(char, end='', flush=True),time.sleep(0.002)
        print("",end='', flush=True),time.sleep(2)
        
        sys.exit() 
        
       




            
                





        

            






