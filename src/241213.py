debug = False

n, m = map(int, input().split())
if debug:
    print(f"n: {n}, m: {m}")

board = []
for _ in range(n):
    row = list(input().strip())
    board.append(row)
    if debug:
        print(f"Row added: {row}")

if debug:
    print("First row:", board[0])

def check_board(x, y):
    cnt_B = 0
    cnt_W = 0
    for i in range(8):
        for j in range(8):
            if ((i + j) % 2 ==0) :
                if not (board[x + i][y + j] == 'B'):
                    cnt_B += 1
                if not (board[x + i][y + j] == 'W'):
                    cnt_W += 1

            else :
                if not (board[x + i][y + j] == 'W'):
                    cnt_B += 1
                if not (board[x + i][y + j] == 'B'):
                    cnt_W += 1

    return min(cnt_W, cnt_B)

min_num = 500
for i in range (n - 8 + 1):
    for j in range(m - 8 + 1):
        min_num = min(min_num, check_board(i,j))


print(min_num)
