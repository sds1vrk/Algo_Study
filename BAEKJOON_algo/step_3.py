# 백준3. for문


#1. 99단
# a=int(input())
# for i in range(1,10):
#     print(a,"*",i,"=",a*i)

#2. n=int(input())
#
# array=[]
# for i in range(n):
#     a,b=map(int,input().split())
#     array.append(a+b)
#
#
# for i in array:
#     print(i)

#3. import sys를 이용한 방법
# import sys
#
# n=int(input())
# data=[sys.stdin.readline().rstrip() for i in range(n)]
#
# for i in range(len(data)):
#     i,j=map(int,data[i].split())
#     print(i+j)

# 방법 2 ==> 이건 무제한으로 입력받는 방법
# import sys
# T=int(input())
# for line in sys.stdin:
#     print(sum(map(int,line.split())))


# 3. 역순 출력
# n=int(input())
#
# for i in range(n,0,-1):
#     print(i)


# 정해진 숫자만큼 빠르게처리
# %d를 활용하여 문자열하고 숫자 합치기
# import sys
# t=int(input())
# for i in range(t):
#     print("Case #%d:"%(i+1),sum(map(int,sys.stdin.readline().split())))



n=int(input())

for i in range(n):
    a,b=map(int,input().split())
    c=a+b
    print("Case #%d: %d + %d = %d"%(i+1,a,b,c))


# 별찍기
# n=int(input())
#
# for i in range(1,n+1):
#     print(" "*(n-i)+"*"*i)


# n,m=map(int,input().split())
# k=list(map(int,input().split()))
# # print(k)
# for i in range(len(k)):
#     if m>k[i]:
#         print(k[i],end=' ')


