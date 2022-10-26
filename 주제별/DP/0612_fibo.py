import sys
'''
def fibo(n,save):
    if save[n] != -1:
        return save[n]
    if n==0 or n==1:
        save[n]=n
        return save[n]
    save[n] = fibo(n-1, save) + fibo(n-2, save)
    return save[n]

def fibo(n, save):
    if save[n] == -1:
        if n == 0 or n == 1:
            save[n] = n
        else:
            save[n] = fibo(n-1, save) + fibo(n-2, save)
    return save[n]
    '''

def main():
    n = int(sys.stdin.readline().strip())
    save = [-1] * 21
    save[0] = 0
    save[1] = 1
    for i in range(2, 21):
        save[i] = save[i-1] + save[i-2]
    print(save[n])

if __name__ == "__main__":
    main()