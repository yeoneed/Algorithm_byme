#재귀로 피보나치 수열 구현
import sys

def fibo(n,save):
    if save[n]!=-1: #이미 탐색한 경우
        return save[n]
    elif n==0 or n==1:
        save[n] = n
        return n
    else:
        save[n] = fibo(n-1, save) + fibo(n-2, save)
        return save[n]

def main():
    n = int(sys.stdin.readline())
    save = [-1 for _ in range(n+1)]
    print(fibo(n,save))

if __name__ == "__main__":
    main()