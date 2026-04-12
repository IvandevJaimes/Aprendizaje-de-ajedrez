from src.utils.data import THEORY_CONTENT
from src.utils.display import Display

def show_level_1_theory():
    Display.show_theory(1, THEORY_CONTENT[1])

def show_level_2_theory():
    Display.show_theory(2, THEORY_CONTENT[2])

def show_level_3_theory():
    Display.show_theory(3, THEORY_CONTENT[3])

def show_level_4_theory():
    Display.show_theory(4, THEORY_CONTENT[4])

def show_level_5_theory():
    Display.show_theory(5, THEORY_CONTENT[5])

THEORY_MODULES = {
    1: show_level_1_theory,
    2: show_level_2_theory,
    3: show_level_3_theory,
    4: show_level_4_theory,
    5: show_level_5_theory,
}
