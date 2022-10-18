import sys
def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_int(): return read_ints()[0]
# 주어진 배열에서 m개의 수열 뽑기


def dfs(n, m, lst, result):
    if len(result) == m:
        print(' '.join([str(i) for i in result]))
        return
    for v in lst:
        if v in result:
            continue  # 이미 있는 수는 추가안함
        if result and v < max(result):  # 기존에 배열에 들어있는 수보다 새로 들어온 수가 작으면 다시 탐색
            continue
        result.append(v)
        dfs(n, m, lst, result)
        result.pop()
    return


def main():
    n, m = read_ints()
    lst = read_ints()  # 입력으로 들어오는 인자들 배열에 집어넣기
    lst.sort()
    result = []
    dfs(n, m, lst, result)


if __name__ == "__main__":
    main()
