import sys

def dfs(n, save):
    if save[n]!=-1:
        return save[n]
    elif n==0 or n==1:
        save[n] = n
    else:
        save[n] = dfs(n-2) + dfs(n-1)
    return save[n]

def main():
    n = int(input())
    save = [-1 for _ in range(10000)]
    
    fib = [-1 for _ in range(10000)]
    fib[0] = 0
    fib[1] = 1
    for i in range(2, 10000):
        fib[i] = fib[i-2] + fib[i-1]
    res = 0

#내일 복습 꼭 할 것


