import sys

read_ints = lambda: list(sys.stdin.readline().split())
read_int = lambda: int(read_ints()[0])

def permu(k, sign, check, flag, idx, max_str, min_str):
    if idx == k+1:
        result_num = ''.join(map(str, check))
        if int(result_num)>int(max_str): #이렇게 종료 조건에서 비교해주는 걸 많이 씀
            max_str = result_num
        if int(result_num)<int(min_str):
            min_str = result_num
        return max_str, min_str

    for i in range(10):
        if flag[i]==True:
            continue
        flag[i]=True
        check[idx] = i
       
        if idx>0 and sign[idx-1]=='<':
            if check[idx-1] > check[idx]:
                flag[i]=False
                check[idx]=False
                continue
        elif idx>0 and sign[idx-1]=='>':
            if check[idx-1] < check[idx]:
                flag[i]=False
                check[idx]=False
                return max_str, min_str

        max_str, min_str = permu(k,sign,check, flag, idx+1, max_str, min_str)

        flag[i]=False
        check[idx]=False

    return max_str, min_str
                
def main():
    basic = int(1e9) #int 안 씌워주면 기본 float형태로 저장됨
    k = read_int()
    sign = read_ints() #부등호 입력
    flag = [False] * 10
    check = [False] * (k+1)
    max_str = '0'
    min_str = str(basic)

    maxi, mini = permu(k, sign, check, flag, 0, max_str, min_str)
    
    print(maxi)
    print(mini)

if __name__ == "__main__":
    main()
