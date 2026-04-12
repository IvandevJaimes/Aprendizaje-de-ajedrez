#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.core.game import GameManager
from src.core.input_handler import InputHandler

def main():
    try:
        game = GameManager()
        game.setup_game()
        game.show_main_menu()
    except KeyboardInterrupt:
        InputHandler.clear_screen()
        print("\nJuego interrumpido por el usuario.\n")
        sys.exit(0)
    except Exception as e:
        InputHandler.clear_screen()
        print(f"Error: {e}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()
