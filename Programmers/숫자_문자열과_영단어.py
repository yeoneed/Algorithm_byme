import sys
s = input()

def solution(s):
    dic = {'zero':0, 'one': 1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    for k in dic.keys():
        if k in s:
            s = s.replace(k, str(dic[k]))
    # print(s)
solution(s)

## 코멘트: 파이썬의 replace 는 해당 문자가 없을 시, 알아서 건너뛰기 때문에 if 문 써줄 필요가 없음!
