# 재귀함수를 이용한 이진수 출력
# 10진수 N이 입력되면 2진수로 변환하여 출력
# d(11) -> d(5) -> d(2) -> d(1) -> d(0)


import sys
sys.stdin=open("input.txt","r")
n=int(input())
def dfs(n):
    # 종료 조건 먼저 명시
    if n==0:
        return
    else :
        # DFS 호출하고 출력 (그래야지 최상단이 먼저 호출)
        dfs(n//2)
        print(n%2,end="")


dfs(n)