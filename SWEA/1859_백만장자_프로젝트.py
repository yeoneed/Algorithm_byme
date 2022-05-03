t = int(input())

for i in range(1,t+1):
    n = int(input())
    tc = list(map(int, input().split()))
    max_sell = tc[-1]
    max_profit = 0
    for idx in range(len(tc)-1, -1, -1):
        if tc[idx]<max_sell:
            max_profit += max_sell-tc[idx]
        elif tc[idx]>max_sell:
            max_sell = tc[idx]
    print(f"#{i} {max_profit}")
            

    