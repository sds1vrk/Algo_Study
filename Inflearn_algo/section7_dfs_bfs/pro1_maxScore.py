# 최대 점수 구하기 (DFS)
import sys
# sys.stdin=open("input.txt","r")
# 조합을 풀기
#
n,m=map(int,input().split())

ss=[]
tt=[]

for i in range(n):
    a,b=map(int,input().split())
    ss.append(a)
    tt.append(b)
res=[]
max_score=-1
def dfs(l,start,s,t):
    global max_score
    # 가지치기 t가 m을 넘으면 더이상 할 필요 없음
    if t>m:
        return

    if max_score<s:
        max_score=s

    # 이렇게 해버리면 순열임
    # for i in range(n):
    #     if ch[i+1]==0:
    #         ch[i+1]=1
    #         # print("si",s[i])
    #         dfs(l+1,s+ss[i],t+tt[i])
    #         ch[i+1]=0

    # 조합은 start부터 범위
    # start로부터 가지치기
    for i in range(start,n):
        dfs(l+1,i+1,s+ss[i],t+tt[i])

#level,start,score,time
dfs(0,0,0,0)

print(max_score)