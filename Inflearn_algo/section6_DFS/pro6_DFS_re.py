# 답은 맞았는데 시간 초과 따라서 강의
import sys
from collections import deque

# sys.stdin=open("input.txt","r")
n,m=map(int,(input().split()))
res = -2147000000000000

def dfs(idx,sum,tsum):
    # print("dfs")
    # 종료 조건
    global res

    # 현재까지의 합 + (total-tsum) 앞으로 밑에까지의 합이 ==> res보다 작으면 더이상 밑으로 갈 필요 없음
    if sum+(total-tsum)<res:
        return

    if sum>n:
        return

    if idx==m:
        if sum>res:
            res=sum

    else :
        # 하나는 자기 자신을 더한것, tsum은 무조건 자기자신을 더한값 ==> 이것을 이용해서 앞으로 밑에서 더할것을 커트시킬수 있음
        dfs(idx+1,sum+a[idx],tsum+a[idx])
        # 하나는 자기 자신을 포함하지 않는것
        dfs(idx+1,sum,tsum+a[idx])


a = [0] * (m)

for i in range(m):
    a[i]=int(input())
# idx, sum, tsum : 부분집합에 자기자신을 무조건 더한 것
total=sum(a)


dfs(0,0,0)
print(res)