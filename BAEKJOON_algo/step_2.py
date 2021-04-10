# 백준2. If문


# a,b=map(int,input().split())
# if a>b:
#     print(">")
# elif a<b:
#     print("<")
# else :
#     print("==")

# a=int(input())
# if a>=90 and a<=100:
#     print("A")
#
# elif a>=80 and a<=89:
#     print("B")
#
# elif a>=70 and a<=79:
#     print("C")
#
# elif a>=60 and a<=69:
#     print("D")
# else :
#     print("F")

# 윤년 확인
# a=int(input())
#
# if a%4==0 and (a%100!=0 or a%400==0):
#     print("1")
# else :
#     print("0")

# 4분면 고르기
# a=int(input())
# b=int(input())
#
# if a>0 and b>0:
#     print("1")
#
# elif a<0 and b>0:
#     print("2")
#
# elif a<0 and b<0:
#     print("3")
#
# else :
#     print("4")


# 45분 전 알람 맞추기
a,b=map(int,input().split())

if a ==0:
    a = a + 24

if b<45:
    a=a-1
    b=60+b-45

else :
    if a==24:
        a=0
    b=b-45

print(a,b)

