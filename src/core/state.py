import json
import os
from typing import Any, Dict
from src.utils.constants import STATE_FILES, STATE_DIR

class StateManager:
    @staticmethod
    def ensure_state_dir() -> None:
        os.makedirs(STATE_DIR, exist_ok=True)

    @staticmethod
    def save_state(key: str, value: Any) -> None:
        StateManager.ensure_state_dir()
        if key not in STATE_FILES:
            raise ValueError(f"Unknown state key: {key}")
        
        file_path = STATE_FILES[key]
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(value, f, ensure_ascii=False, indent=2)

    @staticmethod
    def load_state(key: str, default: Any = None) -> Any:
        StateManager.ensure_state_dir()
        if key not in STATE_FILES:
            raise ValueError(f"Unknown state key: {key}")
        
        file_path = STATE_FILES[key]
        if not os.path.exists(file_path):
            return default
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return default

    @staticmethod
    def delete_state(key: str) -> None:
        if key not in STATE_FILES:
            raise ValueError(f"Unknown state key: {key}")
        
        file_path = STATE_FILES[key]
        if os.path.exists(file_path):
            os.remove(file_path)

    @staticmethod
    def clear_all_game_state() -> None:
        keys_to_clear = [
            "level_reached",
            "scores",
            "theory_seen"
        ]
        for key in keys_to_clear:
            StateManager.delete_state(key)

    @staticmethod
    def get_user_session() -> Dict[str, Any]:
        return {
            "user": StateManager.load_state("user"),
            "difficulty": StateManager.load_state("difficulty", "1"),
            "level_reached": StateManager.load_state("level_reached", "0"),
            "scores": StateManager.load_state("scores", {}),
        }

    @staticmethod
    def is_game_in_progress() -> bool:
        level = StateManager.load_state("level_reached", "0")
        return level not in ["0", "5"]

    @staticmethod
    def update_score(level: int, score: int) -> None:
        scores = StateManager.load_state("scores", {})
        scores[str(level)] = score
        StateManager.save_state("scores", scores)

    @staticmethod
    def get_score(level: int) -> int:
        scores = StateManager.load_state("scores", {})
        return scores.get(str(level), 0)

    @staticmethod
    def mark_theory_as_seen(level: int) -> None:
        seen = StateManager.load_state("theory_seen", {})
        seen[str(level)] = True
        StateManager.save_state("theory_seen", seen)

    @staticmethod
    def is_theory_seen(level: int) -> bool:
        seen = StateManager.load_state("theory_seen", {})
        return seen.get(str(level), False)
