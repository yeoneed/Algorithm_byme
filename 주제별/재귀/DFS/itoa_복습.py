def itoa(num):
    sign = 1
    if num<0:
        sign= -1
        num*=-1
    elif num==0:
        return 0
        
    result = itoa_recur(num)

    if sign==-1:
        result = '-'+result
    return result

def itoa_recur(num):
    if num==0:
        return ""
    remain = str(num%10)
    ret = itoa_recur(num//10)
    return ret+remain

def main():
    print(itoa(5182))
    print(itoa(-281))
    print(itoa(0))

if __name__ == "__main__":
    main()