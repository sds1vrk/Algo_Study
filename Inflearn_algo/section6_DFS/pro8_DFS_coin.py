# 동전 교환
import sys
# sys.stdin=open("3190.txt","r")

n=int(input())
a=list(map(int,input().split()))
m=int(input())

res=[]
min=99999999999999999999

def dfs(idx,m):
    # print("dfs")
    # print(idx,m)
    global min

    if idx>min:
        return

    if m<0:
        return

    if m==0:
        # print("here")
        # res.append(idx)
        if idx<min:
            min=idx
        return

    elif m>0 :
        for i in range(n):
            dfs(idx+1,m-a[i])

# m=[0]*(m+1)
dfs(0,m)
print(min)
# print(min(res))