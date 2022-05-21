#백준 2606 바이러스
from collections import deque

read_ints = lambda: list(map(int, input().split()))
read_int = lambda: read_ints()[0]

def bfs(graph, start_x, visited): #bfs는 그래프, 시작 노드, 방문 리스트 정보를 받음 
    q= deque()                    #덱을 선언
    q.append(start_x)             #덱에 시작 노드를 집어넣음
    while q:                      #덱에 아무것도 없을 때 까지
        start_node = q.popleft()  #덱에 가장 먼저 넣은 노드를 반환
        visited[start_node]=1     #해당 노드 방문 처리(꺼냈으면 무조건 반환!) 
        for nodes in graph[start_node]: #시작 노드와 연결된 노드들 중 아직 방문안한 노드들을 넣음
            if visited[nodes]!=1:
                q.append(nodes)           
#이런 과정을 통해서 더이상 1과 연결된 새로운 노드가 발견되지 않을 때 까지 탐색함

def main():
    cnt = 1
    node = read_int() #노드 개수 입력
    edge = read_int() #간선 개수 입력
    graph = [[] for _ in range(node+1)] #0부터 시작하기 때문에 노드수에 +1 만큼 내부 리스트를 만듬
    visited = [0] * (node+1) #방문 처리도 노드수+1 크기의 리스트 만듬
    for i in range(edge): 
        n1,n2 = map(int, input().split()) #노드 1,2를 입력받아서 그래프를 만듬
        graph[n1].append(n2) #그래프는 양방향 연결이기 때문에 양쪽 노드에 연결
        graph[n2].append(n1)
    
    bfs(graph, 1, visited) #만든 2차원 리스트 형태의 그래프를 bfs탐색
    
    print(sum(visited)-1) #방문한 노드에서 1 제외한 숫자 출력(1과 연결된 노드의 개수니까)

if __name__ == "__main__":
    main()