from collections import deque
import sys

def bfs(graph, start, n):
    visited = [0 for _ in range(n+1)]
    length = 0
    q = deque()
    q.append(start)
    visited[start]=1
    while q:
        x = q.popleft()
        length+=1
        for i in graph[x]:
            if visited[i]!=1:
                q.append(i)
                visited[i]=1
    return length

def main():
    n,m = list(map(int, sys.stdin.readline().strip().split()))
    graph = [[] for _ in range(n+1)]
    max= -1e9
    answer = []

    for i in range(m):
        x, y = list(map(int, sys.stdin.readline().strip().split()))
        graph[y].append(x)

    for i in range(1,n+1):
        size = bfs(graph, i, n)
        if size>max:
            max = size
            answer= [i]
        elif size==max:
            answer.append(i)

    for i in answer:
        print(i, end = ' ')
    print()
    
if __name__ == "__main__":
    main()