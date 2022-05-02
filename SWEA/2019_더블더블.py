import sys

n = int(sys.stdin.readline())
result = 1

for i in range(n+1):
    print(result, end= ' ')
    result *= 2