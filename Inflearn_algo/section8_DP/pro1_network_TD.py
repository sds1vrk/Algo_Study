# Top down 방식 (재귀, 메모제이션)
# 메모제이션 : 기록해서 재사용 (다시 계산하지 않고)
import sys
sys.stdin=open("input.txt","r")
n=int(input())
dp=[0]*(n+1)


def dfs(n):

    # 사용했던것을 재사용 ==> 속도가 비약적으로 증가됨
    if dp[n]>0:
        return dp[n]

    # 종착점은 제일 짧은것
    if n==1 or n==2:
        return n

    else :
        dp[n]=dfs(n-1)+dfs(n-2)
        return dp[n]




print(dfs(n))

