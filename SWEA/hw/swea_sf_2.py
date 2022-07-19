#문제: 주어진 리스트에서 홀수가 연속하거나 짝수가 연속하는 경우-> 리스트 원소 간 교환을 통해서 문제를 해결할 수 있다. 이때 그 교환 횟수를 출력하라
#예시) 7 3 8 4: 홀수 하나와 짝수 하나 교환하면 7 8 3 4 이런식으로 홀,짝이 번갈아 나오므로 문제 해결, 교환 횟수: 1

#import sys
#sys.stdin = open("input2.txt")
t = int(input())

def is_valid_tc(n,tc):
    tmp = [0 for _ in range(n)]
    if n==1:
            return 0

    for i in range(n): #주어진 값이 홀수라면 1을, 짝수라면 -1로 변환해 tmp에 넣음
        if tc[i]%2==1:
            tmp[i]= 1
        else:
            tmp[i]=-1
    
    if n%2==0: #주어진 리스트의 길이가 짝수일 때
        if sum(tmp)!=0: #tmp의 합이 0이 아니면(짝수나 홀수의 개수가 많으면 안되므로)
            return -1   #-1 return
    else: #주어진 리스트의 길이가 홀수일 때 
        if abs(sum(tmp))!=1: #짝수와 홀수의 개수가 1개 넘게 차이나면 -1 return
            return -1 

    return(solve(n, tc, tmp))#정상적인 리스트면 solve함수에 넣기

def solve(n, tc, tmp):
    cnt = 0
    base= [0 for _ in range(n)]

    if n%2==0: #리스트 길이 짝수면서
        if tmp[0]==1: #첫번째 숫자가 홀수면 정답 리스트(base)홀짝홀짝홀짝 이런식으로 돼야함
            for i in range(n):
                if i%2==0:
                    base[i]=1 #홀수면 1을 넣고
                else:
                    base[i] = -1 #짝수면 -1을 넣음
        else: #리스트 길이 짝수면서 첫번째 숫자가 짝수일 경우
            for i in range(n):
                if i%2==0:
                    base[i]=-1 #정답 리스트(base)는 짝홀짝홀짝홀 이런식으로 돼야함
                else:
                    base[i] =1
    else: #길이 홀수일 때
        if sum(tmp)==1: #홀수 더 많을 경우 1부터(첫번째 숫자 홀수여야 함) 시작해야 하므로
            for i in range(n):
                if i%2==0:
                    base[i]=1 #base는 홀짝홀짝홀 이런식
                else:
                    base[i] = -1
        else:
            for i in range(n): #짝수 더 많을 경우 -1(첫번째 숫자 짝수로) 부터 시작
                if i%2==0:
                    base[i]=-1 #base는 짝홀짝홀짝홀 이런식
                else:
                    base[i] =1

    for k in range(n):
        if tmp[k]!=base[k]: #테스트 케이스 짝홀 여부랑 정답 리스트 짝홀 여부 다른 경우: cnt 증가
            cnt+=1
    
    return cnt//2 #두 숫자를 '교환'하는 횟수 구하므로 cnt//2 해줌
                

def main():
    for t_idx in range(1,t+1):
        n = int(input())
        tc = list(map(int,(input().split())))
        answer = is_valid_tc(n,tc)
        print(f"#{t_idx} {answer}")
       
if __name__ == "__main__":
    main()