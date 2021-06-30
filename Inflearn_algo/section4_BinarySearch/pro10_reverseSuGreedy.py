# 역수열
# 현재 상황에서 최선의 경우 탐색
# 해결방법
# 0인 배열 만든 다음에, 1부터 집어 넣어 현 상황에서 최선의 경우 고르기

import sys
# sys.stdin=open("3190.txt","r")

n=int(input())
a=list(map(int,input().split()))
a.insert(0,0)


vv=[0]*n

for i in range(1,n+1):
    for j in range(n):
        if a[i]==0 and vv[j]==0:
            vv[j]=i
            break

        if vv[j]==0:
            a[i]-=1



# print("v",vv)

for x in vv:
    print(x,end=" ")









