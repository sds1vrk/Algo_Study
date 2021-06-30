# 스도쿠 검사
# 합이 45인것으로 했는데 5번 케이스에서 반례 발생
# 1~9까지 합이 45, 그 외에도 9개의 합이 45인것이 존재
import sys
# sys.stdin=open("3190.txt","r")

a=[list(map(int,input().split()))for _ in range(9)]

# print(a)
n=len(a)
# print(n)
k=45

# 행열 검사
def hy(n):

    for i in range(n):
        # 행열검사
        sum1 = 0
        sum2 = 0
        for j in range(n):
            # 행 합
            sum1 = sum1 + a[i][j]

            # 열 합
            sum2 = sum2 + a[j][i]

        if sum1 != k or sum2 != k:
            # print("False")
            return False

    else :
        return True


def gcheck(s,e):
    # print("asdf")
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(s,e):

        for j in range(0,3):
            sum1+=a[i][j]

        for j in range(3,6):
            sum2+=a[i][j]
        for j in range(6,9):
            sum3+=a[i][j]

    # print(sum1, sum2, sum3,"k",k)

    if sum1 != k or sum2 != k or sum3 != k:
        # print("False")
        return False

    else :
        return True



pan=hy(n)
if pan:
    # 격자 검사, 3번 검사
    s,e=0,3

    for i in range(3):
        pan2=gcheck(s,e)
        # print("pan2",pan2)
        if not pan2:
            print("NO")
            break
        s+=3
        e+=3

    else :
        print("YES")



else :
    print("NO")


