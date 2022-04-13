#정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
import sys
n, x = map(int, sys.stdin.readline().split()) #n과 x 입력

a = list(map(int, sys.stdin.readline().split())) #a라는 list 입력 받기

for i in a:
    if i<x:
        print(i, end = ' ')
