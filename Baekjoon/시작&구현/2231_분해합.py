#첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
import sys 
n = int(sys.stdin.readline().strip()) #자연수 n 입력

for sang in range(1, n+1): #주어진 숫자까지 1부터 순차 탐색-> 런타임 에러 과외쌤께 질문
    num = sum(map(int, str(sang))) #생성자 각 자릿수의 합 구하기
    bun_hap = sang+num #분해합 = 생성자 + 생성자 각 자릿수의 합임을 이용
    if bun_hap == n: #조건을 만족하는 생성자 중 가장 작은 생성자를 출력하기
        print(sang)
        break #가장 작은 생성자만 출력하고 탐색 종료

if bun_hap!=n: 
    print(0)


 #if sang==n: #생성자랑 분해합이랑 같으면 분해합 없다는 뜻-> 0출력
       # print(0)
