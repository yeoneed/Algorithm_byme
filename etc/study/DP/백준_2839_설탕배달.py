import sys

read_ints = lambda: list(map(int, sys.stdin.readline().strip().split()))
read_int = lambda: read_ints()[0]

def dp(n, save):
    if n==3 or n==5:
        return 1
    for i in range(4, n+1):
        if save[i-3]!=-1 and save[i-5]!=-1:
            save[i] = min(save[i-3], save[i-5]) +1
        elif save[i-3]==-1 and save[i-5]!=-1:
            save[i] = save[i-5]+1
        elif save[i-3]!=-1 and save[i-5]==-1:
            save[i] = save[i-3]+1
    
    return save[n]

def main():
    n = read_int()
    save = [-1] * (n+1)
    save[3] = 1
    if n>=5:
        save[5]=1
    print(dp(n,save))

if __name__ == "__main__":
    main()
