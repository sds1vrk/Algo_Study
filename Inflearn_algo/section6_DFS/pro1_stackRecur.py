# 재귀함수와 스택
# 재귀함수는 반복문의 대체재 (for문 while문 등의 대체재)
# 재귀함수로 풀면 코드 유연성이 좋아짐

import sys
sys.stdin=open("input.txt","r")

def dfs(x):
    # 재귀함수 종료 조건
    if x>0:
        dfs(x-1)
        print(x,end="")


if __name__=="__main__":
    n=int(input())
    dfs(n)