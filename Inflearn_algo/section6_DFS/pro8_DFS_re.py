# 동전 교환
import sys
# sys.stdin=open("input.txt","r")

n=int(input())
a=list(map(int,input().split()))
# 제일 큰것부터 없애기 위해 내림차순으로
a.sort(reverse=True)
m=int(input())

res=[]
min=99999999999999999999


def dfs(i,sum):
    global min

    # 가지 커트하는게 중요
    # 이것은 이미 나온값을 더 파지 않기 위해 사용
    # min을 앞에서 이미 구했는데 더 팔 필요가 없음
    if i>min:
        return

    if sum>m:
        return

    if sum==m:
        if i<min:
            min=i
        return

    else :
        for j in range(n):
            dfs(i+1,sum+a[j])

dfs(0,0)
print(min)