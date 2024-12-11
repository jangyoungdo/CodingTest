debug = False

tri = []
for i in range(1, 45):
    num = int((i*(i+1))/2)
    if debug:
        print(num)
    tri.append(num)

if debug:
    print(tri)

ans = [0] * 1001
for i in tri:
    for j in tri:
        for k in tri:
            num = i + j + k
            if num <= 1000:
                ans[num] = 1

                 

T=int(input())
for i in range(T):
    N = int(input())
    if debug:
        print(N)
    print(ans[N])
