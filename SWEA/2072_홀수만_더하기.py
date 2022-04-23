t = int(input())

for i in range(1,t+1):
    s = list(map(int, input().split()))
    sum = 0
    for j in s:
        if j%2==1:
            sum+=j
    print(f"#{i} {sum}")

