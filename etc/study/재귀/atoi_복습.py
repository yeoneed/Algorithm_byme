def atoi(num_str):
    sign = 1
    num_lst = list(num_str)

    if num_lst[0]=='-':
        sign = -1
        num_lst = num_lst[1:]

    answer = atoi_recur(num_lst) * sign
    return answer


#재귀
def atoi_recur(lst):
    if not lst:
        return 0
    num = int(lst[-1])
    ret = atoi_recur(lst[:-1])
    result = num+ret*10
    return result

def main():
    print(atoi("5182"))
    print(atoi("-281"))
    print(atoi("0"))
    print(atoi("-0"))

if __name__ == "__main__":
    main()