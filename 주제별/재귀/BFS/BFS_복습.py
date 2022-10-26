#bfs 복습
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def is_valid_xy(n,m,x,y):
    return x>=0 and x<n and y>=0 and y<m

def bfs(n,m,board,visited,x,y):
    q = deque()
    q.append((x,y)) #입력받은 좌표 큐에 넣기
    visited[x][y]=1
    while q: #q가 빌 때까지 탐색
        start_x,start_y = q.popleft() #입력받은 좌표 꺼내기

        for i in range(4): #입력받은 좌표 상하좌우 돌면서 새로 방문할 점 탐색
            nx = start_x + dx[i]
            ny = start_y + dy[i]
            if is_valid_xy(n,m,nx,ny)==1 and board[nx][ny]==1 and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=1



def solve(n, m, board): #bfs 카운트 세는 함수
    cnt=0
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and visited[i][j]==0:
                bfs(n,m,board,visited,i,j)
                cnt+=1
    return cnt



def main():
  # case 1
  n = 15
  m = 14
  board = [
    '10000111100000',
    '11111101111110',
    '11011101101110',
    '11011101100000',
    '11011111111111',
    '11011111111100',
    '11000000011111',
    '01111111111111',
    '00000000011111',
    '01111111111000',
    '00011111111000',
    '00000001111000',
    '11111111110011',
    '11100011111111',
    '11100011111111'
  ]
  
  board = [list(map(int, row)) for row in board]
  cnt = solve(n, m, board)
  print(cnt)

  # case 2
  n = 5
  m = 5
  board = [
    '11000',
    '10001',
    '00101',
    '10001',
    '10111'
  ]
  board = [list(map(int, row)) for row in board]
  cnt = solve(n, m, board)
  print(cnt)

if __name__ == "__main__":
  main()