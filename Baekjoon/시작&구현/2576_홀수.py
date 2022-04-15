#7개의 자연수가 주어질 때, 이들 중 홀수인 자연수들을 모두 골라 그 합을 구하고, 고른 홀수들 중 최솟값을 찾는 프로그램을 작성하시오.
import sys
odd = []

for i in range(7):
    num = int(sys.stdin.readline().strip())
    if num%2==1:
        odd.append(num)

if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)

