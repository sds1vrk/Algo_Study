import sys
sys.stdin=open("input.txt","r")


def dfs(v):
    # 종료지점에 오면
    if v==n+1:
        # ch로 체크된 인덱스만 출력
        for i in range(1,n+1):
            if ch[i]==1:
                print(i,end=" ")
        print()

        return

    else :
        # v이라는 원소를 사용하겠다.
        ch[v]=1
        dfs(v+1)
        # v이라는 원소 사용안함
        ch[v]=0
        dfs(v+1)


n=int(input())

ch=[0]*(n+1) # 원소 사용 하냐 안하냐
dfs(1)