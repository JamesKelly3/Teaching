"""
Fill in details for the below class to allow playing tic-tac-toe (noughts and crosses)
Each cell in the board is either " " if no-one has played, "O" if player 1 played there and "X" if player 2 played there
"""
from enum import Enum
from typing import List, Optional


class Player(Enum):
    ONE = 0
    TWO = 1
    # special value for a tied game
    DRAW = 2

class TicTacToe:
    board: List[List[str]] = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    whose_turn = Player.ONE

    def play_move(self, x: int, y: int):
        pass


    def winner(self) -> Optional[Player]:
        # None if the game is tied, Player.ONE if player 1 wins, Player.TWO if player 2 wins
        # this is the hardest bit, remember players can win on a row, a column, or a diagonal
        # there are 8 possible ways to win, it's a valid solution to check them all manually, but it's better to
        # have something more generic if you can.
        pass

    def draw_board(self):
        pass
