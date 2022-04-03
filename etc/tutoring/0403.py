#lst = [i for i in range(10)] -> i 가 0부터 9까지 돌면서 i를 출력한다. 
#-> 각 알파벳의 역할, 왜 쓰는지(=역할) 잘 생각하기
#remove_lst =set([4,7,8]) #set은 중복 원소 고려x
#print(lst[:-1]) #lst[:-1]=> 인덱스 -1은 len(lst)-1임

#lst2 = [i for i in lst if i not in remove_lst]
#-> i 가 lst 범위에서 도는데 remove_lst에 없는 경우만 i 형태를 가져온다. 
#-> i for i에서 i는 가져오는 "형태"
#print(lst2)

#dic 복습
#d = {'a': 6, 'b': 4, 'c': 8}
#tmp = dict([(v, k) for k, v in d.items()])
#=> 튜플 (v,k) 형태를 가져온다-> k,v에서-> 어디에 있는 k,v? d.items()에 있는 k,v
#-> 근데 가져온 튜플 (v,k)형태를 다시 dictionary 로 바꾸겠다. 
#print(tmp)

#get_key = lambda d: d[1] #람다에서 d: d[1] 이렇게 한 칸 띄워주는 게 아래처럼 함수 선언하고 엔터 띄워주는거랑 같음
#= def func():
#      blabla~~

#d2 = sorted(d.items(), key=lambda x: x[1])
#d3 = [k for k,v in d2]
#print(d3)


lists = []
lists.append([5, 6, 7, 8])
lists.append([5, 6, 4, 5])
lists.append([1, 9, 3, 5])
get_key = lambda lst: lst[::-1]
lst2 = sorted(lists, key=get_key)
print(lst2)

실제 값          인덱스번호     get_key의 결괏값
[5, 6, 7, 8]        0          [8, 7, 6, 5]
[5, 6, 4, 5]        1          [5, 4, 6, 5]
[1, 9, 3, 5]        2          [5, 3, 9, 1]

2 1 0