# DFS로 순열 구하기
import sys
sys.stdin=open("input.txt","r")

n,m=map(int,input().split())


def dfs(idx):


    if idx==m:
        # print("종료")
        # 종료할떄는 체크를 풀어줌
        for i in range(m):
            print(ch[i],end=" ")
        print()

    else :
        for i in range(1,n+1):
            # 중복된것은 뻗지 못하게 하면 됨
            # 해당 원소가 들어가있는 체크리스트 만든다
            if check[i]==0:
                check[i]=1
                ch[idx]=i
                dfs(idx+1)
                # check[i]=1로 만든후 되돌아옴
                check[i]=0

            # check[i]==0이기 때문에 자기자신은 dfs를 못타고 감
            # check[2]는 dfs가 가능하여 끝까지 나아감
            # return 온 후 check[1]=1이였던것을 check[1]=0으로 만들어주고 다음 for문을 돌음
            


ch=[0]*m
check=[0]*(n+1)
dfs(0)

