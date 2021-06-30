# enumrate를 활용해서 대푯값 구하기
# 최소값 이용

import sys
sys.stdin=open("../section1/3190.txt", "rt")

n=int(input())

# 파이썬의 round는 even_round 방식이라 정확한 반올림은 원래수에서 0.5를 더한 후에 int로 치환해서 사용
array=list(map(int,input().split()))
value=sum(array)/len(array)+0.5
avr=int(value)
# avr=round(sum(array)/len(array))

# 최소값 구하기
# 최소값은 가장 큰 값을 초기값으로 잡는다
min=float("inf")
res=0
for i,x in enumerate(array):
    tmp=abs(x-avr)
    if tmp<min:
        min=tmp
        res=i+1
        score=x
    # 나중에 들어온 점수가 더 크다면 index+1
    elif tmp==min:
        if x>score:
            score=x
            res=i+1

print(avr,res)

