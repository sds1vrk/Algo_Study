# 수들의 합
# tot =a[0]
# lt ~ rt
# tot < m   tot+=rt값, 그리고 rt의 인덱스 증가
# tot = m   cnt+=1,     lt의 값을 인덱스 1증가 시켜서 이동 tot 값 변경
# tot > m ,  tot에서 lt 값을 빼주고, lt 인덱스 증가시키고 다음으로 이동

# 종료 시점
# rt는 다 돌고 n으로 가 있는다
# lt 만 이동하다가 값이 tot 값이 < m 이면 rt의 인덱스를 증가시켜야 되는데 rt=n이기 때문에 이때 break를 한다.
# if 마지막 인덱스가 tot > m 이라면, tot - lt 이기 때문에 tot는 0이 된다 따라서 다시 tot < m 으로 간다. 그리고 rt==m 이기 떄문에 break 에 이미 걸려 while 문 종료

import sys
sys.stdin=open("input.txt","r")
n,m=map(int,input().split())
a=list(map(int,input().split()))

lt=0
rt=1
tot=a[0]
cnt=0

while True:
    if tot<m :
        if rt<n:
            tot+=a[rt]
            rt+=1
        else :
            # rt == n
            break

    elif tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1

    else :
        tot-=a[lt]
        lt+=1

print(cnt)
