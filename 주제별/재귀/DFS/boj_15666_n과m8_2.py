import sys
from itertools import permutations


def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_int(): return read_ints()[0]


n, m = read_ints()
lst = read_ints()
lst.sort()
# visited = [0] * n  # 인덱스 기준으로 얘 썻나 안썻나 판단하는 거임!!


def main():
    # 순열 만들때 부터 중복 제거해서 result에 담고 정렬
    result = sorted(list(set(permutations(lst, m))))
    """
    for i in result:
        print(list(i))  # ( , ) 튜플 형태
    """

    for i in result:
        for j in i:
            print(j, end=" ")
        print()


if __name__ == "__main__":
    main()
