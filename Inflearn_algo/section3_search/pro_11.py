# 격자판 회문수

import sys
# sys.stdin=open("3190.txt","r")

# 문자로 저장
a=[list((input().split())) for _ in range(7)]
# print(a)


result=[]

# su1=[]
# su2=[]
# for i in range(7):
#     for j in range(3):
#         kk=a[i]
#         o=''.join(kk[0+j:5+j])
#         h=o[::-1]
#         print(o,h)
#
#         if o==h:
#             su1.append(o)
#
#         # kkk=a[i][0]


# 행 부분
for i in range(7):

    for j in range(3):
        su1 = ""
        su2 = ""
        # su1+=a[i][j]+a[i][j+1]

        for k in range(5):
            su1+=a[i][j+k]
            su2+=a[j+k][i]

        # print("su1",su1)

        hsu1=su1[::-1]
        hsu2=su2[::-1]

        # print(hsu1)

        if su1==hsu1:
            result.append(su1)

        if su2==hsu2:
            result.append(su2)


# 열 부분
# for i in range(7):
#
#     for j in range(3):
#         su2 = ""
#
#         for k in range(5):
#             su2+=a[j+k][i]
#
#         print("su1",su2)
#
#         hsu2=su2[::-1]
#
#         print(hsu2)
#
#         if su2==hsu2:
#             result.append(su2)

print(len(result))