import sys
def read_ints(): return list(map(int, input().split()))
def read_int(): return read_ints()[0]


def dfs(n, m, result):
    if len(result) == m:  # 재귀 벗어날 예외 처리 작성
        print(' '.join([str(i) for i in result]))
        return
    for i in range(1, n+1):
        if i not in result:  # 결과 배열에 i 가 없으면
            result.append(i)  # i를 추가
            dfs(n, m, result)  # 다시 탐색
            result.remove(i)
    return


def main():
    n, m = read_ints()
    result = []
    dfs(n, m, result)


if __name__ == "__main__":
    main()
