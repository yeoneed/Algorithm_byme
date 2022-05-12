t = int(input())

for idx in range(1,t+1):
    tc = input()

    for i in range(len(tc)//2): #반만 탐색하면 회문 검사 할 수 있음
        if tc[i] != tc[-1-i]:
            answer = 0
            break #break 통해서도 시간 복잡도 줄일 수 있음(조건 안맞으면 더이상 연산안하고 반복문 빠져나감)
        else:
            answer = 1

    print(f"#{idx} {answer}")
    
            