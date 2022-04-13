#우리나라 고유의 윷놀이는 네 개의 윷짝을 던져서 배(0)와 등(1)이 나오는 숫자를 세어 도, 개, 걸, 윷, 모를 결정한다. 
#네 개 윷짝을 던져서 나온 각 윷짝의 배 혹은 등 정보가 주어질 때 도(배 한 개, 등 세 개), 개(배 두 개, 등 두 개), 걸(배 세 개, 등 한 개), 윷(배 네 개), 모(등 네 개) 중 어떤 것인지를 결정하는 프로그램을 작성하라.

import sys
cnt=0

while cnt<3:

    n = list(map(int, sys.stdin.readline().split()))

    if sum(n)==1:
        print('C')
    elif sum(n)==2:
        print('B')
    elif sum(n)==3:
        print('A')
    elif sum(n)==4:
        print('E')
    else:
        print('D')
    cnt+=1
    