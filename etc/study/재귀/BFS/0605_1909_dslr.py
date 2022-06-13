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
    visited = [(-1, "X") for _ in range(10000)]
    q.append(start)
    visited[start] = (-2, "START")

    while q:
        now = q.popleft()
        if now==end:
            history(visited, end)
            break
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
            
            if visited[next] == (-1, "X"): #기본!! 아직 방문하지 않은 점에 대해서만 처리!
                q.append(next)
                visited[next] = (now, move)

    return


'''
def history(visited, end):
    val, move = visited[end]
    if (val, move) == (-2, "START"):
        print()
        return    
    else:
        history(visited, val)
        print(move, end='')
'''


def history(visited, now):
    if now == -2:
        print()
        return
    before, move = visited[now]
    history(visited, before)
    print(move, end="")
    
            
def solve(start, end):
    bfs(start, end)

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        a,b = list(map(int, sys.stdin.readline().strip().split()))
        solve(a,b)


if __name__ == "__main__":
    main()

#오늘은 swea 풀기