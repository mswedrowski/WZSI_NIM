from logic.Board.Board import Board
from logic.Player.AI.AI import AI
from logic.Player.AI.Heuristics import Heuristics
from logic.Player.Human import Human


class Game:
    if __name__ == '__main__':
        board = Board(int(input('Enter how many rows you want to create ')))
        board.display_board()

        player_1 = Human()
        player_2 = AI(heuristics=Heuristics.avoid_one_match_in_a_row)

        current_player = player_1

        while not board.is_end():
            print('')
            board.display_board()

            if isinstance(current_player, Human):
                row_to_modify, num_matches = current_player.make_move()
            else:
                row_to_modify, num_matches = current_player.make_move(board)

            print("Move by " + current_player.name + " Row: " + str(row_to_modify) + " Num matches" + str(num_matches))

            if board.make_move(row_to_modify, num_matches):
                # swap
                if current_player == player_1:
                    current_player = player_2
                else:
                    current_player = player_1
        print(' ')
        print("End of game " + str(current_player.name) + " won.")
