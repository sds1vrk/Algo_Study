# 사과나무
# start과 end로 풀기
import sys
sys.stdin=open("input.txt","r")

n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]

print(a)

s=n//2
e=n//2
res=0
# print(s,e)
for i in range(n):
    for j in range(s,e+1):
        print(a[i][j],end=" ")
        res+=a[i][j]
    print()

    if i<n//2:
        s-=1
        e+=1
    else :
        s+=1
        e-=1

print(res)