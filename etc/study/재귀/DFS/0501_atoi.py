def atoi(num_str): #문자형 숫자를 그냥 숫자로 바꾸는 함수(alphabet to int)
    num_lst = list(num_str)
    if num_lst[0]=='-':
        num_lst= num_lst[1:]
        flag = -1
    else:
        flag = 1

    return (atoi_recursive(num_lst)*flag)

def atoi_recursive(num_lst):
    if len(num_lst)==1:
        return int(num_lst[0])
    num = int(num_lst[-1])
    ret = atoi_recursive(num_lst[:-1])
    return ret*10 + num

def main():
    print(atoi("5182"))
    print(atoi("-281"))
    print(atoi("0"))
    print(atoi("-0"))

if __name__ == "__main__":
    main()