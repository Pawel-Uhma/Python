import random
import tkinter as tk

random.seed(a=None, version=2)

board = [[0 for x in range(9)] for y in range(9)]

numbers_to_place = 81


def place_numbers_on_board():
    for number in range(numbers_to_place):
        placed = False
        while not placed:
            placed = can_place(random.randint(0, 8), random.randint(0, 8), random.randint(1, 9))


def can_place(x, y, number_to_place):  # x - column    y - row
    print(x, y, number_to_place)
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
            if board[i][j] == number_to_place:
                return False

    return True

    board[x][y] = number_to_place
    return True


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


def build_window():
    window = tk.Tk()
    for i in range(9):
        window.columnconfigure(i, weight=1, minsize=50)
        window.rowconfigure(i, weight=1, minsize=50)
        for j in range(9):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j, padx=1, pady=1)
            label = tk.Label(master=frame, text=str(board[i][j]))
            label.pack()
    regenerate_button = tk.Button(master=window, text="Regenerate", command=place_numbers_on_board())
    regenerate_button.grid(row=9, column=0, sticky="nsew")
    solve_button = tk.Button(master=window, text="Solve", command=place_numbers_on_board())
    solve_button.grid(row=9, column=3, sticky="nsew")
    window.mainloop()


place_numbers_on_board()
print_board()
