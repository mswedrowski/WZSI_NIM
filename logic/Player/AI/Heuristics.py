import random
from operator import itemgetter


class Heuristics:

    @staticmethod
    def get_first_allowed_then_all_moves(board):
        moves = []  # Array of (row number,items taken)
        for row_num in range(len(board.rows)):
            for matches in range(1, board.rows[row_num].number_of_matches):
                moves.append((row_num, matches))
        if len(moves) == 0:
            for row_num in range(len(board.rows)):
                for matches in range(1, board.rows[row_num].number_of_matches + 1):
                    moves.append((row_num, matches))
        return moves

    @staticmethod
    def avoid_one_match_in_a_row(board):
        return random.choice(Heuristics.get_first_allowed_then_all_moves(board))

    @staticmethod
    def take_the_most_matches(board):
        moves = sorted(Heuristics.get_first_allowed_then_all_moves(board),key=itemgetter(1),reverse=True)
        return moves[0]
