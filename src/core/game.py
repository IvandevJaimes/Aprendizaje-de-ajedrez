from typing import Optional
import time
from src.core.state import StateManager
from src.core.input_handler import InputHandler
from src.utils.display import Display
from src.utils.constants import REQUIRED_SCORE_TO_UNLOCK, Colors, TOTAL_LEVELS
from src.challenges.challenge import run_level_challenge
from src.theory.level import THEORY_MODULES

class GameManager:
    def __init__(self):
        self.session = StateManager.get_user_session()
        self.username = self.session.get("user")
        self.difficulty = self.session.get("difficulty")
        self.current_level = int(self.session.get("level_reached", "0"))

    def setup_game(self) -> bool:
        Display.clear_screen()
        
        print("\nPara disfrutar de una mejor experiencia, maximiza la pantalla.\n")
        Display.press_to_continue()
        
        if not self.username:
            self.username = InputHandler.get_input("Ingresa tu nombre: ")
            password = InputHandler.get_input("Ingresa una contraseña (para recuperar tu partida): ")
            StateManager.save_state("user", self.username)
            StateManager.save_state("password", password)
        
        return True

    def show_main_menu(self):
        while True:
            Display.show_main_menu()
            
            choice = InputHandler.get_input(f"{Colors.GREEN}Elige una opción:{Colors.RESET} ").strip()
            
            if choice == "1":
                self.challenge_mode()
            elif choice == "2":
                self.riddle_mode()
            elif choice == "3":
                self.free_play()
            elif choice == "4":
                self.load_or_delete_game()
            elif choice == "5":
                self.show_instructions()
            elif choice == "6":
                self.show_credits()
            elif choice == "7":
                Display.clear_screen()
                print(f"{Colors.LIGHT_GREEN}¡Gracias por jugar! Hasta pronto.{Colors.RESET}\n")
                break
            else:
                InputHandler.clear_line()
                print(f"{Colors.YELLOW}Opción inválida. Intenta nuevamente.{Colors.RESET}")
                time.sleep(2)
                InputHandler.clear_line()

    def challenge_mode(self):
        Display.clear_screen()
        
        if StateManager.is_game_in_progress():
            print(f"{Colors.LIGHT_GREEN}Bienvenido de nuevo, {self.username}!{Colors.RESET}\n")
            print("Parece que ya tienes una partida en progreso.\n")
            print("Cargar tu partida desde el menú principal para continuar.\n")
            Display.press_to_continue()
            return
        
        self._select_difficulty()
        StateManager.save_state("difficulty", self.difficulty)
        
        Display.clear_screen()
        self._run_challenge_mode()

    def riddle_mode(self):
        Display.clear_screen()
        print(f"{Colors.LIGHT_GREEN}Modo Adivinanzas - En desarrollo{Colors.RESET}")
        Display.press_to_continue()

    def free_play(self):
        while True:
            Display.show_level_menu()
            
            choice = InputHandler.get_input(f"{Colors.GREEN}Selecciona nivel (1-5) o (11) para salir:{Colors.RESET} ").strip()
            
            if choice == "11":
                break
            
            if choice in ["1", "2", "3", "4", "5"]:
                self._select_difficulty()
                level = int(choice)
                THEORY_MODULES[level]()
                score = run_level_challenge(level, self.difficulty)

    def load_or_delete_game(self):
        Display.clear_screen()
        print(f"{Colors.LIGHT_CYAN}Cargar o Borrar Partida{Colors.RESET}\n")
        
        if not StateManager.is_game_in_progress():
            print(f"{Colors.YELLOW}No hay partida en progreso.{Colors.RESET}\n")
            Display.press_to_continue()
            return
        
        choice = InputHandler.get_input("¿Deseas borrar tu partida? (Si/No): ").upper()
        
        if choice in ["S", "SI"]:
            password = InputHandler.get_input("Ingresa tu contraseña: ")
            saved_password = StateManager.load_state("password")
            
            if password == saved_password:
                StateManager.clear_all_game_state()
                print(f"{Colors.GREEN}Partida borrada.{Colors.RESET}\n")
            else:
                print(f"{Colors.RED}Contraseña incorrecta.{Colors.RESET}\n")
        
        Display.press_to_continue()

    def show_instructions(self):
        Display.clear_screen()
        instructions = f"""
{Colors.LIGHT_YELLOW}INSTRUCCIONES DEL JUEGO{Colors.RESET}

{Colors.LIGHT_CYAN}MODO DESAFÍO:{Colors.RESET}
Responde preguntas de ajedrez para desbloquear niveles progresivos.
Necesitas {REQUIRED_SCORE_TO_UNLOCK}+ puntos para pasar al siguiente nivel.

{Colors.LIGHT_CYAN}MODO LIBRE:{Colors.RESET}
Accede a cualquier nivel y su contenido teórico sin restricciones.

{Colors.LIGHT_CYAN}DIFICULTADES:{Colors.RESET}
• Fácil: Sin límite de tiempo
• Normal: 10 segundos por pregunta
• Difícil: 5 segundos (-1 punto por error)

{Colors.LIGHT_CYAN}NAVEGACIÓN:{Colors.RESET}
Usa los números para seleccionar opciones.
Presiona cualquier tecla para continuar entre pantallas.
        """
        print(instructions)
        Display.press_to_continue()

    def show_credits(self):
        Display.clear_screen()
        credits = f"""
{Colors.LIGHT_YELLOW}CRÉDITOS{Colors.RESET}

Proyecto: Aprendizaje de Ajedrez
Versión: 2.0

{Colors.LIGHT_CYAN}Desarrollo:{Colors.RESET} Refactorizado para escalabilidad multiplataforma

{Colors.LIGHT_CYAN}Contenido:{Colors.RESET} Basado en conceptos de ajedrez reconocidos

{Colors.LIGHT_CYAN}Licencia:{Colors.RESET} Código abierto

{Colors.LIGHT_GREEN}Gracias por usar nuestro sistema educativo.{Colors.RESET}
        """
        print(credits)
        Display.press_to_continue()

    def _select_difficulty(self):
        Display.show_difficulty_menu()
        
        choice = InputHandler.get_input(f"{Colors.GREEN}Selecciona dificultad (1-3):{Colors.RESET} ").strip()
        
        while choice not in ["1", "2", "3"]:
            InputHandler.clear_line()
            print(f"{Colors.YELLOW}Opción inválida.{Colors.RESET}")
            time.sleep(2)
            InputHandler.clear_line()
            choice = InputHandler.get_input(f"{Colors.GREEN}Selecciona dificultad (1-3):{Colors.RESET} ").strip()
        
        self.difficulty = choice

    def _run_challenge_mode(self):
        for level in range(1, TOTAL_LEVELS + 1):
            current_score = StateManager.get_score(level)
            
            if current_score >= REQUIRED_SCORE_TO_UNLOCK:
                continue
            
            THEORY_MODULES[level]()
            score = run_level_challenge(level, self.difficulty)
            
            if score >= REQUIRED_SCORE_TO_UNLOCK:
                StateManager.save_state("level_reached", str(level))
            else:
                break
        
        Display.show_game_over(sum([StateManager.get_score(l) for l in range(1, TOTAL_LEVELS + 1)]))
