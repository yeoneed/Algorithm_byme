#1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.

t = int(input())

for idx in range(1,t+1):
    tc = int(input())
    sum=0

    for i in range(1,tc+1):
        if i%2==1:
            sum+=i
        else:
            sum-=i
    
    print(f"#{idx} {sum}")