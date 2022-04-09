#"Hello, World! Hello, Python!”에서 “Hello” 등장 횟수 찾기
s = "Hello, World! Hello, Python!, Hello"
cnt = 0
idx = -1

while True:
    idx = s.find("Hello", idx+1) #세번째 인자 안 줄 때 기본값: len(s)
    if idx==-1:
        break
    cnt+=1 #if문이 break면 어짜피 빠져나가니까 else 안 붙여도 됨

print(cnt) # 2
