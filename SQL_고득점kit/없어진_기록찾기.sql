-- 코드를 입력하세요
# outer에는 있는데 in에 없는 애들 출력
# 1. 조인 하고 없는거 찾기
/*
select o.ANIMAL_ID, o.NAME
from ANIMAL_OUTS o 
where o.ANIMAL_ID NOT IN(
select b.ANIMAL_ID
from ANIMAL_INS a join ANIMAL_OUTS b on a.ANIMAL_ID = b.ANIMAL_ID
) */

#2. right outer join 활용하기
select  b.ANIMAL_ID, b.NAME
from ANIMAL_OUTS b
where b.ANIMAL_ID in(
select o.ANIMAL_ID
from ANIMAL_INS i right outer join ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID
where i.ANIMAL_ID is null #=null 말고 is null로 해야됨
    )
    