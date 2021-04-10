# 백준1. 입출력과 사친연산


# 파이썬 그대로 출력 print(""" """)
# 이 문제는 이스케이프 없애기 위해 \를 추가
# print("\    /\\")
# print(" )  ( ')")
# print("(  /  )")
# print(" \(__)|")

# print("|\_/|")
# print("|q p|   /}")
# print('( 0 )"""\\')
# print('|"^"'"`    |")
# print('||_/=\\\__|')

# A+B 출력
# 방법 1
# value=list(map(int,input().split()))
# sum=0
# for i in value:
#     sum+=i
# print(sum)
# 방법 2
# a,b=map(int,input().split())
# print(a+b)


# a,b=map(int,input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# //는 몫
# print(a//b)
# %는 나머지
# print(a%b)


# a,b,c=map(int,input().split())
# print((a+b)%c)
# print(((a%c) + (b%c))%c)
# print((a*b)%c)
# print(((a%c)*(b%c))%c)

a=int(input())
b=input()

print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b))

