import random

GRID_SIZE = 4

class Board:
    def __init__(self):
        self.grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.score = 0
        self.spawn_tile()
        self.spawn_tile()

    def spawn_tile(self):
        empty_cells = [(r, c) for r in range(GRID_SIZE) for c in range(GRID_SIZE) if self.grid[r][c] == 0]
        if not empty_cells:
            return
        r, c = random.choice(empty_cells)
        self.grid[r][c] = 4 if random.random() < 0.1 else 2

    def can_move(self):
        # If any cell is empty
        if any(0 in row for row in self.grid):
            return True
        # If any adjacent cells can merge
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE-1):
                if self.grid[r][c] == self.grid[r][c+1]:
                    return True
        for c in range(GRID_SIZE):
            for r in range(GRID_SIZE-1):
                if self.grid[r][c] == self.grid[r+1][c]:
                    return True
        return False

    def slide_row_left(self, row):
        # Remove zeros
        new_row = [num for num in row if num != 0]
        # Merge
        i = 0
        while i < len(new_row)-1:
            if new_row[i] == new_row[i+1]:
                new_row[i] *= 2
                self.score += new_row[i]
                new_row.pop(i+1)
                new_row.append(0)
                i += 1
            else:
                i += 1
        # Pad with zeros
        new_row += [0] * (GRID_SIZE - len(new_row))
        return new_row

    def move_left(self):
        new_grid = [self.slide_row_left(row) for row in self.grid]
        changed = new_grid != self.grid
        self.grid = new_grid
        return changed

    def move_right(self):
        reversed_grid = [row[::-1] for row in self.grid]
        new_grid = [self.slide_row_left(row)[::-1] for row in reversed_grid]
        changed = new_grid != self.grid
        self.grid = new_grid
        return changed

    def transpose(self):
        self.grid = [list(row) for row in zip(*self.grid)]

    def move_up(self):
        self.transpose()
        changed = self.move_left()
        self.transpose()
        return changed

    def move_down(self):
        self.transpose()
        changed = self.move_right()
        self.transpose()
        return changed

    def is_win(self):
        return any(any(cell == 2048 for cell in row) for row in self.grid)

    def print_board(self):
        print("\n" + "-" * 25)
        for row in self.grid:
            print("".join(f"{num:^6}" if num != 0 else "   .  " for num in row))
        print("-" * 25)
        print(f"Score: {self.score}\n")
