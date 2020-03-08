from logic.Board.Board import Board
from logic.Player.Human import Human


class Game:
    if __name__ == '__main__':
        board = Board(int(input('Enter how many rows you want to create')))
        board.display_board()

        player_1 = Human()
        player_2 = Human()

        current_player = player_1

        while not board.is_end():
            print('')
            board.display_board()
            row_to_modify, num_matches = current_player.make_move()

            if board.make_move(row_to_modify, num_matches):
                # swap
                if current_player == player_1:
                    current_player = player_2
                else:
                    current_player = player_1

        print("End of game " + str(current_player.name) + " won.")
