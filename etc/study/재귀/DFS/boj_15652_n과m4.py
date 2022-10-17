import sys
def read_ints(): return list(map(int, input().split()))
def read_int(): return read_ints()[0]


def dfs(n, m, result, lv):
    if len(result) == m:  # 재귀 벗어날 예외 처리 작성
        print(' '.join([str(i) for i in result]))
        return
    for i in range(1, n+1):
        if i < lv:
            continue
        result.append(i)  # i를 추가
        lv = i
        dfs(n, m, result, lv)  # 다시 탐색
        # 가장 최근에 넣은거 삭제하려면 pop, remove 함수는 리스트 앞 부터 탐색하며 해당 값과 일치하는 애를 삭제한다.
        result.pop()  # 그 깊이에서 넣은거 삭제
    return


def main():
    n, m = read_ints()
    result = []
    dfs(n, m, result, 1)


if __name__ == "__main__":
    main()
