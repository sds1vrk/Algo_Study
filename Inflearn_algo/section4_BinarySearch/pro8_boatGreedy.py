# 구명보트 최소 개수

import sys
# sys.stdin=open("3190.txt","r")



n,m=map(int,input().split())
res=0
a=list(map(int,input().split()))

# 오름 차순 정렬
# 맨 마지막꺼 먼저 꺼내고, 제일 크니깐 여기다가 더 큰게 있으면 제일 작은거 합치고 없으면skip
a.sort()
# print(a)

while a:
    k=a.pop()
    # 만약 a가 있으면 뺌, 이 조건을 안하면 인덱스 오류 생김
    if a and k+a[0]<=m:
        a.pop(0)

    res+=1

print(res)