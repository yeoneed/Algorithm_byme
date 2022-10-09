import sys
def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_int(): return read_ints()[0]


result = []


def permu(n, m, lv):
    if len(result) == m:
        print(' '.join([str(i) for i in result]))
    for i in range(lv, n+1):  # 1부터 n까지 돌면서 해당 숫자를 포함할지 안할지 정하면 됨
        if i not in result:
            result.append(i)
            permu(n, m, i+1)
            result.remove(i)
# static 변수 안쓰는 이유?: 헷갈림


def main():
    n, m = read_ints()  # n과 m입력
    permu(n, m, 1)


if __name__ == "__main__":
    main()
