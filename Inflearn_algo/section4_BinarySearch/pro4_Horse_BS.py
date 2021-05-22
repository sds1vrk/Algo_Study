# 마굿간에 말 배치

# 말의 최단거리를 이분탐색으로 가정하고 푼다
# 말의 최단거리를 이분탐색으로 구하고 이 값을 입력하였을때 만약 이 값이 말 사이에 최단거리안에 있으면 cnt 증가

# cnt의 return 값이 3마리보다 더 많이 넣을수 있으면 당연히 3도 되므로 >=m으로 한다

import sys
sys.stdin=open("input.txt","r")

n,m=map(int,input().split())
a=[]
for i in range(n):
   a.append(int(input()))

a.sort()
# print("a",a)

# lt, rt는 거리
lt=1
rt=a[-1]

def count(length):
    # 첫번째 말
    # 첫번쨰 마굿간에 첫번째 말을 배치한다.
    # 말 사이의 최대 거리를 구해야 되므로 첫번쨰 수가 기준이 된다.

    cnt = 1
    ep = a[0]

    for i in range(1,len(a)):
        # 두 말 사이에 차이가 lenght보다 크거나 같으면 배치 가능 (length를 최단거리라고 설정하였기 때문에)
        if a[i]-ep>=length:
            cnt+=1
            # 이쪽이 가능하면 두번째 말을 배치하고 ep를 바꿔준다
            ep=a[i]

    return cnt


res=0
while lt<=rt:
    # 여기에서 mid는 말 사이에 최단거리라고 가정, 구할려는 값임
    mid=(lt+rt)//2


    # print("mid",mid)

    # 3마리보다 더많이 넣을수 있으므로, 3마리 4마리 넣으수 잇으면 3마리는 당연히 들어가는거임
    # print("cnt",count(mid))

    if count(mid)>=m:
        res=mid
        # 최대 거리 구하기 위해서 lt=mid+1
        lt=mid+1
        # print("lt",lt)
    else :
        rt=mid-1

print(res)




