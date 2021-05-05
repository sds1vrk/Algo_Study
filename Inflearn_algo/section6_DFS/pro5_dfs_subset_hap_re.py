# 부분집합의 합 구하기
import sys
sys.stdin=open("input.txt","r")

n=int(input())
a=list(map(int,input().split()))
total=sum(a)

def dfs(l,hap):

    # 가지치기로 시간 더 줄이기
    if hap>(total//2):
        return

    # 인덱스가 0부터 시작하고 5번까지 다 사용하였기 때문에 6이 나오면 종료
    if l==n:
        # print("dfs 종료")
        if hap==(total-hap):
            print("YES")
            sys.exit(0)

    else :
        dfs(l+1,hap+a[l])
        dfs(l+1,hap)

dfs(0,0)
print("NO")



