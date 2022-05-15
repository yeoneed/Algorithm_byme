def atoi(num_str):
    num_lst = list(num_str)
    num=0
    if num_lst[0] == "-":
        sign = -1
        num_lst = num_lst[1:]
    else:
        sign = 1
    
    num_lst = [int(i) for i in num_lst]
    for i,v in enumerate(num_lst):
        num += v * (10 ** (len(num_lst)-1-i))
    
    return sign * num
        


def main():
    print(atoi("5182"))
    print(atoi("-281"))
    print(atoi("0"))
    print(atoi("-0"))

if __name__ == "__main__":
    main()