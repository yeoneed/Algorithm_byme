import sys

n = int(sys.stdin.readline().strip())

for i in range(-n+1, n):
    k = abs(i)
    print(' '*(n-k-1) + '*'*(2*k+1))