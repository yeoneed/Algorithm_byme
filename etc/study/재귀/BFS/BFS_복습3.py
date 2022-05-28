#length.py ((0, 0)부터 (n-1, m-1)까지의 최단 경로 길이 구하기)

from collections import deque

dx = [-1,1,0,0] #상 하 좌 우
dy = [0,0,-1,1]

def is_valid_xy(n,m,x,y):
    return x>=0 and x<n and y>=0 and y<m

def solve(n, m, board):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    length = bfs(n,m,board, visited, 0,0, n-1, m-1)
    return length

def bfs(n,m,board,visited,start_x, start_y, dst_x, dst_y):
    q = deque()
    q.append((start_x, start_y, 0))
    visited[start_x][start_y] =1
    while q:
        x,y,l = q.popleft()
        if (x,y)== (dst_x, dst_y): #목표 좌표에 도착 시 처음부터의 해당 좌표까지의 길이 반환
            return l
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if is_valid_xy(n,m,nx,ny)==1 and board[nx][ny]==1 and visited[nx][ny]==0:
                q.append((nx, ny, l+1))
                visited[nx][ny] =1
    return -1

def history()
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
  length = solve(n, m, board)
  print(length)

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
  length = solve(n, m, board)
  print(length)

if __name__ == "__main__":
  main()