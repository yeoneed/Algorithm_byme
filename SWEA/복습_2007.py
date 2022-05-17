t = int(input())

for idx in range(1,t+1):
    pat = input()
    n = len(pat)
    for i in range(n):
        if i>0 and pat[:i] == pat[i:2*i]:
            print(f"#{idx} {i}")
            break


