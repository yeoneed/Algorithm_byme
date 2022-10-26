import sys
from collections import deque

"""
이 문제에서 알아둬야 할 것:
1. result, flag등을 꼭 써야하는지, 안쓰고 그냥 종료조건에서 출력해도 되면 쓰지 말기
2. dfs든 bfs든 무조건 들어온 지점의 방문처리 부터 해주기!
3. 예외 조건은 dfs, bfs 맨 앞부분에 작성하기
4. pypy3보다 python3에서 왜 시간이랑 공간복잡도 둘다 작을까..?pypy3가 더 빠르다고 들었는데...

"""

#sys.stdin = open("input.txt")


def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_int(): return read_ints()[0]


def bfs(n, graph, v):
    visit = [0 for _ in range(n+1)]

    q = deque()
    q.append(v)

    while q:
        x = q.popleft()  # 큐의 특성인 FIFO를 사용하기 위해서는 popleft 사용해야 함(먼저 들어온 거부터 먼저 삭제)
        visit[x] = 1
        print(x, end=" ")
        for nodes in graph[x]:
            if visit[nodes] == 0 and nodes not in q:  # 큐에 없는 요소들만 새로 추가하기!
                q.append(nodes)


def dfs(n, graph, v, visited):
    # 항상 들어온 지점 "방문처리부터" 해주기!
    visited[v] = 1
    print(v, end=" ")
    for i in graph[v]:
        if visited[i] == 0:
            dfs(n, graph, i, visited)


def main():
    n, m, v = read_ints()
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)  # for range로 해도 되는데 간단한 거니까 그냥 곱셈으로 선언해주기!

    for i in range(m):
        a, b = read_ints()
        graph[a].append(b)
        graph[a].sort()
        graph[b].append(a)  # 그래프 생성
        graph[b].sort()

    dfs(n, graph, v, visited)
    print()
    bfs(n, graph, v)


if __name__ == "__main__":
    main()
