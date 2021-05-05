# Subset 다시 구하기
# 주어진 숫자 3일때 나오는 부분집합의 수 구하기

n=int(input())

def dfs(l):
    if l==n+1:
        # DFS 종료
        for i in range(n+1):
            if ch[i]==1:
                print(i,end=" ")
        print()

    else :
        # dfs 증가
        ch[l]=1
        dfs(l+1)
        ch[l]=0
        dfs(l+1)

ch=[0]*(n+1)
dfs(1)