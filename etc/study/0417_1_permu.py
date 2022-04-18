import sys

read_ints = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
read_int = lambda: read_ints()[0]

def permutation_recursive(seq, flag, results, N, M, idx):
    if idx==M:
        print(results)
        return
    for i in range(N):
        if flag[i]==True:
            continue
        flag[i] = True
        results[idx]=seq[i]
        permutation_recursive(seq, flag, results, N, M, idx+1)

def permuation_main(seq, M):
  print("***permutation***")
  N = len(seq)
  flag = [False] * N
  results = [0] * M
  permutation_recursive(seq, flag, results, N, M, 0)

def main():
  seq = read_ints()
  M = read_int()
  permuation_main(seq, M)

if __name__ == "__main__":
  main()