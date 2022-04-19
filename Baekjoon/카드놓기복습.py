import sys

read_ints = lambda: list(map(int, sys.stdin.readline().strip().split())) #리스트 입력 받기
read_int = lambda: read_ints()[0] #숫자 하나만 입력 받기

def permu(n,k,flag,s,res,idx,ans):
    if idx==k:
        ans.add(''.join(map(str, res)))
        return

    for i in range(n):
        if flag[i]==True:
            continue
        flag[i] = True
        res[idx] = s[i]
        permu(n,k,flag,s,res,idx+1,ans)
        flag[i] = False


def main():
    n = read_int() #리스트 길이
    k = read_int() #카드 몇 개 뽑을 지
    s = []
    res = [0] * k
    flag = [False]*n
    ans = set() #중복 숫자 없게 하기 위해서 집합 사용
    s = [read_int() for _ in range(n)] #타이핑쳐서 입력받기

    permu(n,k,flag,s,res,0,ans)

    print(len(ans))
    
if __name__ == "__main__":
  main()

