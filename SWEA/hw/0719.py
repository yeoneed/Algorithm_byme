#섬나라 다리짓기
#bfs 문제 같은데,,

import sys
from collections import deque

sys.stdin = open("0719.txt")

read_ints = lambda: list(map(int, sys.stdin.readline().strip().split()))
read_int = lambda: read_ints()[0] 

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def is_valid_xy(n,x,y):
    return x>=0 and x<n and y>=0 and y<n

def bfs(n,board,visited,start_x,start_y):
    q = deque()
    q.append((start_x,start_y))
    visited[start_x][start_y]=1 #큐에 넣으면 바로 방문처리, 그 점 기준으로 탐색 또 하겠다는 소리니까
    size = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if is_valid_xy(n,nx,ny)==1 and board[nx][ny]==1 and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=1
                size+=1 #큐에 상하좌우 탐색해서 다른 거 들어오는 순간 섬의 사이즈 증가시키기
    return size

def solve(n, board):
    max_size = -1e9
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]== 1 and visited[i][j] ==0:
                size = bfs(n,board,visited,i,j) #각 섬의 사이즈 반환받음
                if max_size<size:
                    max_size = size
    return max_size

def main():
    n = read_int()
    board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        board[i] = read_ints()

    print(solve(n,board))


if __name__ == "__main__":
    main()