#N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 
# 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

import sys

def input():
    n,s = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))

def combi(lst,n,s,flag, idx):
    if idx==n:
        for i,f in enumerate(flag):
            if f:
                if sum(lst[i])==s:
                    cnt+=1
            

    flag[idx]=1
    combi(lst, n,s,flag, idx+1)
    flag[idx]=0
    combi(lst,n,s,flag, idx+1)




def main():
    n,s = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    idx=0
    flag = [False]*n
    combi(lst, n,s,flag, idx)

if __name__ == "__main__":
  main()