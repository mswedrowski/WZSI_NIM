from .Row import Row


class Board:
    def __init__(self, num_of_rows):
        self.rows = [Row(num_of_matches) for num_of_matches in range(1, num_of_rows+1)]

    def display_board(self):
        for index, row in enumerate(self.rows):
            print("RowNum:" + str(index) + " " + row.get_row_as_string())

    def make_move(self, row_num, num_of_matches):
        if (len(self.rows) - 1) - row_num >= 0:
            return self.rows[row_num].remove_matches(num_of_matches)
        else:
            return False

    def is_end(self):
        return any((map(lambda row: row.number_of_matches == 0, self.rows)))
