import sys
from collections import deque

sys.stdin = open("input.txt")

d = ['D', 'S', 'L', 'R']

def D(num):
    return num*2%10000

def S(num):
    return num-1 if num!=0 else 9999

def L(num):
    return num%1000 * 10 +num//1000

def R(num):
    return num//10 + num%10 * 1000

    
def bfs(start, end):
    q = deque()
    visited = [0 for _ in range(10000)]
    q.append((start, 0))
    visited[start] =1

    while q:
        now, step = q.popleft()
        if now==end:
            return step
        for i in range(4):
            move = d[i]
            if move=='D':
                next = D(now)
            elif move=='S':
                next = S(now)
            elif move=='L':
                next = L(now)
            else:
                next = R(now)

            q.append((next, step+1))
            visited[next] =1

    return -1   
            
            
def solve(start, end):
    print(bfs(start, end))
    
def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        a,b = list(map(int, sys.stdin.readline().strip().split()))
        solve(a,b)

if __name__ == "__main__":
    main()