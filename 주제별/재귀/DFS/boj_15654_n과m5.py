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
        result.append(v)
        dfs(n, m, lst, result)  # 값 반영을 위해서 result를 넘겨줌
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
