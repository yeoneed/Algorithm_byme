import sys

read_ints = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
read_int = lambda: read_ints()[0]

def permu(lst, op_count, n, idx, answer):
   if idx==n-1:
      return answer, answer
   
   max_val = int(-1e10)
   min_val = int(1e10)
   for i in range(4):
        if op_count[i] == 0:
           continue
        op_count[i] -= 1
        result = calculate(answer, i, lst, idx)
        max_tmp, min_tmp = permu(lst, op_count, n, idx+1, result)
        op_count[i] += 1
        if max_val < max_tmp:
            max_val = max_tmp
        if min_val > min_tmp:
            min_val = min_tmp

   return max_val, min_val

        
def calculate(res, op, lst, idx):
   if op==0:
      res += lst[idx+1]
      return res
   elif op==1:
      res-= lst[idx+1]
      return res
   elif op==2:
      res*=lst[idx+1]
      return res
   elif op==3:
      if res>=0: 
         res= res//lst[idx+1]
         return res
      else: 
         res = abs(res)//lst[idx+1]
         return res*-1

def main():
    n = read_int()
    lst = read_ints()
    op_count = read_ints()
    answer = lst[0]
    
    max_val, min_val = permu(lst, op_count, n, 0, answer)
    print(max_val)
    print(min_val)

if __name__ == "__main__":
    main() 