#n이하의 수 중에서 가장 큰 2의 거듭제곱 수를 반환하는 함수 func4(n)을 작성해라. n은 10억 이하의 자연수
def func4(n):
    res = 1
    while res<n:
        res = 2*res
        
    return res//2

print(func4(34))

#print(2**5)

