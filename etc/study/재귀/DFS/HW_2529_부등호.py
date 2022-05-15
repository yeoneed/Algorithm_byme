import sys

read_ints = lambda: list(sys.stdin.readline().split())
read_int = lambda: int(read_ints()[0])

def permu(k, sign, check, flag, idx, result):
    if idx == k+1:
        result_num = ''.join(map(str, check))
        result.append(result_num)
        return
    
    for i in range(10):
        if flag[i]==True:
            continue
        flag[i]=True
        check[idx] = i
       
        if idx!=0 and sign[idx-1]=='<':
            if check[idx-1] > check[idx]:
                flag[i]=False
                check[idx]=False
                continue
        elif idx!=0 and sign[idx-1]=='>':
            if check[idx-1] < check[idx]:
                flag[i]=False
                check[idx]=False
                return

        ret = permu(k,sign,check, flag, idx+1, result)
        flag[i]=False
        check[idx]=False

    return

def max_min(result):
    int_result = [int(i) for i in result]
    min_int = min(int_result)
    max_int = max(int_result)
    min_idx = int_result.index(min_int)
    max_idx = int_result.index(max_int)
    min_str = result[min_idx]
    max_str = result[max_idx]
    
    return max_str, min_str
            
                
def main():
    k = read_int()
    sign = read_ints() #부등호 입력
    flag = [False] * 10
    check = [False] * (k+1)
    result = [] 

    permu(k, sign, check, flag, 0, result)
    
    max_str, min_str = max_min(result)
    print(max_str)
    print(min_str)


if __name__ == "__main__":
    main()
