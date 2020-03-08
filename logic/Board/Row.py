class Row:
    def __init__(self, init_number_of_matches):
        self.number_of_matches = init_number_of_matches

    def remove_matches(self, number_to_remove):
        if self.number_of_matches - number_to_remove >= 0:
            self.number_of_matches = self.number_of_matches - number_to_remove
            return True
        else:
            return False

    # TODO - make it less ugly
    def get_row_as_string(self):
        row = ' '
        for match in range(self.number_of_matches):
            row += "| "
        return row
