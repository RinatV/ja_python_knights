import os


def input_xy(msg, value_errmsg, assert_func=lambda x, y: x > 0 and y > 0):
    while True:
        try:
            inp = input(msg)
            x, y = tuple(map(int, inp.split()))
            assert assert_func(x, y)
        except:
            print(value_errmsg)
        else:
            return x, y


size_x, size_y = input_xy('Enter your board dimensions: ', 'Invalid dimensions!')


def is_inboard(x, y):
    return 1 <= x <= size_x and 1 <= y <= size_y


x, y = input_xy("Enter the knight's starting position: ", 'Invalid position!', is_inboard)

knights = set()
knights.add((x, y))

left_width = len(str(size_y))
cell_width = len(str(size_x)) + 1


def left_label(num):
    return str(num).rjust(left_width)


def cell(space, fill_char, value):
    return space + str(value).rjust(cell_width, fill_char)


def horizontal_divider():
    return f"{left_label('')}-{cell('-', '-', '') * size_x}--"


def bottom_nums():
    bottom = f"{left_label('')} "
    for num in range(1, size_x + 1):
        bottom += cell(' ', ' ', num)
    return bottom


def horizontal_line(row):
    line = f"{left_label(row)}|"
    for col in range(1, size_x + 1):
        if (col, row) in knights:
            line += cell(' ', ' ', 'X')
        else:
            line += cell(' ', '_', '')
    line += ' |'
    return line


def chess_board():
    board = []
    board.append(horizontal_divider())
    for hor in range(size_y, 0, -1):
        board.append(horizontal_line(hor))
    board.append(horizontal_divider())
    board.append(bottom_nums())
    return os.linesep.join(board)


print(chess_board())
