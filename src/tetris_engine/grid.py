from typing import List

from tetris_engine.piece import Piece


class Grid:

    CHAR = "."
    HEIGHT = 10
    WIDTH = 10

    def __init__(self, rows: int = HEIGHT, cols: int = WIDTH, char: str = CHAR):
        self.height = rows
        self.width = cols
        self.char = char
        self.grid: List[List[int]] = [[char for _ in range(cols)] for _ in range(rows)]
        self.score = 0  # Tetris game score
        self.rem_rows = 0  # No.of partially filled rows remaining (output)

    def place_piece(self, piece: Piece, piece_y: int = 0, piece_x: int = 0):
        """Place the piece on the grid"""
        for row_idx, row in enumerate(piece.get()):
            for col_idx, col in enumerate(row):
                if col == 1:
                    self.grid[piece_y + row_idx][piece_x + col_idx] = Piece.CHAR

    def drop_piece(self, piece: Piece, piece_y: int, piece_x: int, max_y: int) -> int:
        """Drop the piece on the grid"""
        y = piece_y
        while y <= max_y and not self.piece_colliding(piece, y, piece_x):
            y += 1
        y_post_drop = y - 1
        self.rem_rows = max(self.rem_rows, self.height - y_post_drop)
        return y_post_drop

    def piece_colliding(self, col: Piece, piece_y: int, piece_x: int) -> bool:
        """Check if there is any collision with other pieces"""
        for row_idx, row in enumerate(col.get()):
            for col_idx, col in enumerate(row):
                if col == 1:
                    grid_y, grid_x = piece_y + row_idx, piece_x + col_idx
                    if (
                        grid_y >= self.height
                        or grid_x < 0
                        or grid_x >= self.width
                        or self.grid[grid_y][grid_x][0] == Piece.CHAR
                    ):
                        return True

    def is_full(self, piece: Piece, piece_y: int, piece_x: int) -> bool:
        """Check if the grid is full"""
        return any(
            row[0] == Piece.CHAR for row in self.grid[0]
        ) or self.piece_colliding(piece, piece_y, piece_x)

    def clear_rows(self) -> bool:
        """Clear the rows that are full and update the score"""
        # Update grid keeping just non-filled rows
        self.grid = [
            row for row in self.grid if not all(item[0] == Piece.CHAR for item in row)
        ]
        # The score is the difference between the original grid height and the updated grid height
        num_cleared_rows = self.height - len(self.grid)
        # Add empty rows for the cleared rows in the beginning
        if num_cleared_rows > 0:
            empty_row = [Grid.CHAR for _ in range(self.width)]
            self.grid = [empty_row[:] for _ in range(num_cleared_rows)] + self.grid
            # Update score
            updated_score = self.score + num_cleared_rows
            self.rem_rows -= updated_score - self.score
            self.score = updated_score
            return True
        else:
            return False

    def output(self) -> int:
        """Return Output (no.of partially filled rows remaining)"""
        return self.rem_rows

    def _print_grid(self):
        """Prints the grid"""
        print("\n".join([" ".join([str(cell) for cell in row]) for row in self.grid]))

    def print(
        self,
        input_seq: str,
        display_enabled: bool = False,
    ):
        """Prints the current state of game"""
        if display_enabled:
            print(f"\n[{input_seq[1:]}]")
            print(f"Score: {self.score} | Output: {self.rem_rows}")
            self._print_grid()
