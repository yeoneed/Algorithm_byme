#tutoring 에서 사용
import sys
from itertools import combinations

read_ints = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
read_int = lambda: read_ints()[0]

def combination(S, flag, idx):
    if idx==len(S): #종료 조건
        if sum(flag)==6: #flag 리스트의 합이 6이면 flag==1인 해당 인덱스의 S값들을 출력하기
            for i,f in enumerate(flag):
                if f: #flag 리스트에서 값이 1인 원소일 때
                    print(S[i], end=' ') #해당 인덱스 i의 S값을 출력
            print()
        return

    flag[idx]=1
    combination(S, flag, idx+1)
    flag[idx]=0
    combination(S,flag, idx+1)

def solve(K, S):
    idx = 0
    flag = [False] * len(S) 
    combination(S, flag, idx)
    print() #한 쌍 실행하고 개행

while True:
    tmp = read_ints()
    K = tmp[0]
    if K == 0:
        break
    S = tmp[1:]
    solve(K, S)







