import threading
import time
from typing import Optional, Tuple
from src.utils.constants import Colors, DIFFICULTIES
from src.core.input_handler import InputHandler
from src.utils.display import Display

class QuizManager:
    def __init__(self, difficulty: str):
        self.difficulty = difficulty
        self.config = DIFFICULTIES.get(difficulty, DIFFICULTIES["1"])
        self.time_limit = self.config.get("time_limit")
        self.penalty = self.config.get("penalty", False)

    def ask_question(self, question_text: str, options: dict, correct_answer: str, explanation: str) -> Tuple[bool, str]:
        Display.print_question_header(question_text, 1)
        print(question_text)
        print()
        Display.print_options(options)
        Display.print_border()
        print()
        
        if self.time_limit:
            answer = self._get_timed_input(options, correct_answer, explanation)
        else:
            answer = self._get_input(options, correct_answer, explanation)
        
        is_correct = answer == correct_answer
        
        if is_correct:
            Display.print_correct_answer(explanation)
        else:
            penalty_str = " -1 PUNTO" if self.penalty else ""
            Display.print_incorrect_answer(correct_answer, explanation, penalty_str)
        
        Display.press_to_continue()
        return is_correct, answer

    def _get_input(self, options: dict, correct_answer: str, explanation: str) -> str:
        valid_options = list(options.keys())
        while True:
            user_input = InputHandler.get_input(f"{Colors.GREEN}Ingrese su respuesta:{Colors.RESET} ").strip()
            if user_input in valid_options:
                return user_input
            InputHandler.clear_line()
            print(f"{Colors.YELLOW}Ingrese una respuesta válida.{Colors.RESET}")
            time.sleep(2)
            InputHandler.clear_line()

    def _get_timed_input(self, options: dict, correct_answer: str, explanation: str) -> Optional[str]:
        valid_options = list(options.keys())
        stop_event = threading.Event()
        user_answer = [None]
        
        def countdown():
            for i in range(self.time_limit, 0, -1):
                if stop_event.is_set():
                    break
                print(f"\r{Colors.GREEN}TIEMPO >>>>> {i} segundos <<<<<<{Colors.RESET} Ingrese su respuesta: ", end="", flush=True)
                time.sleep(1)
            
            if not stop_event.is_set():
                stop_event.set()
                print(f"\r{Colors.RED}<<<<<<<<<<<<<<<<<< ¡Tiempo agotado! >>>>>>>>>>>>>>>>>>{Colors.RESET}\n")
                time.sleep(2)
        
        def get_input_thread():
            while not stop_event.is_set():
                try:
                    answer = InputHandler.get_input()
                    if answer in valid_options:
                        stop_event.set()
                        user_answer[0] = answer
                        break
                except:
                    pass
        
        timer_thread = threading.Thread(target=countdown)
        input_thread = threading.Thread(target=get_input_thread)
        
        timer_thread.daemon = True
        input_thread.daemon = True
        
        timer_thread.start()
        input_thread.start()
        
        timer_thread.join(timeout=self.time_limit + 1)
        input_thread.join(timeout=self.time_limit + 1)
        
        return user_answer[0]
