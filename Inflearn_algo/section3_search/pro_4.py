# 두 리스트 합치기
import sys
# sys.stdin=open("3190.txt","r")

n=int(input())
n_a=list(map(int,input().split()))


m=int(input())
m_a=list(map(int,input().split()))

result=n_a+m_a
result.sort()

for i in result:
    print(i,end=" ")