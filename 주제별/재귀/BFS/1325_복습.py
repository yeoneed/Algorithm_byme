import sys
from collections import deque
#pypy3으로 해야 시간초과 없이 돌아감

def bfs(n,m,graph,start):
    visited = [False for _ in range(n+1)] #모든 노드 방문 초기화
    cnt = 0
    q = deque()
    q.append(start)
    visited[start]=True
    while q:
        x = q.popleft()
        cnt+=1
        for i in graph[x]:
            if visited[i]==False:
                q.append(i)
                visited[i]=1
    return cnt

def main():
    n,m = map(int, sys.stdin.readline().strip().split())
    graph = [[] for _ in range(n+1)]
    max = -1e9
    result = []

    for i in range(m):
        a,b = map(int, sys.stdin.readline().strip().split())
        graph[b].append(a)
    
    for start in range(1, n+1):
        cnt = bfs(n,m,graph, start)
        if max<cnt:
            max = cnt
            result = [start]
        elif max==cnt:
            result.append(start)
    
    for v in result:
        print(v, end = ' ')

if __name__ == "__main__":
    main()