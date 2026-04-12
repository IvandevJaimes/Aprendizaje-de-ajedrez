ROJO="\033[31m"
VERDE="\033[32m"

RESET="\033[0m"




import time 
import os
from colorama import*
import sys
import json
from TEORIA1 import*
from NIVEL1 import*
from NIVELES import *

usuario=""
def inicio():
    
    def LIMPIAR():
        sys.stdout.write('\033[F\033[K')
    def TITULO():

        
        print(Fore.LIGHTCYAN_EX+"#####################################################################################################################################################################"+RESET)
        print()
        print(Fore.LIGHTWHITE_EX+"                                                                            MODO DESAFIO                                                            "+RESET)
        print()
        print(Fore.LIGHTCYAN_EX+"#####################################################################################################################################################################"+RESET)
        print()
    TITULO()
    


    try:
        with open('usuario.json', 'r') as file:
            cargarU=json.load(file)

        with open('contra.json', 'r') as file:
            contra=json.load(file)

        with open('nivel_jugado.json', 'r') as file:
                NJ=json.load(file)
        TT="t"

    except:
        TT="f"
        NJ="0"
        
        




    
        

    if TT=="t" and NJ <"5":
                
        print()
        print()
        print()
        print(Fore.LIGHTGREEN_EX+"    >>>>>>>>>>>>>> Bienvenido de nuevo "+ cargarU+ " <<<<<<<<<<<<<<"+RESET)
        print()
        print()
        print()
        for char in""" Al parecer ya iniciaste una partida en modo desafío. Para continuar con tu partida puedes volver y cargar tu partida guardada en el menú principal y continuar donde lo dejaste.""" :
            print(char, end='', flush=True),time.sleep(0.02)
        print()
        print()
        print()
        for char in "Presiona cualquier tecla para volver... ":
            print(char, end='', flush=True),time.sleep(0.001)
        msvcrt.getch()
        os.system('cls' if os.name == 'nt' else 'clear')


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      
    if NJ=="5":
        os.system('cls' if os.name == 'nt' else 'clear')
        TITULO()

        print()
        print()
        print()
        print(Fore.LIGHTGREEN_EX+"    >>>>>>>>>>>>>> Bienvenido de nuevo "+ cargarU+ " <<<<<<<<<<<<<<"+RESET)
        print()
        print()
        print()
        for char in"""Ya has completado el modo desafio, si deseas volver a jugarlo puedes inciar una nueva partida aquí, de lo contrario puedes probar otro modo de juego.""" :
            print(char, end='', flush=True),time.sleep(0.02)
        print()
        print()
        print()
        while (True):
                try:
                    RR=input("¿Desea inciar una nueva partida en modo desafío? (Si/No): ")
                    RR=RR.upper()
                    if RR not in ["SI","NO","S","N"]:
                        raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        
                    break
                except ValueError as E :
                    LIMPIAR()
                    print(E)
                    print ("",end='', flush=True),time.sleep(2)
                    LIMPIAR()
        if RR=="NO" or RR=="N":
                print()
                print()
                for char in Fore.LIGHTYELLOW_EX+ "Volviendo al menú principal..."""+RESET:
                    print(char, end='', flush=True),time.sleep(0.02)
                print ("",end='', flush=True),time.sleep(2)  
                os.system('cls' if os.name == 'nt' else 'clear')
        elif RR =="SI" or RR=="S":
            LIMPIAR()
            while True:
                C=input(Fore.LIGHTBLUE_EX+"Porfavor ingrese su contraseña para iniciar una nueva partida: "+RESET)
                if C == contra:
                    LIMPIAR()
                    print(Fore.GREEN+"Contraseña correcta"+RESET)
                    ELIMINAR=['nivel_jugado.json','flag.json','puntaje.json','puntaje1.json','puntaje2.json','puntaje3.json','puntaje4.json','puntaje5.json','PF.json']
                    for filename in ELIMINAR:
                         if os.path.exists(filename):
                             os.remove(filename)
                    break
                else:
                    LIMPIAR()
                    print(Fore.RED+"Contraseña incorrecta. Porfavor vuelva a intentarlo")
                    time.sleep(2)
                    LIMPIAR()
            print()
            for char in "Presiona cualquier tecla para continuar... ":
              print(char, end='', flush=True),time.sleep(0.001)
            msvcrt.getch()
            os.system('cls' if os.name == 'nt' else 'clear')
            print()
            TITULO()
            print()
            print()
            print(Fore.LIGHTMAGENTA_EX+"¡Bienvenido al juego de aprendizaje de ajedrez en modo desafio! "+cargarU+RESET)
            print()
            for char in"""En este juego deberás enfrentarte al desafio de preguntas triva. Antes de comenzar a responder las preguntas se te presentará el aprendizaje de cada nivel. 
A medida que vayas avanzando los niveles se irán poniendo mas dificiles. ¡Con cada respuesta correcta obtendras 1 punto!, pero para poder desbloquear el siguiente nivel tendras que
conseguir una puntuacíon de 5 o más. Tu progeso se guardará automaticamente al completar cada nivel.""" :
                print(char, end='', flush=True),time.sleep(0.02)

            print()
            print()
            print("A continuación se presentará la temática de cada nivel:")
            print()
            
            N01=Fore.LIGHTMAGENTA_EX+"   # NIVEL1: "+RESET+"Qué es el ajedrez, su ojetivo, piezas y movimientos básicos "
            N02=Fore.LIGHTGREEN_EX+"   # NIVEL2: "+RESET+"Notación algebraica, aperturas, movimientos especiales y empates "
            N03=Fore.LIGHTYELLOW_EX+"   # NIVEL3: "+RESET+"Tácticas, técnicas de juego y estrategias "
            N04=Fore.LIGHTBLUE_EX+"   # NIVEL4: "+RESET+"Maniobras, conceptos estratégicos, formas de juego"
            N05=Fore.LIGHTRED_EX+"   # NIVEL5: "+RESET+"Historia del ajedrez"

            for N1 in N01:
                print(N1, end='', flush=True),time.sleep(0.02)
            print()
            print()

            for N2 in N02:
                print(N2, end='', flush=True),time.sleep(0.02)
            print()
            print()

            for N3 in N03:
                print(N3, end='', flush=True),time.sleep(0.02)
            print()
            print()

            for N4 in N04:
                print(N4, end='', flush=True),time.sleep(0.02)
            print()
            print()

            for N5 in N05:
                print(N5, end='', flush=True),time.sleep(0.02)
            print()
            print()
            print()
            print()

            while (True):
                            try:
                                RR=input("¿Desea inciar una nueva partida en modo desafío? (Si/No): ")
                                RR=RR.upper()
                                if RR not in ["SI","NO","S","N"]:
                                    raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                                    
                                break
                            except ValueError as E :
                                LIMPIAR()
                                print(E)
                                print ("",end='', flush=True),time.sleep(2)
                                LIMPIAR()
                    


            if RR== "SI" or RR=="S":
                
                while(True):
                        TITULO()
                        

                        os.system('cls' if os.name == 'nt' else 'clear')
                        TITULO()
                        print()
                        print()
                        print()
                        print(Fore.LIGHTMAGENTA_EX+"________________________________  Elige la dificultad del juego  ________________________________ "+RESET)
                        print()
                        print()
                        print(Fore.LIGHTRED_EX+"-----> ATENCIÓN: "+RESET+"Una vez seleccionada la dificultad no podrás camiarla.")
                        print()
                        print(Fore.LIGHTBLUE_EX+"###############################################################################################################################"+RESET)
                        print()
                        print(Fore.LIGHTGREEN_EX+"--- 1. "+RESET+"Facil (Sin límite de tiempo para responder las preguntas)."+RESET)
                        print()
                        print(Fore.LIGHTGREEN_EX+"--- 2. "+RESET+"Normal (Tendrás un tiempo de 10 segundos para responder las preguntas)."+RESET)
                        print()
                        print(Fore.LIGHTGREEN_EX+"--- 3. "+RESET+"Difícil (Las preguntas tendrán puntuación negativa y tendrás 5 seg para responder y la teoria solo se mostrará una vez)."+RESET)
                        print()
                        print(Fore.YELLOW+"--- 4. SALIR"+RESET)
                        print()
                        print(Fore.LIGHTBLUE_EX+"###############################################################################################################################"+RESET)
                        print()
                        print()
                        
                        try:
                            R=input("Elige una opción: ")
                            
                            if R not in ["1","2","3","4"]:
                                raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                                            
                                
                        except:
                                
                                LIMPIAR()
                                print(Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                                print ("",end='', flush=True),time.sleep(2)
                                LIMPIAR()    

                        if R=="1":
                            LIMPIAR()
                            DIFICULTAD="1"
                            with open ('DIFICULTAD.json' , 'w') as file:
                                json.dump(DIFICULTAD, file)

                            for char in "De acuerdo. vamos a inciar con el nivel 1 en modo fácil":
                                print(char, end='', flush=True),time.sleep(0.02)
                            print ("",end='', flush=True),time.sleep(3)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            NIVELES()
                            break

                        elif R=="2":
                            LIMPIAR()
                            DIFICULTAD="2"
                            with open ('DIFICULTAD.json' , 'w') as file:
                                json.dump(DIFICULTAD, file)

                            for char in "De acuerdo. vamos a inciar con el nivel 1 en modo normal":
                                print(char, end='', flush=True),time.sleep(0.02)
                            print ("",end='', flush=True),time.sleep(3)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            
                            NIVELES()
                            break


                        elif R=="3":
                            LIMPIAR()
                            DIFICULTAD="3"
                            with open ('DIFICULTAD.json' , 'w') as file:
                                json.dump(DIFICULTAD, file)

                            for char in "De acuerdo. vamos a inciar con el nivel 1 en modo dificil":
                                print(char, end='', flush=True),time.sleep(0.02)
                            print ("",end='', flush=True),time.sleep(3)
                            os.system('cls' if os.name == 'nt' else 'clear')
                            
                            NIVELES()
                            break





                        elif R=="4":
                            print()
                            print()
                            for char in Fore.LIGHTYELLOW_EX+ "Volviendo..."""+RESET:
                                print(char, end='', flush=True),time.sleep(0.02)
                            print ("",end='', flush=True),time.sleep(2)  
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                
                            
                    
                
                            
                            
            elif RR=="NO" or RR=="N":
                    print()
                    print()
                    for char in Fore.LIGHTYELLOW_EX+ "Volviendo al menú principal..."""+RESET:
                        print(char, end='', flush=True),time.sleep(0.02)
                    print ("",end='', flush=True),time.sleep(2)  
                    os.system('cls' if os.name == 'nt' else 'clear')




    
            
            

                

            








#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    elif TT =="f" and NJ=="0":

 
        print()
        print()
        print()
        print(Fore.LIGHTGREEN_EX+"------------------------     Antes de comenzar debes registrarte     ------------------------------------------------------------------------------------------------"+RESET)
        print()

        usuario=input("   Cree su nombre de usuario: ")
        with open ('usuario.json' , 'w') as file:
            json.dump(usuario, file)
        
        
        LIMPIAR()
    
        while(True):
            
            try:
                contra=input("   Cree su contraseña (Mínimo 4 caractéres): ")
                if len (contra) >=4:
                    LIMPIAR()
                    
                    with open ('contra.json', 'w') as file:
                        json.dump(contra, file)
                    break

                else:
                    raise ValueError (f"{ROJO}la contraseña debe tener mínimo 4 caractéres. Porfavor vuelve a intentarlo{RESET} ")

            except ValueError as E:
                LIMPIAR()
                print(E)
                print ("",end='', flush=True),time.sleep(2)
                LIMPIAR()
        

     

        



        while(True):
            try:
                contras=input("   Confirme su contraseña para ingresar al juego: ")
                if contras == contra:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                    
            
                else:
                    
                    
                    LIMPIAR()
                    print(f"{ROJO}la contraseña no coincide. Porfavor vuelve a intentarlo{RESET} ")
                    print ("",end='', flush=True),time.sleep(2)
                    LIMPIAR()
                          
            except:
                
                LIMPIAR()
                print(f"{ROJO}la contraseña no coincide. Porfavor vuelve a intentarlo{RESET} ")
                print ("",end='', flush=True),time.sleep(2)
            
        print()
        TITULO()
        print()
        print()
        print(Fore.LIGHTMAGENTA_EX+"¡Bienvenido al juego de aprendizaje de ajedrez en modo desafio! "+usuario+RESET)
        print()
        for char in"""En este juego deberás enfrentarte al desafio de preguntas triva. Antes de comenzar a responder las preguntas se te presentará el aprendizaje de cada nivel. 
A medida que vayas avanzando los niveles se irán poniendo mas dificiles. ¡Con cada respuesta correcta obtendras 1 punto!, pero para poder desbloquear el siguiente nivel tendras que
conseguir una puntuacíon de 5 o más. Tu progeso se guardará automaticamente al completar cada nivel.""" :
            print(char, end='', flush=True),time.sleep(0.02)

        print()
        print()
        print("A continuación se presentará la temática de cada nivel:")
        print()
        
        N01=Fore.LIGHTMAGENTA_EX+"   # NIVEL1: "+RESET+"Qué es el ajedrez, su ojetivo, piezas y movimientos básicos "
        N02=Fore.LIGHTGREEN_EX+"   # NIVEL2: "+RESET+"Notación algebraica, aperturas, movimientos especiales y empates "
        N03=Fore.LIGHTYELLOW_EX+"   # NIVEL3: "+RESET+"Tácticas, técnicas de juego y estrategias "
        N04=Fore.LIGHTBLUE_EX+"   # NIVEL4: "+RESET+"Maniobras, conceptos estratégicos, formas de juego"
        N05=Fore.LIGHTRED_EX+"   # NIVEL5: "+RESET+"Historia del ajedrez"

        for N1 in N01:
            print(N1, end='', flush=True),time.sleep(0.02)
        print()
        print()

        for N2 in N02:
            print(N2, end='', flush=True),time.sleep(0.02)
        print()
        print()

        for N3 in N03:
            print(N3, end='', flush=True),time.sleep(0.02)
        print()
        print()

        for N4 in N04:
            print(N4, end='', flush=True),time.sleep(0.02)
        print()
        print()

        for N5 in N05:
            print(N5, end='', flush=True),time.sleep(0.02)
        print()
        print()
        print()
        print()
        
        print()
        print()
        while (True):
                try:
                    RR=input("¿Desea inciar una nueva partida en modo desafío? (Si/No): ")
                    RR=RR.upper()
                    if RR not in ["SI","NO","S","N"]:
                        raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                        
                    break
                except ValueError as E :
                    LIMPIAR()
                    print(E)
                    print ("",end='', flush=True),time.sleep(2)
                    LIMPIAR()
        


        if RR== "SI" or RR=="S":
            
            while(True):
                    TITULO()
                    

                    os.system('cls' if os.name == 'nt' else 'clear')
                    TITULO()
                    print()
                    print()
                    print()
                    print(Fore.LIGHTMAGENTA_EX+"________________________________  Elige la dificultad del juego  ________________________________ "+RESET)
                    print()
                    print()
                    print(Fore.LIGHTRED_EX+"-----> ATENCIÓN: "+RESET+"Una vez seleccionada la dificultad no podrás camiarla.")
                    print()
                    print(Fore.LIGHTBLUE_EX+"###############################################################################################################################"+RESET)
                    print()
                    print(Fore.LIGHTGREEN_EX+"--- 1. "+RESET+"Facil (Sin límite de tiempo para responder las preguntas)."+RESET)
                    print()
                    print(Fore.LIGHTGREEN_EX+"--- 2. "+RESET+"Normal (Tendrás un tiempo de 10 segundos para responder las preguntas)."+RESET)
                    print()
                    print(Fore.LIGHTGREEN_EX+"--- 3. "+RESET+"Difícil (Las preguntas tendrán puntuación negativa y tendrás 5 seg para responder y la teoria solo se mostrará una vez)."+RESET)
                    print()
                    print(Fore.YELLOW+"--- 4. SALIR"+RESET)
                    print()
                    print(Fore.LIGHTBLUE_EX+"###############################################################################################################################"+RESET)
                    print()
                    print()
                    
                    try:
                        R=input("Elige una opción: ")
                        
                        if R not in ["1","2","3","4"]:
                            raise ValueError (Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                                        
                            
                    except:
                            
                            LIMPIAR()
                            print(Fore.YELLOW+"Porfavor ingrese una respuesta válida. Vuelva a intentarlo"+RESET)
                            print ("",end='', flush=True),time.sleep(2)
                            LIMPIAR()    

                    if R=="1":
                        LIMPIAR()
                        DIFICULTAD="1"
                        with open ('DIFICULTAD.json' , 'w') as file:
                            json.dump(DIFICULTAD, file)

                        for char in "De acuerdo. vamos a inciar con el nivel 1 en modo fácil":
                            print(char, end='', flush=True),time.sleep(0.02)
                        print ("",end='', flush=True),time.sleep(3)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        NIVELES()
                        break

                    elif R=="2":
                        LIMPIAR()
                        DIFICULTAD="2"
                        with open ('DIFICULTAD.json' , 'w') as file:
                            json.dump(DIFICULTAD, file)

                        for char in "De acuerdo. vamos a inciar con el nivel 1 en modo normal":
                            print(char, end='', flush=True),time.sleep(0.02)
                        print ("",end='', flush=True),time.sleep(3)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        
                        NIVELES()
                        break


                    elif R=="3":
                        LIMPIAR()
                        DIFICULTAD="3"
                        with open ('DIFICULTAD.json' , 'w') as file:
                            json.dump(DIFICULTAD, file)

                        for char in "De acuerdo. vamos a inciar con el nivel 1 en modo dificil":
                            print(char, end='', flush=True),time.sleep(0.02)
                        print ("",end='', flush=True),time.sleep(3)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        
                        NIVELES()
                        break





                    elif R=="4":
                        print()
                        print()
                        for char in Fore.LIGHTYELLOW_EX+ "Volviendo..."""+RESET:
                            print(char, end='', flush=True),time.sleep(0.02)
                        print ("",end='', flush=True),time.sleep(2)  
                        os.system('cls' if os.name == 'nt' else 'clear')
                        break
            
                        
                
            
                        
                        
        elif RR=="NO" or RR=="N":
                print()
                print()
                for char in Fore.LIGHTYELLOW_EX+ "Volviendo al menú principal..."""+RESET:
                    print(char, end='', flush=True),time.sleep(0.02)
                print ("",end='', flush=True),time.sleep(2)  
                os.system('cls' if os.name == 'nt' else 'clear')


    




