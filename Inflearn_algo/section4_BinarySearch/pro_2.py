# 랜선 자르기 - 결정 알고리즘

import sys
sys.stdin=open("input.txt","r")


# K는 랜선의 , N: 필요한 랜선의 개수
k,n=map(int,input().split())
a=[]
for i in range(k):
    a.append(int(input()))

a.sort()
# print(a)
#  K개의 랜선 개수를 이용해서 ==> N개로 만들기, 이때 자를수 있는 최대 길이를 정수로 출력

# 내 생각
# 오름차순으로 하고 이 중에서 가장 작은 값을 뽑는다
# 가장 작은 값을 나눈 몫을 구하고 이 값을 cnt에 넣고 이 값의 합이 맞는지 확인한다.
# 틀리면 점차 줄여나가 최대값을 구한다.

# 1,2번이 틀림 이유는 가장 작은 값보다 더 작은 값이 답이 될 수 있기 때문임
# 따라서 가장 큰 값을 뽑는다

# 시간 초과 발생하기 떄문에 범위를 좁혀야 됨

max_length=a[-1]
while True:

    cnt=0

    for i in range(len(a)):
        if int(a[i]//max_length)>0:
            cnt+=int(a[i]//max_length)

    if cnt==n:
        break
    else :
        max_length-=1

print(max_length)




