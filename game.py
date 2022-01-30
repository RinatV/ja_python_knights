import os

# tstdin = ["4 3", "1 1", "3 2", "1 3", "2 1", "4 2", "2 3", "3 1", "1 2", "3 3", "4 1", "2 2", "4 3"]
stdin = []


def input_xy(msg, value_errmsg, assert_func=lambda x, y: x > 0 and y > 0):
    while True:
        try:
            if 'tstdin' not in globals():
                inp = input(msg)
            else:
                inp = tstdin.pop(0)
                print(msg, inp)
            x, y = tuple(map(int, inp.split()))
            assert assert_func(x, y)
        except (ValueError, AssertionError):
            print(value_errmsg)
        else:
            stdin.append(f'{x} {y}')
            return x, y


size_x, size_y = input_xy('Enter your board dimensions: ', 'Invalid dimensions!')


def is_inboard(x, y):
    return 1 <= x <= size_x and 1 <= y <= size_y


x, y = input_xy("Enter the knight's starting position: ", 'Invalid position!', is_inboard)
start_x, start_y = x, y

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


def landings(x, y):
    positions = set()
    for dx, dy in [(1, 2), (2, 1), (-1, -2), (-2, -1), (-1, 2), (2, -1), (1, -2), (-2, 1)]:
        if 1 <= x + dx <= size_x and 1 <= y + dy <= size_y:
            positions.add((x + dx, y + dy))
    return positions


def landing_positions():
    positions = set()
    for x, y in knights:
        positions.update(landings(x, y))
    return positions


stop = False


def warnsdorff(x, y):
    cells = set(knights)
    cells.add((x, y))
    positions = landings(x, y)
    counter = 0
    for cell in positions:
        if not cell in cells:
            counter += 1
    return counter


last = [start_x, start_y]


def horizontal_line(row):
    line = f"{left_label(row)}|"
    moves = None
    for col in range(1, size_x + 1):
        if (col, row) in knights:
            if col == last[0] and row == last[1]:
                line += cell(' ', ' ', 'X')
            else:
                line += cell(' ', ' ', '*')
        elif (col, row) in landings(x, y):
            cell_moves = warnsdorff(col, row)
            moves = moves if cell_moves == 0 else True
            line += cell(' ', ' ', cell_moves)
        else:
            line += cell(' ', '_', '')
    line += ' |'
    return line, moves


def chess_board():
    board = []
    board.append(horizontal_divider())
    moves = None
    for hor in range(size_y, 0, -1):
        line, line_moves = horizontal_line(hor)
        moves = moves or line_moves
        board.append(line)
    board.append(horizontal_divider())
    board.append(bottom_nums())
    return os.linesep.join(board), moves


print(chess_board()[0])


def is_posible(x, y):
    return is_inboard(x, y) and not (x, y) in knights and (x, y) in landings(*last)


while True:
    x, y = input_xy("Enter your next move: ", 'Invalid move!', is_posible)
    last[0], last[1] = x, y
    _, moves = chess_board()
    knights.add((x, y))
    board, _ = chess_board()
    print(board)
    if len(knights) == size_x * size_y:
        print('What a great tour! Congratulations!')
        break
    if moves is None:
        print('No more possible moves!')
        print(f'Your knight visited {len(knights)} squares!')
        break
