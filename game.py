import os

try:
    inp = input("Enter the knight's starting position: > ")
    x, y = tuple(map(int, inp.split()))
    assert (1 <= x <= 8) and (1 <= y <= 8)

except:
    print('Invalid dimensions!')
    exit(0)

chess = """ -------------------
8| _ _ _ _ _ _ _ _ |
7| _ _ _ _ _ _ _ _ |
6| _ _ _ _ _ _ _ _ |
5| _ _ _ _ _ _ _ _ |
4| _ _ _ _ _ _ _ _ |
3| _ _ _ _ _ _ _ _ |
2| _ _ _ _ _ _ _ _ |
1| _ _ _ _ _ _ _ _ |
 -------------------
   1 2 3 4 5 6 7 8 """.splitlines()


def kprint(x, y):
    r = 8 - y + 1
    c = x * 2 + 1
    row = chess[r]
    row = row[:c] + 'X' + row[c+1:]
    chess[r] = row


kprint(x, y)
print(os.linesep.join(chess))
