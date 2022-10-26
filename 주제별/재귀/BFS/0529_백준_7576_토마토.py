import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def is_valid_xy(n,m,a,b):
    return a>=0 and a<n and b>=0 and b<m

def bfs(n,m,board,start, answer):
    step = 0
    q = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]

    for (start_x,start_y) in start:
        q.append((start_x,start_y, step))
        visited[start_x][start_y] = 1

    while q:
        a,b,step = q.popleft()
        for i in range(4):
            na = a+dx[i]
            nb = b+dy[i]
            if is_valid_xy(n,m,na,nb)==1 and board[na][nb]==0 and visited[na][nb]==False:
                q.append((na,nb, step+1))
                visited[na][nb]=1
                board[na][nb]=1

    return is_valid_answer(answer,board,step)

def is_valid_answer(answer, lst, step):
    sum_num = 0
    for i in lst:
        sum_num+=sum(i)
    if sum_num==answer:
        return step
    return -1
    
def main():
    cnt = 0
    not_tomato = 0
    m,n = list(map(int,sys.stdin.readline().strip().split()))
    board = [[] for _ in range(n)]
    start = []

    for i in range(n):
        board[i] = list(map(int, sys.stdin.readline().strip().split()))
    
    for i in range(n):
        for j in range(m):
            if board[i][j]==1:
                start.append((i,j))
            elif board[i][j]==-1:
                not_tomato+=1

    answer = n*m-not_tomato*2

    step = bfs(n,m,board,start, answer)
    print(step)

if __name__ == "__main__":
    main()
