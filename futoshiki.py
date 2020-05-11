import random
import copy


class Piece:  # puzzle piece
    def __init__(self, value):
        self.value = value
        self.domain = [1, 2, 3, 4, 5]
        self.constraints = []


def file_browse(fname):  # open file function
    f = open(fname, "r")
    file_info = f.read().splitlines()
    inp_board = [line.split() for line in file_info]
    return inp_board[0:5], inp_board[6:11], inp_board[12:16]


inputboard, horiboard, vertboard = file_browse("finput2.txt")

arr = copy.deepcopy(inputboard)
nonzero = []


def setup(board):  # does a bit of forward checking
    for i in range(5):
        for j in range(5):
            if board[i][j] != '0':
                nonzero.append((i, j, int(board[i][j])))  # append row, col, val of nonzero
                board[i][j] = Piece(int(board[i][j]))
                board[i][j].domain = []
            else:
                board[i][j] = Piece(int(board[i][j]))  # set each part of board as a piece of puzzle
    for row in range(5):
        for i in range(4):
            if horiboard[row][i] == '>':
                # inequalities.append((row, i))
                if 1 in board[row][i].domain:
                    board[row][i].domain.remove(1)
                # board[row][i+1].domain.remove(5)
                board[row][i].constraints.append('>')  # [row][i] has to be > [row][i+1]
            if horiboard[row][i] == '<':
                # inequalities.append((row, i))
                if 5 in board[row][i].domain:
                    board[row][i].domain.remove(5)
                # board[row][i+1].domain.remove(1)
                board[row][i].constraints.append('<')  # [row][i] has to be < [row][i+1]
    for row in range(4):
        for i in range(5):
            if vertboard[row][i] == '^':

                if 5 in board[row][i].domain:
                    board[row][i].domain.remove(5)

                board[row][i].constraints.append('^')  # [row][i] has to be < [row+1][i]
            if vertboard[row][i] == 'v':
                # inequalities.append((row, i))
                if 1 in board[row][i].domain:
                    board[row][i].domain.remove(1)
                # board[row+1][i].domain.remove(5)
                board[row][i].constraints.append('v')  # [row][i] has to be > [row+1][i]
    return board


setup(inputboard)


def remove_row_val(board, val):  # value to be removed
    for elem in range(5):
        if val in board[elem].domain:
            board[elem].domain.remove(val)


def remove_col_val(board, col, val):
    for row in range(5):
        if val in board[row][col].domain:
            board[row][col].domain.remove(val)


def forwardcheck(board):
    for i in range(5):
        for j in range(5):
            if len(board[i][j].domain) == 1:
                board[i][j].value = board[i][j].domain[0]
                board[i][j].domain = []
            if board[i][j].value != 0:
                remove_row_val(board[i], board[i][j].value)
                remove_col_val(board, j, board[i][j].value)
                if ">" in board[i][j].constraints:
                    for elem in board[i][j + 1].domain:
                        if elem >= board[i][j].value:
                            board[i][j + 1].domain.remove(elem)

                if "<" in board[i][j].constraints:
                    for elem in board[i][j + 1].domain:
                        if elem <= board[i][j].value:
                            board[i][j + 1].domain.remove(elem)

                if "^" in board[i][j].constraints:
                    for elem in board[i + 1][j].domain:
                        if elem <= board[i][j].value:
                            board[i + 1][j].domain.remove(elem)

                if "v" in board[i][j].constraints:
                    for elem in board[i + 1][j].domain:
                        if elem >= board[i][j].value:
                            board[i + 1][j].domain.remove(elem)
            if len(board[i][j].domain) == 0 and board[i][j].value == 0:
                print("No solution")
    return board


forwardcheck(inputboard)

for i in range(len(inputboard)):
    for j in range(len(inputboard[i])):
        print(inputboard[i][j].domain)

temp = copy.deepcopy(inputboard)


def return_tups(board):
    tuples = []
    for i in range(5):
        for j in range(5):
            if len(board[i][j].domain) == 1:
                tuples.append((i, j))
    for i in range(5):
        for j in range(5):
            if len(board[i][j].domain) == 2:
                tuples.append((i, j))
    for i in range(5):
        for j in range(5):
            if len(board[i][j].domain) == 3:
                tuples.append((i, j))
    for i in range(5):
        for j in range(5):
            if len(board[i][j].domain) == 4:
                tuples.append((i, j))
    for i in range(5):
        for j in range(5):
            if len(board[i][j].domain) == 5:
                tuples.append((i, j))
    return tuples


print(return_tups(inputboard))


# helper function to test if a solution is usable
def complete(board):
    for i in range(5):
        for j in range(5):
            if board[i][j].value == 0:
                return False
    return True


# resets board to original state before it was passed in
def resetboard(board):
    for i in range(5):
        for j in range(5):
            board[i][j] = copy.deepcopy(temp[i][j])  # make sure temp doesnt get changed


def backtracking(board):
    tuples = return_tups(board)
    for tups in tuples:
        row = tups[0]
        col = tups[1]
        if len(board[row][col].domain) != 0 and board[row][col].value == 0:
            board[row][col].value = random.choice(board[row][col].domain)
            board[row][col].domain = []
            forwardcheck(board)

        # if we have a contradiction, backtracking begins
        elif len(board[row][col].domain) == 0 and board[row][col].value == 0:
            resetboard(board)
            backtracking(board)
    if complete(board):
        return board

    # backtracking(inputboard)


def printboard(board):
    for i in board:
        print(i)


def main():
    backtracking(inputboard)

    for i in range(5):
        for j in range(5):
            arr[i][j] = inputboard[i][j].value

    f = open("output_futo.txt", "w")
    i = 0
    while i < 5:  # 5x5
        f.write(str(arr[i]))
        f.write("\n")
        i = i + 1
    f.write("\n")


main()