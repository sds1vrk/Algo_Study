# 증가 수열 만들기
# 문제가 이해가 안됨
# 10
# 3 2 10 1 5 4 7 8 9 6이 답이 3 LRR이 되는지 모르겠음 ==> 둘 다 선택하고 정렬 ==> 둘중 작은것을 last로 사용
# 이유는 3, 6, 9 ==>  L R R 이 됨

import sys
# sys.stdin=open("input.txt","r")
n=int(input())
a=list(map(int,input().split()))

lt=0
rt=len(a)-1
last=0
temp=[]
result=""
# 여기서 or 조건이 들어가기 때문에 L이랑 R을 비교해야됨
while lt<=rt:
    if a[lt]>last:
        temp.append((a[lt],"L"))
        # lt+=1

    if a[rt]>last:
        temp.append((a[rt],"R"))
        # rt-=1

    # temp에 들어갈수 있는게 아무것도 없으면 last가 가장 큰 값이 되므로 종료
    if len(temp)==0:
        break

    # temp를 비교하여 LR 둘중 작은것을 먼저 써야됨
    temp.sort()
    # 제일 작은 것은 result에 넣는다
    result+=temp[0][1]
    if temp[0][1]=="L":
        lt+=1

    if temp[0][1]=="R":
        rt-=1

    last=temp[0][0]
    temp.clear()

print(len(result))
print(result)
