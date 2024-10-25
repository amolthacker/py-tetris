import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.getcwd(), "src"))

from tetris_engine.tetris import Tetris


class TestTetris(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.tetris = Tetris()

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


if __name__ == "__main__":
    unittest.main()
