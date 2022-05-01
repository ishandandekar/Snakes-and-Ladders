class Snakes_and_Ladders:
    def __init__(self):
        self.nbrs = {}
        self.vertices = self.nbrs.keys()

    def _add_relation(self, vertex, edge):
        if vertex not in self.vertices:
            self.nbrs[vertex] = set()
            self.nbrs[vertex].add(edge)
        else:
            self.nbrs[vertex].add(edge)

    def print_edges(self, vertex):
        print(self.nbrs[vertex])

    def setup_game(self, number_of_players):
        for i in range(1, 100, 1):
            self._add_relation(i, i+1)
        # Ladders
        self._add_relation(2, 38)
        self._add_relation(4, 14)
        self._add_relation(9, 31)
        self._add_relation(21, 42)
        self._add_relation(28, 84)
        self._add_relation(51, 67)
        self._add_relation(72, 91)
        self._add_relation(80, 99)

        # Snakes
        self._add_relation(17, 7)
        self._add_relation(62, 19)
        self._add_relation(54, 34)
        self._add_relation(87, 36)
        self._add_relation(64, 60)
        self._add_relation(93, 73)
        self._add_relation(95, 75)
        self._add_relation(98, 79)

        self.player_pos = []
        for i in range(number_of_players):
            self.player_pos.append(1)

    def move_player(self, number_of_jumps, player_number):
        initial_position = self.player_pos[player_number-1]
        new_pos = initial_position+number_of_jumps
        if len(self.nbrs[new_pos]) == 2:
            new_pos = list(self.nbrs[new_pos])[-1]
        self.player_pos[player_number-1] = new_pos

        if self._endgame():
            print(
                f"Congratulations Player {player_number}!!!\nYou won the game!!!")
        else:
            print(f"Player {player_number} has been moved to {new_pos}")

    def _endgame(self):
        if 100 in self.player_pos:
            return True
        return False


if __name__ == '__main__':
    g = Snakes_and_Ladders()
    g.setup_game()
    print(g.move_player(1, 1))
