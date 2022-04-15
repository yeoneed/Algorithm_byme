#다섯 개의 자연수가 주어질 때 이들의 평균과 중앙값을 구하는 프로그램을 작성하시오.
#from audioop import avg
import sys
lst = []

for i in range(5):
    num= int(sys.stdin.readline().strip())
    lst.append(num)
    
lst.sort()
print(sum(lst)//5)
print(lst[2])


