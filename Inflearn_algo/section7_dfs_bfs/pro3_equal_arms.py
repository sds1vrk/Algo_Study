# 양팔 저울 문제 (DFS)
# 세방향 가지치기
# 추를 왼쪽에 놓느다 (+), 가운데에 놓는다 (-), 오른쪽에 놓는다 (사용하지 않는다)

import sys
# sys.stdin=open("input.txt","r")
def dfs(l,sum):
    global res

    if l==n:
        # 범위는 0보다 크고, 최대값보다 미만
        if 0<sum:
            sum=abs(sum)
            res.add(sum)


    else :
        dfs(l+1,sum+g[l])
        dfs(l+1,sum-g[l])
        dfs(l+1,sum)


n=int(input())
g=list(map(int,input().split()))
s=sum(g)
# 중복제거하기 위해서
res=set()
dfs(0,0)

print(s-len(res))