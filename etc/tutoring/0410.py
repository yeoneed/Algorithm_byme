import sys

read_ints = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
read_int = lambda: read_ints()[0]

def combination_recursive(seq, flag, N, M, idx):
    if idx==N:
        if sum(flag)==M:
            for i,f in enumerate(flag):
                if f:
                    print(seq[i], end = ' ')
            print()
        return

    flag[idx]=1
    combination_recursive(seq, flag, N, M, idx+1)
    flag[idx]=0
    combination_recursive(seq, flag, N, M, idx+1)


def combination_main(seq, M):
  print("***combination***")
  N = len(seq)
  flag = [False] * N
  combination_recursive(seq, flag, N, M, 0)

def main():
  seq = read_ints()
  M = read_int()
  combination_main(seq, M)

if __name__ == "__main__":
  main()