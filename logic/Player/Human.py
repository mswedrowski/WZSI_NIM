from logic.Player.Player import Player

class Human(Player):
    def __init__(self):
        self.name = input("Enter the name of the player")

    def get_rownum(self):
        return int(input(self.name+" enter a row number"))

    def get_matches(self):
        return int(input(self.name+" enter number of matches you want to remove from a row"))

    def make_move(self):
        return self.get_rownum(), self.get_matches()
