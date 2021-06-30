# 점수 계산

import sys
# sys.stdin=open("3190.txt","rt")

n=int(input())

m=list(map(int,input().split()))

cnt=0
sum=0

def hap(cnt):
    hap=0
    print("cnt",cnt)
    for i in range(1,cnt+1):
        hap+=i
    # print(hap)
    return hap
# print(len(m))
# 이 코드는 마지막에 1이 안나오면 더이상 합칠수 없음
# for i in range(len(m)):
#     if m[i]==1:
#         cnt+=1
#
#     else :
#         if cnt==1:
#             print("here")
#             sum+=1
#         elif cnt>1:
#             sum+=hap(cnt)
#         cnt=0
# print(sum)

# 따라서 바로 바로 합쳐줘야함
for i in range(len(m)):
    if m[i]==1:
        cnt+=1
        sum+=cnt
    else :
        cnt=0

print(sum)