import sys
import random

read_ints = lambda: list(map(int, sys.stdin.readline().strip().split()))
read_int = lambda: read_ints()[0] 

def game(hand, computer, re):
    if hand>computer or (hand==1 and computer==3):
        print("이겼습니다!!!")
        return 1

    elif hand==computer:
        print("비겼습니다!!!")
        return 0

    else:
        print("졌습니다!!!")
        return -1

    
def calculate(menu):

    if menu==1:
        re = 5
    elif menu==2:
        re = 3
    else:
        re = 1

    sum = 0
    limit = re//2 +1
    for i in range(re):
        computer = random.randrange(1,4)
        print("컴퓨터:", computer)
        print("가위바위보 중 하나 입력:")
        hand = read_int()
        sum += game(hand, computer, re)
        if sum>=limit:
            print("###인간 승")
            break
        elif sum<=(limit*-1):
            print("###컴퓨터 승")
            break
    

def main():
    print("가위바위보 게임을 시작합니다. 아래 보기 중 하나를 고르세요.")
    print("1. 5판 3승")
    print("2. 3판 2승")
    print("3. 1판 1승")

    print("번호를 입력하세요.", end = "")
    menu = read_int()
    calculate(menu)

        
if __name__ == "__main__":
    main()