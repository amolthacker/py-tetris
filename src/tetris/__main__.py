import sys
from typing import List

from tetris.simulator import Simulator


def main() -> None:
    """Entry point to run the simulator"""
    tetris = Simulator()
    for input_str in sys.stdin:
        output = tetris.simulate(input_str.strip(), display_enabled=False)
        sys.stdout.write(f"{str(output)}\n")


if __name__ == "__main__":
    main()
