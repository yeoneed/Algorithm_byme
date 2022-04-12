#n이 제곱수이면 1을 반환, 제곱수가 아니면 0을 반환하는 함수 func3(n) 작성하기, n은 10억 이하의 자연수
#return이랑 break 같이 사용 안 함! return안에 함수 종료가 포함되어 있기 때문에

def func3(n):
    for i in range(2, n): #제곱근 질문: c언어는 for(i=1; i*i=n 이런식으로 범위를 제한할 수 있는데 파이썬에서는 그런식으로 어떻게 하는지)
        if i*i==n:
            return 1
            
    return 0

print(func3(121))

#시복: O(n)