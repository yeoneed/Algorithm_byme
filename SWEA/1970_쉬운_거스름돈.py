t = int(input())

def solve(num):
    if num//50000!=0:
        print(num//50000, end = ' ')
        num = num%50000
        
    else: print(0, end = ' ') 

    if (num//10000)!=0:
        print(num//10000, end = ' ')
        num = num%10000
        
    else: print(0, end = ' ') 

    if (num//5000)!=0:
        print(num//5000, end = ' ')
        num = num%5000
        
    else: print(0, end = ' ') 

    if (num//1000)!=0:
        print(num//1000, end = ' ')
        num = num%1000
        
    else: print(0, end = ' ')

    if (num//500)!=0:
        print(num//500, end = ' ')
        num = num%500
        
    else: print(0, end = ' ') 

    if (num//100)!=0:
        print(num//100, end = ' ')
        num = num%100
        
    else: print(0, end = ' ') 

    if (num//50)!=0:
        print(num//50, end = ' ')
        num = num%50
        
    else: print(0, end = ' ') 

    if (num//10)!=0:
        print(num//10)
        num = num%10
        
    else: print(0) 
    
def main():
    for t_idx in range(1,t+1):
        n = int(input())
        print(f"#{t_idx}")
        solve(n)
        

if __name__ == "__main__":
    main()