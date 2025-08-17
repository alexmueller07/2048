import curses
from board import Board

KEY_ACTIONS = {
    curses.KEY_UP: "up",
    curses.KEY_DOWN: "down",
    curses.KEY_LEFT: "left",
    curses.KEY_RIGHT: "right",
}

class Game:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.board = Board()
        curses.curs_set(0)
        self.stdscr.nodelay(False)
        self.stdscr.keypad(True)

    def draw(self):
        self.stdscr.clear()
        self.stdscr.addstr("2048 Console Game\nUse arrow keys to move. Press 'q' to quit.\n\n")
        for row in self.board.grid:
            row_str = "".join(f"{num:^6}" if num != 0 else "   .  " for num in row)
            self.stdscr.addstr(row_str + "\n")
        self.stdscr.addstr(f"\nScore: {self.board.score}\n")
        self.stdscr.refresh()

    def play(self):
        while True:
            self.draw()
            if self.board.is_win():
                self.stdscr.addstr("\nYou made 2048! Press any key to exit.\n")
                self.stdscr.getch()
                break
            if not self.board.can_move():
                self.stdscr.addstr("\nGame Over! No more moves.\n")
                self.stdscr.getch()
                break

            key = self.stdscr.getch()
            if key == ord('q'):
                break
            if key not in KEY_ACTIONS:
                continue

            moved = False
            if KEY_ACTIONS[key] == "up":
                moved = self.board.move_up()
            elif KEY_ACTIONS[key] == "down":
                moved = self.board.move_down()
            elif KEY_ACTIONS[key] == "left":
                moved = self.board.move_left()
            elif KEY_ACTIONS[key] == "right":
                moved = self.board.move_right()

            if moved:
                self.board.spawn_tile()
