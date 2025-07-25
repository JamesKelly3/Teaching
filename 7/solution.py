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

    def play_move(self, x, y):
        self.board[x][y] = "O" if self.whose_turn == Player.ONE else "X"
        self.whose_turn = Player.TWO if self.whose_turn == Player.ONE else Player.TWO


    def winner(self) -> Optional[Player]:
        # None if the game is not finished, Player.ONE if player 1 wins, Player.TWO if player 2 wins

        # This solution is kind of yucky, you can probably make it better!
        diagonal_contain = []
        inverse_diagonal_contain = []
        any_empty = False
        for i in range(len(self.board)):
            if self.board[i][i] != " ":
                diagonal_contain.append(self.board[i][i])
            if self.board[2-i][2-i] != " ":
                inverse_diagonal_contain.append(self.board[2-i][2-i])
            row_contains = []
            column_contains = []
            for j in range(len(self.board[i])):
                if self.board[i][j] == " ":
                    any_empty = True
                if self.board[i][j] != " ":
                    row_contains.append(self.board[i][j])
                if self.board[j][i] != " ":
                    column_contains.append(self.board[j][i])
            if len(row_contains) == 3 and len(set(row_contains)) == 1:
                return Player.ONE if row_contains[0] == "O" else Player.TWO
            if len(column_contains) == 3 and len(set(column_contains)) == 1:
                return Player.ONE if column_contains[0] == "O" else Player.TWO
        if len(diagonal_contain) == 3 and len(set(diagonal_contain)) == 1:
            return Player.ONE if diagonal_contain[0] == "O" else Player.TWO
        if len(inverse_diagonal_contain) == 3 and len(set(inverse_diagonal_contain)) == 1:
            return Player.ONE if inverse_diagonal_contain[0] == "O" else Player.TWO
        return None if any_empty else Player.DRAW

    def draw_board(self):
        for i in range(len(self.board)):
            print(" | ".join(self.board[i]))
