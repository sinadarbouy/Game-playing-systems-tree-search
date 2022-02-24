class Board:
    DEFAULT_BOARD_SIZE = 3

    def __init__(self, *args):
        print(len(args))
        if len(args) > 0:
            self.board = [[None for x in range(args[0])]
                          for y in range(args[0])]
        else:
            self.board = [[None for x in range(self.DEFAULT_BOARD_SIZE)]
                          for y in range(self.DEFAULT_BOARD_SIZE)]


c = Board(4)
print(c.board)
