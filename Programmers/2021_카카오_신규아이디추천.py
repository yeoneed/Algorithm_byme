#1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
#2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
#3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
#4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
#5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
#6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     #만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
#7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

import sys
new_id = list(sys.stdin.readline().strip())
new_id2 = []
idx=-1

def solution(new_id):
    new_id= list(new_id)
    new_id2 = []
    idx=-1
    for k,v in enumerate(new_id): 
        new_id[k] = ord(new_id[k]) #10진 숫자로 바꾸기
        if new_id[k]>=65 and new_id[k]<=90: #알파벳 대문자면
            new_id[k]+=32 #소문자로 바꿔주기

#조건 만족하는 것만 new_id2에 넣기
        if (new_id[k]>=97 and new_id[k]<=122) or (new_id[k]>=48 and new_id[k]<=57) or new_id[k]==45 or new_id[k]==46 or new_id[k]==95:
            new_id2.append(new_id[k])
            idx+=1
            if len(new_id2)!=1: #문자 길이가 2 이상일때
                if new_id2[idx]==new_id2[idx-1]==46: #마침표가 연속 두개오면 그전꺼까지만 담기
                    new_id2= new_id2[:idx]
                    idx-=1

    if new_id2:
#마침표가 처음이나 끝에 있으면 제거
        if new_id2[0]==46:
                new_id2.remove(new_id2[0])

    if new_id2:
        if new_id2[-1]==46:
            new_id2.remove(new_id2[-1])

    if not new_id2:
        new_id2.append(97) #빈 문자열일 경우 a 대입

    if len(new_id2)>=16: #문자열 길이가 16 이상일 때 15번째까지만 출력
        new_id2= new_id2[:15]
        
    if new_id2[-1]==46:
            new_id2.remove(new_id2[-1]) #마지막 문자가 마침표일 경우 제거

    if len(new_id2)<=2: #new_id 길이가 2자 이하면 길이 3 될때까지 가장 마지막 문자 붙이기
        while True:
            new_id2.append(new_id2[-1])
            if len(new_id2)==3:
                break
    for k,v in enumerate(new_id2):
        new_id2[k] = chr(new_id2[k])

    answer = "".join(new_id2) 
    return answer
    
solution(new_id)
    


    