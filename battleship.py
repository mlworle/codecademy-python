# Battleship Game from CodeAcademy

from random import randint

board = []

for i in range(5):
    board.append(['O']*5)

def print_board(bd):
    for row in range(5):
        print " ".join(bd[row])

print "Let's play Battleship!"
print_board(board)

def random_col(board):
    return randint(0, len(board)-1)

def random_row(board):
    return randint(0, len(board)-1)

print ("Let's play Battleship!")
print ('You have 10 chances to find the ship. Good luck.')

ship_col = random_col(board)
ship_row = random_row(board)

# Loop the guesses
for turn in range(10):
    guess_row = int(raw_input('Guess Row: '))
    guess_col = int(raw_input('Guess Col: '))

    if turn < 11:
        if guess_row == ship_row and guess_col == ship_col:
            print ('Congratulations! You sank my battleship!')
            break
        else:
            if guess_row not in range(5) or guess_col not in range(5):
                print ('Ooops, that\'s not even in the ocean.')
            elif board[guess_row][guess_col] == 'X':
                print ('You guessed that one already.')
            else:
                board[guess_row][guess_col] = 'X'
                print_board(board)
                print ('You missed my battleship!')
        turn = turn + 1
        print ('Turn %d') %(turn)
    else:
        print ('Sorry. Game\'s over.')
