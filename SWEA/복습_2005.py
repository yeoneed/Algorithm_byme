t = int(input())

for idx in range(1,t+1):
    n = int(input())
    tc = [[0 for _ in range(n)] for _ in range(n)]

    print(f"#{idx}")
    for i in range(n):
        for j in range(n):
            if j==0 or j==i:
                tc[i][j]=1
            else:
                if i>=j:
                    tc[i][j] = tc[i-1][j-1] + tc[i-1][j]

            if tc[i][j]:
                print(tc[i][j], end = ' ')
        print()
