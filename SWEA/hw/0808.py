from collections import deque
import sys

read_ints = lambda: list(map(int, sys.stdin.readline().strip().split()))

def main():
    n,k = read_ints()
    q = deque()
    for i in range(n+1):
        q.append(i)
    




if __name__ == "__main__":
    main()