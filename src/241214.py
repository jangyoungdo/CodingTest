debug = False

n, m = map(int, input().split())
if debug:
    print(f"n: {n}, m: {m}")

board = []
for i in range(n):
    row = list(map(int, input().strip()))
    board.append(row)
    if debug:
        print(f"Row added: {row}")

if debug:
    print("First row:", board)

def find_square(_n,_m,_num):
    for i in range(_n -_num + 1):
        for j in range(_m -_num + 1):
            if board[i][j] == board[i+_num-1][j] == board[i][j+_num-1] == board[i+_num-1][j+_num-1]:
                return _num * _num
    return 0

num = min(n, m)
results = []

for i in range(1, num+1):
    if find_square(n, m, i) != 0:
        results.append(find_square(n, m, i))
    

print(max(results))

