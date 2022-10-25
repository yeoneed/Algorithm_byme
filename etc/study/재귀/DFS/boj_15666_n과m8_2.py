import sys
from itertools import permutations


def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_int(): return read_ints()[0]


n, m = read_ints()
lst = read_ints()
lst.sort()
# visited = [0] * n  # 인덱스 기준으로 얘 썻나 안썻나 판단하는 거임!!


def main():
    result = list(permutations(lst, 2))
    """
    for i in result:
        print(list(i))  # ( , ) 튜플 형태
    """
    #result = list(set([i for i in result]))
    print(set([i for i in result]))
    result


if __name__ == "__main__":
    main()
