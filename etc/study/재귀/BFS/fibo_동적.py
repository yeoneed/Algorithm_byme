import sys

def fivo(num,save):
    if save[num]!=-1: #종료 조건(해당 save 값이 채워져 있을 경우 재귀 x)
        return save[num]
    elif num<=1: #save리스트 값이 비어있고
        save[num] = num
        #return save[num]
    else:
        save[num] = fivo(num-1, save) + fivo(num-2, save)
        #return save[num]
    return save[num] #각각 return 들어가는 거를 코드의 중복 줄이고자 바깥으로 뺌!
                    
def main():
    n = int(sys.stdin.readline()) #숫자 입력
    save = [-1 for _ in range(n+1)]
    fivo(n,save)
    print(save[-1])

if __name__ == "__main__":
    main()
