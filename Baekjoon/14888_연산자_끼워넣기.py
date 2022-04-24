import sys

read_ints = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
read_int = lambda: read_ints()[0]

def permu(op, lst, flag, n, idx, answer):
   if idx==n-1:
      return answer, answer
   
   max_val = int(-1e10)
   min_val = int(1e10)
   for i,v in enumerate(op):
      if flag[i]==1:
         continue
      flag[i] = True
      result = calculate(answer, v, lst, idx)
      max_tmp, min_tmp = permu(op,lst,flag, n, idx+1, result)
      flag[i] = False
      if max_val < max_tmp:
         max_val = max_tmp
      if min_val > min_tmp:
         min_val = min_tmp

   return max_val, min_val

        
def calculate(res, op, lst, idx):
   if op=='+':
      res += lst[idx+1]
      return res
   elif op=='-':
      res-= lst[idx+1]
      return res
   elif op=='*':
      res*=lst[idx+1]
      return res
   elif op=='/':
      if res>=0: 
         res= res//lst[idx+1]
         return res
      else: 
         res = abs(res)//lst[idx+1]
         return res*-1

def transcal(o_cal, cal):
    for i in range(o_cal[0]):
       cal.append('+')
    for i in range(o_cal[1]):
       cal.append('-')
    for i in range(o_cal[2]):
       cal.append('*')
    for i in range(o_cal[3]):
       cal.append('/')
    return cal

def main():
    n = read_int()
    lst = read_ints()
    o_cal= read_ints()
    op = []
    op = transcal(o_cal,op)
    flag = [False]*len(op)
    answer = lst[0]
    
    max_val, min_val = permu(op, lst, flag, n, 0, answer)
    print(max_val)
    print(min_val)

if __name__ == "__main__":
    main() 


