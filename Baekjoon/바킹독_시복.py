#n 이하의 자연수 중에서 3의 배수이거나 5의 배수인 수를 모두 합한 값을 반환하는 함수 func1을 작성하라. N은 5만 이하의 자연수
def func(n):
    result = 0
    for i in range(1, n): #시간 복잡도: n
        if i%3==0 or i%5==0: #연산 +2
            result += i      #연산+2(덧셈 한번, 결과 저장 한번)
    return result            #결과 반환 한번

print(func(16)) #시복 O(n)