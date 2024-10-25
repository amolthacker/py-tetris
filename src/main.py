import sys
from typing import List

from tetris_engine.tetris import Tetris


def main():
    """Entry point to run the simulator"""
    tetris = Tetris()
    for input_str in sys.stdin:
        output = tetris.simulate(input_str.strip(), display_enabled=False)
        sys.stdout.write(f"{str(output)}\n")


if __name__ == "__main__":
    main()
