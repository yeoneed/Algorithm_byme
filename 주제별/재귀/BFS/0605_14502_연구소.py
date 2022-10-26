import sys
from itertools import combinations
from collections import deque
from copy import deepcopy as copy

#sys.stdin = open("input.txt")

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def is_valid_xy(n,m,x,y):
    return x>=0 and x<n and y>=0 and y<m

def bfs(n,m,board, start):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    for (i,j) in start:
        q.append((i,j))
        visited[i][j] =1

    cnt = 0
    while q:
        x,y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if is_valid_xy(n,m,nx,ny)==1 and board[nx][ny]==0 and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny]=1
    
    return cnt 

def main():
    n,m = list(map(int, sys.stdin.readline().strip().split()))
    board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    
    start_xy = []
    zero_lst = []
    wall_cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j]==0:
                zero_lst.append((i,j))
            elif board[i][j] == 1:
                wall_cnt += 1
            elif board[i][j] == 2:
                start_xy.append((i, j))
    
    #변수명 근접 선언
    min_val = int(1e9)
    for wall in combinations(zero_lst, 3):
        board_cp = copy(board)
        for (x, y) in wall:
            board_cp[x][y] = 1
        result = bfs(n,m,board_cp, start_xy)
        if min_val > result:
            min_val = result

    print(n * m - wall_cnt - 3 - min_val)

if __name__ =="__main__":
    main()