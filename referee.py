# import playerOne
# import playerTwo

INITIAL_GRID = ["0000000",
                "0000000",
                "0000000",
                "0000000",
                "0000000",
                "0000000"]

class Grid(list):
    """A list of strings that contains a Connect Four grid."""

    HEIGHT = 6
    WIDTH = 7
    TOKEN_1 = "1"
    TOKEN_2 = "2"

    @property
    def lines(self):
        """Return a list of lines in self."""
        return self

    @property
    def columns(self):
        """Return a list of columns in self."""
        return [''.join(a) for a in [[self[i][j] for i in range(self.HEIGHT)]
                                     for j in range(self.WIDTH)]]

    @property
    def diagonals(self):
        """Return a list of diagonals from self of length is 4 or more."""
        diagonals = []
        for j in range(3, self.WIDTH - 1):  # We only want diagonals of
                                            # length 4 or more.
            diagonals.append([self[j-i][i] for i in range(j+1)])
            diagonals.append([self[j-i][self.WIDTH-1 - i] for i in range(j+1)])
            diagonals.append([self[self.HEIGHT-1-j+i][self.WIDTH-1-i]
                              for i in range(j+1)])
            diagonals.append([self[self.HEIGHT-1-j+i][i] for i in range(j+1)])
        return [''.join(a) for a in diagonals]

    @property
    def winner(self):
        """
        Return 1 or 2 if ones or twos have won, respectively, 0 otherwise.

        This property assumes there can only be one winner.
        """
        strings = ' '.join(self.lines + self.columns + self.diagonals)
        if self.TOKEN_1 * 4 in strings:
            return self.TOKEN_1
        elif self.TOKEN_1 * 4 in strings:
            return self.TOKEN_2
        return 0

    def __repr__(self):
        """Printing function for the grid."""
        return reduce(lambda a, b: a + '\n' + ' '.join(b), self, '')

    def move(self, j, token):
        """Mutate self such that token has played a move in column j."""
        for i in range(self.HEIGHT-1, -1, -1):
            if self[i][j] == "0":
                self[i] = self[i][:j] + token + self[i][j+1:]
                return self
        raise Exception('Invalid move')

class Referee(object):
    pass
