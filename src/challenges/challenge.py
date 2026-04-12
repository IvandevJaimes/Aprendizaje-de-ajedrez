from src.utils.data import CHALLENGES
from src.core.quiz_manager import QuizManager
from src.utils.display import Display
from src.core.state import StateManager

class LevelChallenge:
    def __init__(self, level: int, difficulty: str):
        self.level = level
        self.difficulty = difficulty
        self.quiz_manager = QuizManager(difficulty)
        self.questions = CHALLENGES.get(level, [])
        self.score = 0
        self.incorrect_count = 0

    def run(self) -> int:
        Display.clear_screen()
        
        for idx, question_data in enumerate(self.questions, 1):
            is_correct, _ = self.quiz_manager.ask_question(
                question_data["question"],
                question_data["options"],
                question_data["correct"],
                question_data["explanation"]
            )
            
            if is_correct:
                self.score += 1
            else:
                self.incorrect_count += 1
                if self.difficulty == "3":
                    self.score = max(0, self.score - 1)
        
        self._show_results()
        StateManager.update_score(self.level, self.score)
        return self.score

    def _show_results(self):
        difficulty_name = {
            "1": "Fácil",
            "2": "Normal",
            "3": "Difícil"
        }.get(self.difficulty, "Desconocida")
        
        Display.show_level_complete(
            self.level,
            self.score,
            self.incorrect_count,
            difficulty_name
        )
        Display.press_to_continue()

def run_level_challenge(level: int, difficulty: str) -> int:
    challenge = LevelChallenge(level, difficulty)
    return challenge.run()
