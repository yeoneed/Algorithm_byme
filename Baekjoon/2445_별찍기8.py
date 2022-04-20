import sys

n = int(sys.stdin.readline().strip())

#for i in range(1,n+1): 
    #print('*'*i + ' '*2*(n-i) + '*'*i)
#for i in range(n-1,0,-1):
    #print('*'*i + ' '*2*(n-i) + '*'*i)

for i in range(1,2*n):
    if i<=n:
        print('*'*i + ' '*2*(n-i) + '*'*i)
    else:
        i-=n
        print('*'*(n-i)+ ' '*2*i + '*'*(n-i))
