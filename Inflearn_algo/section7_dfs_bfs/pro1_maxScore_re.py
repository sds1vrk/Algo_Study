# 최대 점수 구하기 (DFS)
# 문제를 푼다, 안푼다라는 개념으로 가야됨
import sys
sys.stdin=open("input.txt","r")

n,m=map(int,input().split())

ss=[]
tt=[]

for i in range(n):
    a,b=map(int,input().split())
    ss.append(a)
    tt.append(b)
max_score=-1
def dfs(l,s,t):
    global max_score
    # 가지치기 t가 m을 넘으면 더이상 할 필요 없음
    if t>m:
        return

    if l==n:
        if s>max_score:
            max_score=s

    else :
        # 1번 문제를 푼다
        dfs(l+1,s+ss[l],t+tt[l])
        # 문제를 풀지 않는다
        dfs(l+1,s,t)


dfs(0,0,0)

print(max_score)