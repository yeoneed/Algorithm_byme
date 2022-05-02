def itoa(num):
    flag = 1
    if num<0:
        flag = -1
        num *=-1
    elif num==0:
        return '0'

    num_str = itoa_recursive(num)

    if flag==-1:
        num_str = '-'+num_str 
    return num_str

def itoa_recursive(num):
    if num==0:
        return ""
    num_str = str(num%10)
    ret = itoa_recursive(num//10)
    return ret+num_str

def main():
    print(itoa(5182))
    print(itoa(-281))
    print(itoa(0))

if __name__ == "__main__":
    main()