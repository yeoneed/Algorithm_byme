import sys
read_ints = lambda: list(map(int, sys.stdin.readline().strip().split()))
read_int = lambda: read_ints[0]

def main():
    n = read_int()
    for i in range(n):
        min_val, max_val = read_ints()
        



if __name__ == "__main__":
    main()