# duplicate ok, higher
import sys
def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_int(): return read_ints()[0]


n, m = read_ints()
lst = read_ints()
lst.sort()
result = []


def dfs():
    if len(result) == m:
        print(' '.join([str(i) for i in result]))
        return

    for i in lst:
        result.append(i)
        dfs()
        result.pop()
    return


def main():
    dfs()


if __name__ == "__main__":
    main()
