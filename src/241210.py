debug = True
num = []
for i in range(9):
    num.append(int(input()))

num = sorted(num)
target = sum(num) - 100

pairs = []
for i in num:
    for j in num:
        if((i != j) and (i + j == target)):
            pairs.append(tuple(sorted((i, j))))

pairs = set(pairs)
if pairs:
    pair = pairs.pop()
    for val in pair:
        num.remove(val)

for i in range(len(num)):
    print(num[i])
