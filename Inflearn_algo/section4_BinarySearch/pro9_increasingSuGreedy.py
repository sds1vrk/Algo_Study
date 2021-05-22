# 증가 수열 만들기
# 문제가 이해가 안됨
# 10
# 3 2 10 1 5 4 7 8 9 6이 답이 3 LRR이 되는지 모르겠음
# 이유는 3, 6, 9 ==>  L R R 이 됨

import sys
sys.stdin=open("input.txt","r")
n=int(input())
a=list(map(int,input().split()))

lt=0
rt=len(a)-1
last=0
temp=[]
while lt<=rt:
    if a[lt]>last:
        temp.append((a[lt],"L"))

    if a[rt]>last:
        temp.append((a[rt],"R"))






print(res)
