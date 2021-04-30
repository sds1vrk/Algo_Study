# 휴가 가기전에 일 최대한 많이 하기
import sys
sys.stdin=open("input.txt","r")

n=int(input())
time=[]
score=[]

for i in range(n):
    a,b=map(int,input().split())

    time.append(a)
    score.append(b)
max_score=-1
# time과 score에 0을 추가, l과 맞춰주기 위해서
time.insert(0,0)
score.insert(0,0)

print(time)
print(score)
# l은 진행되고 있는 날짜
def dfs(l,t,s):
    global max_score
    if t>n:
        return


    # 이렇게 냅두면 멈추질 않음
    # 종료 조건을 더 넣어줘야 함
    if l==n+1:
        if max_score<s:
            max_score=s

    else :
        # 일한다
        # 만약 현재 날짜 + 상담을 진행할 날짜
        # l+time[l] <=n+1 안에 들어가 있어야지 다음날 상담이 가능
        if l+time[l]<=n+1:
            dfs(l+time[l],t+time[l],s+score[l])
        # 일하지 않는다
        dfs(l+1,t,s)

dfs(1,0,0)

print(max_score)