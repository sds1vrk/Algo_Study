# 바둑이를 승차할 수 있는 최대 무게 구하기
# 그리디로는 안됨 ==> 최대 무게이기 때문에 모든 경우의 수를 구해야 함, 최대 마리는 그리디로 가능

import sys
# sys.stdin=open("input.txt","r")

n,m=map(int,(input().split()))
a=[0]*(m)

for i in range(m):
    a[i]=int(input())

# print(a)

res=[]
def dfs(idx):
    # print(idx)
    if idx==m:
        hap=0
        for i in range(m+1):
            if ch[i]!=0:
                hap+=ch[i]
        if hap<=n:
            res.append(hap)
    else :
        ch[idx+1]=a[idx]
        dfs(idx+1)
        ch[idx + 1] = 0
        dfs(idx + 1)


ch=[0]*(m+1)
dfs(0)
print(max(res))

