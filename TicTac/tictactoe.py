class TicTacGame:

    def show_board(self, board=None):
        if not board:
            board = self.board
        print('*-----------*')
        print('|', board[0], '|', board[1], '|', board[2], '|')
        print('|---|---|---|')
        print('|', board[3], '|', board[4], '|', board[5], '|')
        print('|---|---|---|')
        print('|', board[6], '|', board[7], '|', board[8], '|')
        print('*-----------*', flush=True)

    def validate_input(self):
        if not self.cur_input:
            self.cur_input = input()
        if not self.cur_input.isdigit():
            raise Exception('Error: Invalid input format')
        elif int(self.cur_input) < 1 or int(self.cur_input) > 9:
            raise Exception('Error: Invalid cell number')
        elif self.board[int(self.cur_input)-1] != ' ':
            raise Exception('Error: This cell is already taken')
        return int(self.cur_input)

    def start_game(self):
        self.board = [' ']*9
        self.cur_sym = '0'
        self.combs = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
        self.err = None
        self.cur_input = None

        print('Start!')
        print('Cell numbers:')
        self.show_board(list(range(1, 10)))

    # Returns the characters in the specified row/column/diagonal
    def get_combination(self, comb):
        return self.board[comb[0]]+self.board[comb[1]]+self.board[comb[2]]

    def check_winner(self):

        if self.err:
            return self.err

        for comb in self.combs:
            cur_str = self.get_combination(comb)
            if cur_str == self.cur_sym*3:
                return 'Game over : ' + self.cur_sym + ' is the winner!'

        # Removes from self.combs those combinations that are already filled
        self.combs = [x for x in self.combs if ' ' in self.get_combination(x)]

        if not self.combs:
            return 'Game over : Draw!'
        return None

    def make_move(self):
        self.cur_sym = '0' if self.cur_sym == 'x' else 'x'
        print('Player', self.cur_sym, 'turn : enter the cell number')
        try:
            pos = self.validate_input()
        except Exception as e:
            self.err = e
        else:
            self.board[pos-1] = self.cur_sym
            self.show_board()

    def validate_game(self, input_list):
        self.start_game()
        result = None
        for inp in input_list:
            self.cur_input = inp
            self.make_move()
            result = self.check_winner()
            if result:
                break
        return result


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
    winner = None
    while not winner:
        game.make_move()
        winner = game.check_winner()
    print(winner)
