# Coin 문제 DP로 푸는 방법
import sys
sys.stdin=open("input.txt","r")

n=int(input())
a=list(map(int,input().split()))
m=int(input())


# 메모제이션
# 동전의 종류 만큼 메모제이션 만들기
# D(5) 이런것을 재사용 하기 위해서 사용
d=[1000001]*(m+1)
d[0]=0
for i in range(n):
    for j in range(a[i],m+1):
        # print(j-a[i])
        if d[j-a[i]]!=1000001:
            print(d[j],d[j-a[i]]+1)
            d[j]=min(d[j],d[j-a[i]]+1)
            print(j,d[j])

if d[m]==1000001:
    print(-1)
else :
    print(d[m])