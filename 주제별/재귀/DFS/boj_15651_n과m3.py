import sys
def read_ints(): return list(map(int, input().split()))
def read_int(): return read_ints()[0]


def dfs(n, m, result):
    if len(result) == m:  # 재귀 벗어날 예외 처리 작성
        print(' '.join([str(i) for i in result]))
        return
    for i in range(1, n+1):
        result.append(i)  # i를 추가
        dfs(n, m, result)  # 다시 탐색
        # 가장 최근에 넣은거 삭제하려면 pop, remove 함수는 리스트 앞 부터 탐색하며 해당 값과 일치하는 애를 삭제한다.
        result.pop()
    return


def main():
    n, m = read_ints()
    result = []
    dfs(n, m, result)


if __name__ == "__main__":
    main()
