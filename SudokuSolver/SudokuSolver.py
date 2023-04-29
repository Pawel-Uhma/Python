import random
import time

random.seed(a=None, version=2)
start_time = time.time()


board = [[8, 0, 0,   0, 0, 0,    0, 0, 0],
         [0, 0, 3,   6, 0, 0,    0, 0, 0],
         [0, 7, 0,   0, 9, 0,    2, 0, 0],

         [0, 5, 0,   0, 0, 7,    0, 0, 0],
         [0, 0, 0,   0, 4, 5,    7, 0, 0],
         [0, 0, 0,   1, 0, 0,    0, 3, 0],

         [0, 0, 1,   0, 0, 0,    0, 6, 8],
         [0, 0, 8,   5, 0, 0,    0, 1, 0],
         [0, 9, 0,   0, 0, 0,    4, 0, 0]]

def can_place(x, y, number_to_place):  # x - column    y - row
    for column in range(9):
        if board[column][y] == number_to_place:
            return False
    for row in range(9):
        if board[x][row] == number_to_place:
            return False

    box_x = x // 3
    box_y = y // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[j][i] == number_to_place:
                return False
    return True


def solve():
    empty = find_empty()
    if not empty:
        return True
    else:
        x, y = empty
    for num in range(1, 10):
        if can_place(x, y, num):
            board[x][y] = num

            if solve():
                return True

            board[x][y] = 0
    return False


def find_empty():
    for column in range(9):
        for row in range(9):
            if not board[column][row]:
                return column, row
    return None


def print_board():
    for column in range(9):
        if column == 3 or column == 6:
            print("\n----------------------------------", end="")
        else:
            print("", end="")
        print("")
        for row in range(9):
            if board[column][row] == 0:
                print(" ", end="")
            else:
                print(board[column][row], end="")

            if row == 2 or row == 5:
                print("", end=" | ")
            else:
                print("", end="   ")



print_board()
solve()
print("\n\n------------------------------------------")
print_board()
print("\n\n--- %s seconds ---" % (time.time() - start_time))
