import sys
# sys.stdin=open("retireDay.txt","r")

n=int(input())
days=[0]*(n+1)
profit=[0]*(n+1)


for i in range(1,n+1):
    d, p = map(int, input().split())
    days[i]=d
    profit[i]=p

# print(days)
# print(profit)

# DFS 그 날 일을 한다 안한다
# 인자는 l, 합 h
max_value=0
def dfs(l,h):
    global max_value
    # 종료 조건은 n+1 날 종료
    if l==n+1:
        if max_value<h:
            max_value=h

    elif l>n+1:
        return

    else :
        # 1일차에 일을 함 ==> 4일차로 감, 그 날까지 일이 가능
        if l+days[l]<=n+1:
            dfs(l+days[l],h+profit[l])

        # 그 날에 일을 안함
        dfs(l+1,h)

dfs(1,0)
print(max_value)



