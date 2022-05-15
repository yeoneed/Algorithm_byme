import sys
from itertools import combinations

#리스트 입력

read_ints = lambda: list(map(int,sys.stdin.readline().rstrip().split()))
read_int = lambda: read_ints()[0]

def combi(s,n):
    for i in range(n):
        for j in range(i, n):
            if s[i][j]!=0:
                


def main():
    n = read_int()

    for i in range(n):
        s = read_ints()

if __name__ == "__main__":
    main()