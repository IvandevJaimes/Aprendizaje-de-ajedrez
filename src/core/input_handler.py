import sys
import os
import platform
from typing import Optional

class InputHandler:
    @staticmethod
    def clear_screen() -> None:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    @staticmethod
    def wait_for_key() -> None:
        if platform.system() == 'Windows':
            import msvcrt
            msvcrt.getch()
        else:
            os.system('stty -echo')
            try:
                sys.stdin.read(1)
            finally:
                os.system('stty echo')

    @staticmethod
    def clear_line() -> None:
        sys.stdout.write('\033[F\033[K')

    @staticmethod
    def get_input(prompt: str = "") -> str:
        return input(prompt)

    @staticmethod
    def get_numeric_input(prompt: str, valid_options: list) -> str:
        while True:
            user_input = InputHandler.get_input(prompt).strip()
            if user_input in [str(opt) for opt in valid_options]:
                return user_input
            InputHandler.clear_line()

    @staticmethod
    def is_windows() -> bool:
        return os.name == 'nt'

    @staticmethod
    def is_unix() -> bool:
        return os.name == 'posix'
