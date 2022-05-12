#10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.
#(소수점 첫째 자리에서 반올림한 정수를 출력한다.)

t = int(input())

for idx in range(1,t+1):
    tc = list(map(int, input().strip().split()))

    tc.remove(max(tc))
    tc.remove(min(tc))

    avg = round(sum(tc)/len(tc))

    print(f"#{idx} {avg}")