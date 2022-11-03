import sys


def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_int(): return read_ints()[0]


n, m = read_ints()
lst = read_ints()
lst.sort()


def dfs(lv, result):
    if lv == m:  # 예외처리
        for i in result:
            print(i, end=" ")
        print()
        return

    lv_current = 0
    for i in range(n):
        if lv_current != lst[i]:
            lv_current = lst[i]
            if result and max(result) > lst[i]:
                continue
            result.append(lst[i])
            dfs(lv+1, result)
            result.pop()
    return


def main():
    result = []
    dfs(0, result)


if __name__ == "__main__":
    main()
