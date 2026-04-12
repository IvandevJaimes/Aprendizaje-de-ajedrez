import sys
import termios
import tty

def getch():
    """Get a single character from stdin without echo"""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def press_any_key(message="Presiona cualquier tecla para continuar... "):
    """Display message and wait for any key press"""
    print(message, end='', flush=True)
    getch()
    print()