#N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 
# 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.
#
import sys

def combi(lst,n,s,flag, idx):
    if idx==n:
        if sum(flag) == 0:
            return 0
        for i,f in enumerate(flag):
            if sum([lst[i] for i,f in enumerate(flag) if f==1])==s:
                return 1
        return 0
    
    res=0 #모든 수의 합이 s인지 아닌지 판별하는 변수 
    flag[idx]=1
    res += combi(lst, n, s, flag, idx+1)
    flag[idx]=0
    res += combi(lst, n, s, flag, idx+1)
    return res

def main():
    n,s = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    idx=0
    flag = [False]*n
    ans = combi(lst, n,s,flag, idx)
    print(ans)

if __name__ == "__main__":
  main()