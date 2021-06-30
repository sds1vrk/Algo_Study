# 랜선 자르기

# 결정 알고리즘으로 풀이
# 결정 알고리즘이란 이분탐색 알고리즘을 이용하여 범위를 좁혀 나가는 방법


import sys
# sys.stdin=open("3190.txt","r")


# K는 랜선의 , N: 필요한 랜선의 개수
k,n=map(int,input().split())
a=[]
for i in range(k):
    a.append(int(input()))

a.sort()
# 초기값은 가장 작은 1부터 ~ 가장 큰값의 중간값
# print(s,e)
# 이분 탐색은 lt와 rt 설정
lt=1
rt=a[-1]

def count(length):
    cnt=0
    for i in a:
        cnt+=i//length

    return cnt

res=0
# lt랑 rt가 같아질때까지 계속 반복
while lt<=rt:
    mid=(lt+rt)//2
    # print("mid", mid)

    # N이상보다 더 많이 만들떄까지
    if count(mid)>=n:
        res=mid
        # print("res",res)
        # 최대값을 구하기 위해 lt 값 늘리기
        lt=mid+1

    else :
        rt=mid-1

print(res)




