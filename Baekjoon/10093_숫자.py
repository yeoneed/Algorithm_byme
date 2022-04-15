#두 양의 정수가 주어졌을 때, 두 수 사이에 있는 정수를 모두 출력하는 프로그램을 작성하시오.
#첫째 줄에 두 수 사이에 있는 수의 개수를 출력한다.
#둘째 줄에는 두 수 사이에 있는 수를 오름차순으로 출력한다.

import sys

a,b = map(int, sys.stdin.readline().strip().split())
n = min(a,b)
m = max(a,b)
cha = m-n

if cha==0 or cha==1:
    print(0)
else:
    print(cha-1)
    for i in range(n+1, m):
        print(i, end=' ')