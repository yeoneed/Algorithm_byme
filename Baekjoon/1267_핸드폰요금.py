import sys
n = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))
res1=0
res2=0

for i in lst:
    res1 += 10+ (i//30)*10
    res2 += 15 + (i//60)*15
    
if res1<res2: print(f"Y {res1}")
elif res1>res2: print(f"M {res2}")
else: print(f"Y M {res1}")
