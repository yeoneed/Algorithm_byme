t = int(input())

for idx in range(1,t+1):
    n = int(input())
    s= [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        for j in range(i+1):
            if j==0 or j==i: #양 끝 값이면 1로 채우기
                s[i][j] = 1
            else: #양 끝 값이 아니면 왼쪽위와 오른쪽위의 합으로 채우기
                s[i][j] = s[i-1][j-1]+s[i-1][j]
            
    print(f"#{idx}")
    for i in s:
        for j in i:
            if j!=0:
                print(j,end=' ')
        print()
    