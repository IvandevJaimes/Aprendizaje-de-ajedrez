import os
from typing import Dict

class Colors:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    LIGHT_BLACK = "\033[90m"
    LIGHT_RED = "\033[91m"
    LIGHT_GREEN = "\033[92m"
    LIGHT_YELLOW = "\033[93m"
    LIGHT_BLUE = "\033[94m"
    LIGHT_MAGENTA = "\033[95m"
    LIGHT_CYAN = "\033[96m"
    LIGHT_WHITE = "\033[97m"
    
    BOLD = "\033[1m"
    RESET = "\033[0m"

CHESS_SYMBOLS = {
    "white_king": "♔",
    "white_queen": "♕",
    "white_rook": "♖",
    "white_bishop": "♗",
    "white_knight": "♘",
    "white_pawn": "♙",
    "black_king": "♚",
    "black_queen": "♛",
    "black_rook": "♜",
    "black_bishop": "♝",
    "black_knight": "♞",
    "black_pawn": "♟",
}

BORDER_LIGHT = f"{Colors.LIGHT_CYAN}♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘   ♖  ♙  ♖   ♘   ♗   ♕   ♔   ♗   ♘{Colors.RESET}"

SEPARATOR = "▄▀" * 96

DIFFICULTIES: Dict[str, dict] = {
    "1": {
        "name": "Fácil",
        "time_limit": None,
        "penalty": False,
        "description": "Sin límite de tiempo"
    },
    "2": {
        "name": "Normal",
        "time_limit": 10,
        "penalty": False,
        "description": "10 segundos por pregunta"
    },
    "3": {
        "name": "Difícil",
        "time_limit": 5,
        "penalty": True,
        "description": "5 segundos por pregunta (-1 punto por error)"
    }
}

REQUIRED_SCORE_TO_UNLOCK = 5
TOTAL_QUESTIONS_PER_LEVEL = 10
TOTAL_LEVELS = 5

STATE_DIR = os.path.expanduser("~/.chess_learning_game")
os.makedirs(STATE_DIR, exist_ok=True)

STATE_FILES = {
    "difficulty": os.path.join(STATE_DIR, "difficulty.json"),
    "user": os.path.join(STATE_DIR, "user.json"),
    "password": os.path.join(STATE_DIR, "password.json"),
    "level_reached": os.path.join(STATE_DIR, "level_reached.json"),
    "scores": os.path.join(STATE_DIR, "scores.json"),
    "theory_seen": os.path.join(STATE_DIR, "theory_seen.json"),
}

MENU_OPTIONS = {
    "1": "challenge_mode",
    "2": "riddle_mode",
    "3": "free_play",
    "4": "load_or_delete",
    "5": "instructions",
    "6": "credits",
    "7": "exit"
}

LEVEL_DESCRIPTIONS = {
    1: "Qué es el ajedrez, su objetivo, piezas y movimientos básicos",
    2: "Notación algebraica, aperturas, movimientos especiales y empates",
    3: "Tácticas, técnicas de juego y estrategias",
    4: "Maniobras, conceptos estratégicos, formas de juego",
    5: "Historia del ajedrez"
}

LEVEL_COLORS = {
    1: Colors.LIGHT_MAGENTA,
    2: Colors.LIGHT_GREEN,
    3: Colors.LIGHT_YELLOW,
    4: Colors.LIGHT_BLUE,
    5: Colors.LIGHT_RED,
}
