import sys
from itertools import combinations

tall = []

for i in range(9):
    tall.append(int(sys.stdin.readline().strip()))

result = list(combinations(tall, 7))

for i in result:
    if sum(i)==100:
        ans= list(i)
        for j in sorted(ans):
            print(j)
        break