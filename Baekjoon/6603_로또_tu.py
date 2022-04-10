#tutoring 에서 사용
import sys
from itertools import combinations

read_ints = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
read_int = lambda: read_ints()[0]

def combination(s,flag, idx):
    if idx ==len(s):
        if sum(flag)==6:
            for i,f in enumerate(flag):
                if f:
                    print(s[i], end=' ')
            print()

        return

    flag[idx]=1
    combination(s,flag, idx+1)
    flag[idx]=0
    combination(s,flag, idx+1)

def solve(K, S):
    idx = 0
    flag = [False] * len(S) 
    combination(S,flag,idx)
    print()

while True:
    tmp = read_ints()
    K = tmp[0]
    if K == 0:
        break
    S = tmp[1:]
    solve(K, S)







