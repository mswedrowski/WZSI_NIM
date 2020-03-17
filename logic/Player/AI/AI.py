import random


class AI:

    def __init__(self, heuristics=None):
        self.name = input("Enter the name of the AI ")
        self.heuristics = heuristics

    def make_move(self, board):
        if self.heuristics is None:
            return random.choice(self.get_allowed_moves(board))
        else:
            return self.heuristics(board)

    @staticmethod
    def get_allowed_moves(self, board):
        possible_moves = []  # Array of (row number,items taken)
        for row_num in range(len(board.rows)):
            for matches in range(1, board.rows[row_num].number_of_matches + 1):
                possible_moves.append((row_num, matches))
        return possible_moves
