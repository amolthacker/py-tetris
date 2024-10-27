import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.getcwd(), "src"))

from tetris.grid import Grid
from tetris.piece import Piece, Shape
from tetris.simulator import Simulator


class TestTetris(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.tetris = Simulator()

    def test_input_sequence_1(self) -> None:
        input_seq = "Q0"
        expected_output = 2
        actual_output = self.tetris.simulate(input_seq)
        self.assertEqual(expected_output, actual_output)

    def test_input_sequence_2(self) -> None:
        input_seq = "I0,I4,Q8"
        expected_output = 1
        actual_output = self.tetris.simulate(input_seq)
        self.assertEqual(expected_output, actual_output)

    def test_input_sequence_3(self) -> None:
        input_seq = "T1,Z3,I4"
        expected_output = 4
        actual_output = self.tetris.simulate(input_seq)
        self.assertEqual(expected_output, actual_output)

    def test_input_sequence_4(self) -> None:
        input_seq = "Q0,I2,I6,I0,I6,I6,Q2,Q4"
        expected_output = 3
        actual_output = self.tetris.simulate(input_seq)
        self.assertEqual(expected_output, actual_output)

    def test_grid_init(self):
        cell_char = "X"
        num_rows = 100
        num_cols = 16
        tetris_grid = Grid(rows=num_rows, cols=num_cols, char=cell_char)
        all(
            all(self.assertEqual(cell_char, cell[0]) for cell in row)
            for row in tetris_grid.grid
        )
        self.assertEqual(num_rows, tetris_grid.height)
        self.assertEqual(num_cols, tetris_grid.width)

    def test_place_piece(self):
        piece = Piece(shape_letter=Shape.Q.name)
        y, x = 6, 4
        tetris_grid = Grid()
        tetris_grid.place_piece(piece=piece, piece_y=y, piece_x=x)
        grid = tetris_grid.grid
        self.assertEqual(Piece.CHAR, grid[6][4])
        self.assertEqual(Piece.CHAR, grid[6][5])
        self.assertEqual(Piece.CHAR, grid[7][4])
        self.assertEqual(Piece.CHAR, grid[7][5])

        piece = Piece(shape_letter=Shape.T.name)
        y, x = 8, 7
        tetris_grid = Grid()
        tetris_grid.place_piece(piece=piece, piece_y=y, piece_x=x)
        grid = tetris_grid.grid
        self.assertEqual(Piece.CHAR, grid[8][7])
        self.assertEqual(Piece.CHAR, grid[8][8])
        self.assertEqual(Piece.CHAR, grid[8][9])
        self.assertEqual(Piece.CHAR, grid[9][8])

    def test_piece_colliding(self):
        piece_in_place = Piece(shape_letter=Shape.T.name)
        y, x = 8, 7
        tetris_grid = Grid()
        tetris_grid.place_piece(piece=piece_in_place, piece_y=y, piece_x=x)

        new_piece = Piece(shape_letter=Shape.T.name)
        new_piece_y, new_piece_x = 8, 7
        self.assertTrue(
            tetris_grid.piece_colliding(
                piece=new_piece, piece_y=new_piece_y, piece_x=new_piece_x
            )
        )

        new_piece_y, new_piece_x = 8, 4
        self.assertFalse(
            tetris_grid.piece_colliding(
                piece=new_piece, piece_y=new_piece_y, piece_x=new_piece_x
            )
        )

        piece_in_place = Piece(shape_letter=Shape.L.name)
        y, x = 7, 0
        tetris_grid = Grid()
        tetris_grid.place_piece(piece=piece_in_place, piece_y=y, piece_x=x)

        new_piece = Piece(shape_letter=Shape.Q.name)
        new_piece_y, new_piece_x = 7, 1
        self.assertFalse(
            tetris_grid.piece_colliding(
                piece=new_piece, piece_y=new_piece_y, piece_x=new_piece_x
            )
        )

    def test_drop_piece(self):
        tetris_grid = Grid()
        piece = Piece(shape_letter=Shape.Z.name)
        piece_y, piece_x = 0, 2
        expected_y_post_drop = 8
        actual_y_post_drop = tetris_grid.drop_piece(
            piece, piece_y, piece_x, tetris_grid.height - len(piece.get())
        )
        self.assertEqual(expected_y_post_drop, actual_y_post_drop)
        tetris_grid.place_piece(piece, actual_y_post_drop, piece_x)
        grid = tetris_grid.grid
        self.assertEqual(Piece.CHAR, grid[8][2])
        self.assertEqual(Piece.CHAR, grid[8][3])
        self.assertEqual(Piece.CHAR, grid[9][3])
        self.assertEqual(Piece.CHAR, grid[9][4])

    def test_is_grid_full(self):
        tetris_grid = Grid()
        piece = Piece(shape_letter=Shape.Q.name)
        for y in range(8, 0, -2):
            tetris_grid.place_piece(piece, y, 0)
        tetris_grid._print_grid()
        self.assertTrue(tetris_grid.is_full(piece, 2, 0))
        self.assertFalse(tetris_grid.is_full(piece, 2, 2))


if __name__ == "__main__":
    unittest.main()
