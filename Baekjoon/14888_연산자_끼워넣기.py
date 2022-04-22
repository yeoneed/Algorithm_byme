import sys

read_ints = lambda: list(map(int, sys.stdin.readline().rstrip().split()))
read_int = lambda: read_ints()[0]

def permu(cal, lst, flag, calres, n, idx, alst):
   if idx==n-1:
      answer = lst[0]
      for i in range(n-1):
         answer = calculate(answer, lst, calres, i)
      alst.append(answer)
      return

   for i in range(n):
      if flag[i]==1:
         continue
      flag[i] =1
      calres[idx]=cal[i]
      permu(cal, lst, flag, calres, n, idx+1,alst)
      flag[i]=0
        
def calculate(res, lst, calres, idx):
   if calres[idx]=='+':
      res += lst[idx+1]
      return res
   elif calres[idx]=='-':
      res-= lst[idx+1]
      return res
   elif calres[idx]=='*':
      res*=lst[idx+1]
      return res
   elif calres[idx]=='/':
      if res>=0: res/=lst[idx+1]
      else: 
         res*=-1
         res/= lst[idx+1]
         res*=-1

def main():
    n = read_int()
    lst = read_ints()
    o_cal= read_ints()
    cal = []
    cal = transcal(o_cal,cal)
    flag = [False]*len(cal)
    calres = []
    alst = []
    calres = permu(cal, lst, flag, calres, n, 0, alst)
    print(max(alst))
    print(min(alst))

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

if __name__ == "__main__":
    main() 


