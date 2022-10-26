# duplicate ok, higher
import sys
def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_int(): return read_ints()[0]


n, m = read_ints()
lst = read_ints()
lst.sort()
result = []
visited = [0] * n


def dfs(lv):
    if lv == m:  # dfs에서는 lv 사용하기!
        print(' '.join([str(i) for i in result]))
        return

    overlap = 0  # 새로운 레벨에서는 overlap 변수 초기화

    for i in range(n):  # 인덱스 활용
        # 방문안한 수면서 그 전 수랑 같지 않은 수일 경우 result 에 추가
        if visited[i] == 1 or overlap == lst[i]:
            continue
        overlap = lst[i]  # 출력하고 다시 돌아왔을 때 바로 전에 추가했던 수랑 같은 수 추가 안하도록
        visited[i] = 1
        result.append(lst[i])
        dfs(lv+1)
        visited[i] = 0
        result.pop()
    return


def main():
    dfs(0)


if __name__ == "__main__":
    main()
