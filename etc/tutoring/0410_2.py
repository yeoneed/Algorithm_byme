def print_array(array, idx):
    print(array[idx], end=' ')
    if idx+1<len(array):
        print_array(array, idx+1)

print_array(list(range(10)), 0) # 0 1 2 3 4 5 6 7 8 9