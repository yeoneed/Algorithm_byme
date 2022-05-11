t = int(input())

for idx in range(1,t+1):
    n = int(input())
    s= [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        s[i][0] = 1
        s[i][i] = 1
    
    for i in range(1,n):
        for j in range(1,i+1):
            if s[i-1][j-1]!=0 and s[i-1][j]!=0:
                s[i][j] = s[i-1][j-1] + s[i-1][j]

    print(f"#{idx}")
    for i in s:
        for j in i:
            if j!=0:
                print(j, end= ' ')
        print()

