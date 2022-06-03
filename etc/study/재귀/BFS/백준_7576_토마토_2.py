import sys
from collections import deque
#sys.stdin = open("input.txt")

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def is_valid_xy(n,m,a,b):
    return a>=0 and a<n and b>=0 and b<m

def bfs(n,m,board,start, answer):
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt=0
    q = deque()
    for (i,j) in start:
        q.append((i,j, 0))
    while q:
        x,y,step = q.popleft()
        cnt+=1 #값이 0,1인것만 큐에 들어가기 때문에
        if cnt==answer:
            return step
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if is_valid_xy(n,m,nx,ny)==1 and board[nx][ny]==0 and visited[nx][ny]!=1:
                q.append((nx,ny,step+1))
                visited[nx][ny]=1
    return -1
        
def solve(n,m,board):
    answer = 0 
    start = []
    for i in range(n):
        for j in range(m):
            if board[i][j]==0 or board[i][j]==1:
                answer +=1
            if board[i][j]==1:
                start.append((i,j))

    return(bfs(n,m,board,start,answer))

def main():
    m,n = list(map(int,sys.stdin.readline().strip().split()))
    board = [[] for _ in range(n)]
    for i in range(n):
        board[i] = list(map(int, sys.stdin.readline().strip().split()))

    step_num = solve(n,m,board)
    print(step_num)

if __name__ == "__main__":
    main()