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



# 해당 a에는 이제 정보가 다 쌓여 있다.
# 먼저 행과 열값 더하기
result=[]
for i in range(n):
    sum1=0
    sum2=0
    for j in range(n):
        # 행값 더하기
        sum1+=a[i][j]
        # 열값 더하기
        # 이게 가능한 이유는 j만 증가가 되니깐 이를 앞으로 빼는거임, 그러면 이미 만들어져있는 a에서 열만 증가 가능
        sum2+=a[j][i]

    result.append(sum1)
    result.append(sum2)


# 대각선 구하기
sum3=0
sum4=0
for i in range(n):
    sum3+=a[i][j]
    sum4+=a[i][n-i-1]

result.append(sum3)
result.append(sum4)

print(max(result))


