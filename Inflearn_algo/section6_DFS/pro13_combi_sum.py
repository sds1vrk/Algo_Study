# combination 합 구하기

import sys
sys.stdin=open("input.txt","r")

# 5, 3
n,m=map(int,input().split())
a=list(map(int,input().split()))
k=int(input())

# 조합의 수가 들어있는 배열
ch=[0]*m
cnt=0
def dfs(l,s,hap):
    global cnt
    if l==m :
        # 반드시 밑에 써줘야 됨, 안써주면 인덱스 번호 초과됨
        # if문에 들어가서 else에 못들어가기 하기 위해서
        print(ch)

        if hap%k==0:
            cnt+=1

    else :
        for i in range(s,n):
            ch[l]=a[i]
            # 이렇게 해버리면 기존 합이랑 연관되어 버림
            # hap+=ch[l]
            # dfs(l+1,i+1,hap)
            dfs(l+1,i+1,hap+a[i])


dfs(0,0,0)
print(cnt)



# 조합의 수가 들어있는 배열
# ch=[0]*m
# cnt=0
# res=[]
# def dfs(l,s):
#     global cnt
#     if l==m :
#         hap=0
#         for i in ch:
#             hap+=i
#         res.append(hap)
#
#     else :
#         for i in range(s,n):
#             ch[l]=a[i]
#             dfs(l+1,i+1)
#
# dfs(0,0)
#
# for i in res:
#     if i%6==0:
#         cnt+=1
#
# print(cnt)