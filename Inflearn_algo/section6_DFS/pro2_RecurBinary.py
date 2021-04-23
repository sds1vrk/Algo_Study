# 재귀함수를 이용한 이진수 출력
# 10진수 N이 입력되면 2진수로 변환하여 출력
import sys
sys.stdin=open("input.txt","r")
res=[]

def dfs(n):
    # dfs 종료 조건, 먼저 명시
    if n<1:
        return

    k=n%2
    n=n//2

    dfs(n)

    print(k,end="")



n=int(input())
dfs(n)

# print(res)