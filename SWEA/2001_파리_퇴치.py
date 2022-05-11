t = int(input())
max_sum= 0

for idx in range(1,t+1):
    n,m = map(int, input().split())
    tc = []
    for i in range(n):
        tc.append(list((map(int, input().split())))) #testcase 입력 끝

    for i in range(n-m+1):
        for j in range(n-m+1):
            sum = 0
            for k in range(m):
                for l in range(m):
                    sum+= tc[i+k][j+l]
            if sum>max_sum:
                max_sum = sum

    print(f"#{idx} {max_sum}")
    max_sum = 0
    

    