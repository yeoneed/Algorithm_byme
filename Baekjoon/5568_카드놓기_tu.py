#첫째 줄에 n이, 둘째 줄에 k가 주어진다. 셋째 줄부터 n개 줄에는 카드에 적혀있는 수가 주어진다.
import sys

read_ints = lambda: list(map(int,sys.stdin.readline().rstrip().split()))
read_int = lambda: read_ints()[0]

def permutation_recursive(seq, flag, results, N, M, idx, ans):
    if idx==M:
        ans.add(''.join(map(str, results))) #**
        return 
    for i,f in enumerate(flag):
        if flag[i]==True:
            continue
        flag[i] = True
        results[idx]=seq[i]
        permutation_recursive(seq, flag, results, N, M, idx+1, ans)
        flag[i]=False

def permuation_main(seq, M):
  #print("***permutation***")
  N = len(seq)
  flag = [False] * N
  results = [0] * M
  ans=set()
  permutation_recursive(seq, flag, results, N, M, 0, ans)
  print(len(ans))


def main():
  n = read_int()
  k = read_int()
  s = [read_int() for _ in range(n)]

  permuation_main(s,k)

if __name__ == "__main__":
  main()

    
