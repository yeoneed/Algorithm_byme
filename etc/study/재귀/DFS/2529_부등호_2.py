read_ints = lambda: list(input().split())
read_int = lambda: int(read_ints()[0])

def permu(k, sign, check, flag, s, idx, result):
    if idx == k+1:
        result_num = ''.join(map(str, check))
        result.append(result_num)
        return result
    
    for i in range(10):
        if flag[i]==True:
            continue
        flag[i]=True
        check[idx] = i

        if flag[i]==1:       
            if idx!=0 and sign[idx-1]=='<':
                if check[idx-1] > check[idx]:
                    flag[i]=False
                    check[idx]=False
                    continue
            elif idx!=0 and sign[idx-1]=='>':
                if check[idx-1] < check[idx]:
                    flag[i]=False
                    check[idx]=False
                    return result

        ret = permu(k,sign,check, flag, s, idx+1, result)
        flag[i]=False
        check[idx]=False

    return result

def max_min(result):
    min_int = int(result[0])
    max_int = int(result[0])
    max_str = result[0]
    min_str = result[0]

    for i in result:
        if int(i)<min_int:
            min_int = int(i)
            min_str = i
        elif int(i)>max_int:
            max_int = int(i)
            max_str = i
    
    return max_str, min_str
            
                
def main():
    k = read_int()
    sign = read_ints() #부등호 입력
    flag = [False] * 10
    s= [int(i) for i in range(10)]
    check = [False] * (k+1)
    result = [] 

    result = permu(k, sign, check, flag, s, 0, result)
    
    max_str, min_str = max_min(result)
    print(max_str)
    print(min_str)



if __name__ == "__main__":
    main()