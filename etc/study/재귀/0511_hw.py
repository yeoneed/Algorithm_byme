import sys
from itertools import combinations

#리스트 입력

read_ints = lambda: list(map(int,sys.stdin.readline().rstrip().split()))
read_int = lambda: read_ints()[0]

def combi(s,n):
    result = list(combinations(s, n//2))
    print(result)


def main():
    n = read_int()
    idx_lst = [i for i in range(n)]
    combi(idx_lst,n)

    for i in range(n):
        s = read_ints()

if __name__ == "__main__":
    main()