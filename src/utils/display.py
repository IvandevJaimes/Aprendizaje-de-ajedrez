import time
from src.utils.constants import Colors, SEPARATOR, BORDER_LIGHT, LEVEL_COLORS, LEVEL_DESCRIPTIONS
from src.core.input_handler import InputHandler

class Display:
    @staticmethod
    def print_slow(text: str, delay: float = 0.02) -> None:
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    @staticmethod
    def print_title(title: str, color: str = Colors.LIGHT_YELLOW) -> None:
        print(color + title + Colors.RESET)

    @staticmethod
    def print_separator(color: str = Colors.LIGHT_CYAN) -> None:
        print(color + SEPARATOR + Colors.RESET)

    @staticmethod
    def print_border() -> None:
        print(BORDER_LIGHT)

    @staticmethod
    def print_question_header(question_number: int, points: int = 1) -> None:
        Display.print_separator(Colors.LIGHT_MAGENTA)
        print()
        print(f"Pregunta {question_number}: {points} punto")
        print()
        Display.print_separator(Colors.LIGHT_MAGENTA)
        print()

    @staticmethod
    def print_options(options: dict) -> None:
        print(Colors.LIGHT_GREEN + ".......... OPCIONES .........." + Colors.RESET)
        print()
        for key, value in options.items():
            print(f"{Colors.LIGHT_BLUE}______ {key}: {Colors.RESET}{value}")
            print()

    @staticmethod
    def print_correct_answer(explanation: str) -> None:
        print(Colors.GREEN + "─────────────── ¡Correcto! ───────────────" + Colors.RESET)
        print()
        Display.print_slow(explanation, delay=0.02)
        print("\n" * 5)

    @staticmethod
    def print_incorrect_answer(correct_option: str, explanation: str, penalty: str = "") -> None:
        penalty_text = f" {penalty}" if penalty else ""
        print(Colors.RED + f">>>>>>> Incorrecto, la opción correcta es {correct_option}{penalty_text} <<<<<<<" + Colors.RESET)
        print()
        Display.print_slow(explanation, delay=0.02)
        print("\n" * 5)

    @staticmethod
    def clear_screen() -> None:
        InputHandler.clear_screen()

    @staticmethod
    def press_to_continue() -> None:
        for char in "Presiona cualquier tecla para continuar... ":
            print(char, end='', flush=True)
            time.sleep(0.001)
        InputHandler.wait_for_key()
        Display.clear_screen()

    @staticmethod
    def show_main_menu() -> None:
        Display.clear_screen()
        print()
        print(Colors.LIGHT_WHITE + "▄▀" * 96 + Colors.RESET)
        print()
        print(Colors.LIGHT_YELLOW + """
        ║                 APRENDIZAJE DE AJEDREZ - SISTEMA EDUCATIVO                      ║
        """.center(80) + Colors.RESET)
        print()
        print(Colors.LIGHT_WHITE + "▄▀" * 96 + Colors.RESET)
        print()
        
        menu = f"""
        {Colors.LIGHT_CYAN}1. Nuevo juego Modo Desafío{Colors.RESET}              {Colors.LIGHT_CYAN}5. Instrucciones{Colors.RESET}
        
        {Colors.LIGHT_CYAN}2. Modo Adivinanzas{Colors.RESET}                    {Colors.LIGHT_CYAN}6. Créditos{Colors.RESET}
        
        {Colors.LIGHT_CYAN}3. Modo Libre{Colors.RESET}                          {Colors.LIGHT_CYAN}7. Salir{Colors.RESET}
        
        {Colors.LIGHT_CYAN}4. Cargar o Borrar Partida{Colors.RESET}
        """
        print(menu)

    @staticmethod
    def show_difficulty_menu() -> None:
        Display.clear_screen()
        print()
        print(Colors.LIGHT_CYAN + "╔" + "═" * 78 + "╗" + Colors.RESET)
        print(Colors.LIGHT_CYAN + "║" + f"                    SELECCIONA NIVEL DE DIFICULTAD".center(78) + "║" + Colors.RESET)
        print(Colors.LIGHT_CYAN + "╚" + "═" * 78 + "╝" + Colors.RESET)
        print()
        
        difficulties = f"""
        {Colors.LIGHT_GREEN}1. Fácil{Colors.RESET}          Sin límite de tiempo
        
        {Colors.LIGHT_YELLOW}2. Normal{Colors.RESET}         10 segundos por pregunta
        
        {Colors.LIGHT_RED}3. Difícil{Colors.RESET}         5 segundos por pregunta (penalización: -1 punto en errores)
        """
        print(difficulties)

    @staticmethod
    def show_level_menu() -> None:
        Display.clear_screen()
        print()
        print(Colors.LIGHT_MAGENTA + "╔" + "═" * 78 + "╗" + Colors.RESET)
        print(Colors.LIGHT_MAGENTA + "║" + f"                         MODO LIBRE - SELECCIONA NIVEL".center(78) + "║" + Colors.RESET)
        print(Colors.LIGHT_MAGENTA + "╚" + "═" * 78 + "╝" + Colors.RESET)
        print()
        
        for level in range(1, 6):
            color = LEVEL_COLORS.get(level, Colors.LIGHT_CYAN)
            print(f"{color}Nivel {level}: {LEVEL_DESCRIPTIONS.get(level, '')}{Colors.RESET}")
            print()

    @staticmethod
    def show_theory(level: int, content: str) -> None:
        Display.clear_screen()
        print(Colors.LIGHT_CYAN + "♟" * 48 + Colors.RESET)
        print(content)
        print(Colors.LIGHT_CYAN + "♟" * 48 + Colors.RESET)
        Display.press_to_continue()

    @staticmethod
    def show_level_complete(level: int, score: int, incorrect: int, difficulty: str) -> None:
        Display.clear_screen()
        print(Colors.LIGHT_MAGENTA + "╔" + "═" * 78 + "╗" + Colors.RESET)
        print(Colors.LIGHT_MAGENTA + "║" + f"NIVEL {level} COMPLETADO".center(78) + "║" + Colors.RESET)
        print(Colors.LIGHT_MAGENTA + "╚" + "═" * 78 + "╝" + Colors.RESET)
        print()
        print()
        
        difficulty_display = difficulty
        if difficulty == "Difícil":
            difficulty_display = f"{Colors.RED}Difícil (Penalización: -1 punto en errores){Colors.RESET}"
        
        print(f"{Colors.LIGHT_BLUE}Dificultad elegida:{Colors.RESET} {difficulty_display}")
        print()
        print(f"{Colors.LIGHT_BLUE}Puntos obtenidos:{Colors.RESET} {Colors.GREEN}{score}{Colors.RESET}")
        print()
        print(f"{Colors.LIGHT_BLUE}Respuestas incorrectas:{Colors.RESET} {Colors.RED}{incorrect}{Colors.RESET}")
        print()

    @staticmethod
    def show_game_over(total_score: int) -> None:
        Display.clear_screen()
        print()
        print(Colors.LIGHT_MAGENTA + "╔" + "═" * 78 + "╗" + Colors.RESET)
        print(Colors.LIGHT_MAGENTA + "║" + f"¡JUEGO COMPLETADO!".center(78) + "║" + Colors.RESET)
        print(Colors.LIGHT_MAGENTA + "╚" + "═" * 78 + "╝" + Colors.RESET)
        print()
        print(f"{Colors.LIGHT_GREEN}Puntuación total: {total_score}{Colors.RESET}")
        print()
