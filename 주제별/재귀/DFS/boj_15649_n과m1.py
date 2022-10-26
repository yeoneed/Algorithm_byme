import sys
def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_int(): return read_ints()[0]


# 파이썬에서는 함수 안에 넣지 않으면 그냥 static으로 쓰임
result = []


def dfs(n, m):
    if len(result) == m:
        print(' '.join([str(i) for i in result]))
        return
    for i in range(1, n+1):
        if i not in result:
            result.append(i)
            dfs(n, m)
            result.remove(i)
    return


def main():
    n, m = read_ints()
    dfs(n, m)


if __name__ == "__main__":
    main()
