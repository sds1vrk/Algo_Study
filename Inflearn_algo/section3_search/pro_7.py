# 사과나무 (다이아몬드)

# 격자판 최대합
# 문제 해결방법
# 2차원 리스트를 이용해서 리스트 만들기
# 방법은 2가지





import sys

# sys.stdin=open("3190.txt","r")

n=int(input())

# 리스트 만들기 1
# a=[]
# for i in range(n):
#     k=list(map(int,input().split()))
#     a.append(k)

# 리스트 만들기 2
a=[list(map(int,input().split())) for i in range(n)]
# print(a)

result=[]

# 몫으로 초기값 적기
s=n//2
e=n//2

sum = 0
for i in range(n):
    # print("i",i)
    for j in range(s,e+1):
        # print("j",j)
        sum+=a[i][j]

    # 감소
    if int(n//2)-1<i:
        s+=1
        e-=1
        # print(s,e)
    else :
        s -= 1
        e += 1

print(sum)







