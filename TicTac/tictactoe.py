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
        input_err = True
        while input_err:
            str_inp = input()
            if not str_inp.isdigit():
                print('Error: Invalid input format\nTry again!')
            elif int(str_inp) < 1 or int(str_inp) > 9:
                print('Error: Invalid cell number\nTry again!')
            elif self.board[int(str_inp)-1] != ' ':
                print('Error: This cell is already taken\nTry again!')
            else:
                input_err = False
        return int(str_inp)

    def start_game(self):
        self.board = [' ']*9
        self.cur_sym = '0'
        self.combs = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
        print('Start!')
        print('Cell numbers:')
        self.show_board(list(range(1, 10)))

    # Returns the characters in the specified row/column/diagonal
    def get_combination(self, comb):
        return self.board[comb[0]]+self.board[comb[1]]+self.board[comb[2]]

    def check_winner(self):
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
        x = self.validate_input()
        self.board[x-1] = self.cur_sym
        self.show_board()


if __name__ == "__main__":
    game = TicTacGame()
    game.start_game()
    winner = None
    while not winner:
        game.make_move()
        winner = game.check_winner()
    print(winner)
