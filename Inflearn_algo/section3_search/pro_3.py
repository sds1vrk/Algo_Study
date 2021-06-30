# 카드 역배치
# 문제 못품
# 구간별 역배치 구하는 문제
# 핵심은 구간 s+e+1
# 3,4,5,6 ==> 3,6 교환, 4,5 교환 ==> 2바퀴 돌면됨
# 회전 수는 ==> 6-3+1 // 2 몫으로 횟수 구함, 2로 나눈 몫인 이유는 반 만큼 회전 하기 위해서 나눔
# 짝수, 홀수 상관 없음
# 그리고 맨 처음과 맨 끝을 스왑




import sys
import math
# sys.stdin=open("3190.txt","r")
a=[i for i in range (1,21)]
# k=array[10-1:5-1-1:-1]
# print(k)
# print(array[:5-1:]+k+array[10::])

# print(array[:4])
# array[:n-1]

# print(array[10:])
# array[m+1:]

for i in range(10):
    m,n=map(int,input().split())
    k=(n-m+1)//2
    # print(k)
    for j in range(k):
        # print(a[m+j-1],a[n-1-j])
        a[m+j-1],a[n-1-j]=a[n-1-j],a[m+j-1]


for x in a:
    print(x, end=" ")

