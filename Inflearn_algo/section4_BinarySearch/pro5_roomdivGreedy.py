# 강의실 배정 문제
# 그리디 - 정렬 후 지금 상황에서 최적의 해를 구함
# 강의실을 먼저 끝내는 것이 최적의 해
# 따라서 강의 종료 시간에 따라 정렬

import sys
# sys.stdin=open("3190.txt","r")

n=int(input())

a=[]
for i in range(n):
    a.append(list(map(int,input().split())))


# 종료 시간에 따라 정렬
# key=lambda
sortA=sorted(a,key=lambda x:x[1])

# print(sortA)

# 현재 상황에서 최적의 해를 구함 ==> 그 해가 전체의 최적의 해
# 가장 먼저 끝나는것 제외
result=[]
temp=sortA[0]
result.append(temp)
for i in range(1,len(sortA)):
    if temp[1]<=sortA[i][0]:
        result.append(sortA[i])
        temp=sortA[i]

print(len(result))




