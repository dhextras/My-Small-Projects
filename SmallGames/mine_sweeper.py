import random
import re

class Board:
    def __init__(self, dimension_size, number_of_bombs):
        self.dimension_size = dimension_size
        self.number_of_bombs = number_of_bombs
        #so we can keep track of them later on

        self.board = self.make_board() 
        self.assigning_values_to_board()

        self.dug = set()

    def make_board(self):
        
        board = [[None for _ in range(self.dimension_size)] for _ in range(self.dimension_size)]
        #this will print [None, None ...... , None] N Times

        #planting the bombs
        bomb_planted = 0
        while bomb_planted < self.number_of_bombs:
            location = random.randint(0, self.dimension_size ** 2 -1)
            row = location // self.dimension_size 
            column = location % self.dimension_size
            
            if board[row][column] == '*':
                continue #no need to plant the bomb if there is already a bomb

            board[row][column] = '*'
            bomb_planted += 1

        return board

    def assigning_values_to_board(self):
        for rows in range(self.dimension_size):
            for columns in range (self.dimension_size):
                if self.board[rows][columns] == '*':
                    continue
                self.board[rows][columns] = self.get_neighbores_number(rows, columns)

    def get_neighbores_number(self, row, column):
        # let's iterate through each of the neighboring positions and sum number of bombs
        # top left: (row-1, column-1)
        # top middle: (row-1, column)
        # top right: (row-1, column+1)
        # left: (row, column-1)
        # right: (row, column+1)
        # bottom left: (row+1, column-1)
        # bottom middle: (row+1, column)
        # bottom right: (row+1, column+1)
        neighbore_bombs = 0
        for rows in range(max(0, row-1), min(self.dimension_size-1, row+1)+1):
            for columns in range(max(0, column-1), min(self.dimension_size-1, column+1)+1):
                #no need to check the box that we choosed
                if rows == row and columns == column:
                    continue 
                if self.board[rows][columns] == '*':
                    neighbore_bombs += 1

        return neighbore_bombs
    
    def dig(self, row , column):
        # dig at that location!
        # return True if successful dig, False if bomb dug

        # a few scenarios:
            # hit a bomb -> game over
            # dig at location with neighboring bombs -> finish dig
            # dig at location with no neighboring bombs -> recursively dig neighbors!
        self.dug.add((row, column)) #keep track
    
        if self.board[row][column] == '*':
            return False
        elif self.board[row][column] > 0:
            return True
        
        for rows in range(max(0, row-1), min(self.dimension_size-1, row+1)+1):
            for columns in range(max(0, column-1), min(self.dimension_size-1, column+1)+1):
                if (rows, columns) in self.dug:
                    continue
                self.dig(rows, columns)

        return True 

    def __str__(self):
        visible_board = [[None for _ in range(self.dimension_size)] for _ in range(self.dimension_size)]

        for row in range(self.dimension_size):
            for column in range(self.dimension_size):
                if (row,column) in self.dug:
                    visible_board[row][column] = str(self.board[row][column])

                else:
                    visible_board[row][column] = ' '


        #i need to see what is this
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dimension_size):
            columns1 = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns1, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dimension_size)]
        indices_row = '   '
        cells = []
        for idx, column in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (column))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, column in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (column))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dimension_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep


def play(dimension_size , number_of_bomb):
    # Step 1: create the board and plant the bombs
    board = Board(dimension_size, number_of_bomb)

    # Step 2: show the user the board and ask for where they want to dig
    # Step 3a: if location is a bomb, show game over message
    # Step 3b: if location is not a bomb, dig recursively until each square is at least
    #          next to a bomb
    # Step 4: repeat steps 2 and 3a/b until there are no more places to dig -> VICTORY!
    
    safe = True

    while len(board.dug) < board.dimension_size ** 2 - number_of_bomb:
        print(board)

        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row,col: "))
        row, column = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dimension_size or column < 0 or column >= board.dimension_size:
            print('Idiot Enter A Right Location .. ')
            print('')
            continue
        
        safe = board.dig(row, column)
        if not safe:
            break

    if safe:
        print('You Finished The Game Dude!! Congrats!')
        print('')
    else:
        print('You Lost Dude!!')
        print('')

    board.dug = [(rows, columns) for rows in range(board.dimension_size) for columns in range(board.dimension_size)]
    print(board)

def start():
    while True:
        mode = int(input('''Which Level You Wanna Play?
                        1. Easy
                        2. Medium
                        3. Hard
                        4. Custom
                        * Press '0' To Go Main Menu
                        => Choose: 
                        '''))

        if mode != 4:
            if mode == 1:
                choice1 = 4
                choice2 = 4
            elif mode == 2:
                choice1 = 7
                choice2 = 9
            elif mode == 3:
                choice1 = 10
                choice2 = 15
            elif mode == 0:
                break
            else:
                print('Invalid Choice!! ')
                print('')
        else:
            choice1 = 0
            
            #i dont know how to make the board if the dimension size go more then 10 
            # if it go more then ttaht board look not good 
            while not int(choice1) in range(1,10):
                print('''
Pls!! Consider The Range Of Both Board Size And Number Of Bombs. Then Choose (-_-)
''')
                custom = re.split(',(\\s)*', input('1. The Board Size {1 => 9} 2. Number Of Bombs. Like {7, 6}: '))
                choice1, choice2 = int(custom[0]), int(custom[-1])
                #and still cant figure it out how to stop before the number of bomb go mroe then the space there is.

        if mode == 1 or 2 or 3 or 4:
            play(choice1, choice2)
        else:
            continue