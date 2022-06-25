#합병 정렬
import sys

sys.stdin = open("input.txt")

def print_array(lst):

def merge_sort(lst):
    if len(lst)==1:
        return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    new = [0 for _ in range(len(lst))]
    for i in range(len(lst)):
        l = 0
        r = 0
        if left[l]<right[r]:
            new[i]= left[l]
            l+=1
        else:
            new[i]= right[r]
            r+=1



def main():
    array = list(reversed(range(10)))
	print_array(array)
	array = merge_sort(array)
	print_array(array)


if __name__ == "__main__":
    main() 