# 랜선 자르기
import sys
# sys.stdin=open("input.txt","r")
n,m=map(int,input().split())
a=[]
for i in range(n):
   a.append(int(input()))


start=1
end=max(a)
# print(end)
answer=0

while start<=end:
    mid=(start+end)//2
    sum=0
    for i in a:
        k=i//mid
        sum+=k

    if sum>=m:
        answer=mid
        start=mid+1

    else :
        end=mid-1

print(answer)