#딕셔너리: 테이블이라고 생각해라
d = {'a':1, 'b':2, 'c':3}

print(d['c'])
print(d.get('e')) #딕셔너리에 없는 값 -> none으로 나옴

#키=인덱스만 출력하기, <keys(), values(), items() 는 함수임-> items() 괄호 꼭 붙여주기!>
for k in d.keys():
    print(k, end= ' ')
print()

#값만 출력하기
for v in d.values():
    print(v, end = ' ')
print()

#key, values를 f 사용해서 출력하기 ver1
for k in d.keys(): #d[k] = values 임
    print(f"{k}:{d[k]}")
print()

#key, values를 키 두 개 사용해서 출력
#items = 딕셔너리를 튜플 형태로 담고 있는 것
for k,v in d.items():
    print(f"{k}:{v}")
print()

#위의 딕셔너리를 컴프리핸션으로 출력
d2 = dict([(v,k) for k,v in d.items()])
print(d2)
