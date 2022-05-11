t = int(input())

for idx in range(1,t+1):
    tc = input()
    tc_lst = list(tc)
    
    for i in range(1, len(tc_lst)):
        if tc_lst[:i] == tc_lst[i:2*i]:
            print(f"#{idx} {i}")
            break 