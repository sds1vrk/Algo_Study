# 뮤직비디오 (결정 알고리즘)
# M개 이하로 짜르기

import sys
sys.stdin=open("input.txt","r")

n,m=map(int,input().split())

a=list(map(int,input().split()))


# 결정 알고리즘, lt와 rt정하기
lt=1
rt=sum(a)
res=0

def count(mid):
    # cnt는 DVD의 저장은 일단 1개
    cnt=1
    # DVD에 저장되는 노래들의 합
    hap=0
    for i in a:
        hap+=i
        if hap>mid:
            # 용량이 초과되서 새로운 DVD가 필요
            cnt+=1
            # 그리고 첫번째 곡으로 i가 들어감
            hap=i


    return cnt



maxx=max(a)
while lt<=rt:
    # 자를수 있는 중간값 찾기
    mid=(lt+rt)//2

    # 만약 count함수에 들어가서 나온 값이 찾을려는 m값 이하이면 정답이 되기에 이것을 mid값에 넣고
    # 3개이하로 만들수 있으면 2,3개 가능하기에 이하로 넣는다.
    # 그리고 최소값을 찾기 위해서 rt값을 줄인다
    # rt값을 줄일수록 mid 값이 작아지기 떄문에

    # 추가적으로 mid>=maxx 를 해준 이유는 123456789 9 9 라고 했을경우 9분 보다 큰것은 따로 들어가야 되므로 mid>=maxx라는 조건을 써준다.
    # mid는 capcity
    if mid>=maxx and count(mid)<=m:
        res=mid
        rt=mid-1

    else :
        # 나온값이 4,5,6 이러면 lt를 늘려서 더 작게 만들어야 됨
        lt=mid+1

print(res)