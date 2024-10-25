from tetris_engine.grid import Grid
from tetris_engine.piece import Piece


class Tetris:

    def __init__(self, grid_height: int = Grid.HEIGHT):
        self.grid_height = grid_height

    def simulate(self, input_str: str, display_enabled: bool = False) -> int:
        # Initialize the grid
        grid = Grid(rows=self.grid_height)

        # Display initialized grid (if display is enabled)
        input_seq = str()
        grid.print(input_seq, display_enabled)

        # Process the input sequence
        for shape, col_offset in input_str.split(","):
            input_seq = ",".join([input_seq, "".join([shape, col_offset])])
            piece = Piece(shape)
            x = int(col_offset)
            y = 0

            # The max Y coordinate for the piece
            max_y = self.grid_height - len(piece.get())

            # Game Over if the grid is full
            if grid.is_full(piece, y, x):
                print("Game Over!")
                break

            # Simulate dropping the piece
            y = grid.drop_piece(piece, y, x, max_y)
            y += 1
            # Check for collision
            if y > max_y or grid.piece_colliding(piece, y, x):
                y -= 1
                # Place the piece on the grid and display
                grid.place_piece(piece, y, x)
                grid.print(input_seq, display_enabled)
                # Clear rows and display grid with rows cleared
                if grid.clear_rows():
                    grid.print(input_seq, display_enabled)

        # Output (no.of partially filled rows remaining) for the input sequence
        return grid.output()
