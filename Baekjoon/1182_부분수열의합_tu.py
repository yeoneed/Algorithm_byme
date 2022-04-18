#N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 
# 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.
#
import sys

def combi(lst,n,s,flag, idx):
    if idx==n:
        if sum(flag) == 0: #아무것도 안 더한 경우에서 s=0랑 같은 경우의 수는 res에서 제외
            return 0
        for i,f in enumerate(flag):
            if sum([lst[i] for i,f in enumerate(flag) if f==1])==s:
                return 1
        return 0
    
    res=0 #모든 수의 합이 s인지 아닌지 판별하는 변수, 합이 s이면 1 더하기 누적
    flag[idx]=1
    res += combi(lst, n, s, flag, idx+1)
    flag[idx]=0
    res += combi(lst, n, s, flag, idx+1)
    return res #이거 안하면 바로위의 코드 res = combi(~~)에서 int형인 res와 반환없는 combi=Nonetype 사이의 매칭 오류 발생

def main():
    n,s = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    idx=0
    flag = [False]*n
    ans = combi(lst, n,s,flag, idx)
    print(ans)

if __name__ == "__main__":
  main()