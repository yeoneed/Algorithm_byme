import sys


def read_ints(): return list(map(int, sys.stdin.readline().strip().split()))
def read_int(): return read_ints()[0]


def fibo(n, save):
    for i in range(3, n+1):
        save[i] = save[i-1] + save[i-2]
    return save[n]


def main():
    n = 8
    save = [0] * (n+1)
    save[1] = 2
    save[2] = 3
    print(fibo(n, save))


if __name__ == "__main__":
    main()
