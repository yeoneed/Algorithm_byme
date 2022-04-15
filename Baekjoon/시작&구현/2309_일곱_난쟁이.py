#다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.
#난쟁이의 키 오름차순으로 출력
import sys

def input():
    tall = []
    for i in range(9): #난쟁이 키 입력
        tall.append(int(sys.stdin.readline().strip()))

    return tall

def combi(tall, flag, idx):
    if idx==len(tall): #종료 조건
        if sum(flag)==7:
            cnt=0
            tall2=[]
            for i,f in enumerate(flag):
                if f:
                    cnt+=tall[i]
            if cnt==100:
                for i,f in enumerate(flag):
                    if f:
                        tall2.append(tall[i])
            if tall2:
                for i in sorted(tall2):
                    print(i)
                sys.exit()    
        return

    flag[idx]=1
    combi(tall, flag, idx+1)
    flag[idx]=0
    combi(tall, flag, idx+1)

def main():
    height = input()
    flag = [False]*len(height)
    idx = 0
    combi(height, flag, idx)

if __name__ == "__main__":
  main()