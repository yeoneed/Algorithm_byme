def atoi(num_str):
    sign = 1
    sum = 0
    num = list(num_str)
    if num[0]=='-':
        num=num[1:]
        sign = -1
    num_int = [int(i) for i in num]
    for i,v in enumerate(num_int):
        sum+= v*(10**(len(num)-1-i))
    return sign*sum


def main():
    print(atoi("5182"))
    print(atoi("-281"))
    print(atoi("0"))
    print(atoi("-0"))

if __name__ == "__main__":
    main()