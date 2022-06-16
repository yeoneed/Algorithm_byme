import sys

read_ints = lambda: list(map(int, sys.stdin.readline().strip().split()))
read_int = lambda: read_ints()[0]

def dp(n, save):
    for i in range(6, n+1):
        save[i] = min(save[i-3], save[i-5]) +1
    return save[n]
def main():
    n = read_int()
    save = [-1] * (n+1)
    save[3] = 1
    save[5] = 1
    save[4] = -1
    print(dp(n,save))


if __name__ == "__main__":
    main()
