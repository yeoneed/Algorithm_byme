#순차적으로 출력하는 함수 구현(재귀로)
def print_array(array, idx):
    if idx==len(array): #종료 조건일때
        print()         #개행 한 번 해주고
        return          #break 한다. 
    print(array[idx], end=' ')
    print_array(array, idx+1)

print_array(list(range(10)), 0) # 0 1 2 3 4 5 6 7 8 9