n = int(input())
result = 0

for i in range(1, n+1):
    i_list = map(int, str(i))
    result = sum(i_list) + i
    if(result == n):
        print(i)
        break
    
    if(i == n):
        print(0)
