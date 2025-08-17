import curses
from game import Game

def main(stdscr):
    game = Game(stdscr)
    game.play()

if __name__ == "__main__":
    curses.wrapper(main)
