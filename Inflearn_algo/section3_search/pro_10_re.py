# 스도쿠 검사
# 합이 45인것으로 했는데 5번 케이스에서 반례 발생
# 1~9까지 합이 45, 그 외에도 9개의 합이 45인것이 존재
# 반례 2 4 3 6 2 8 5 7 8
import sys
# sys.stdin=open("3190.txt","r")

a=[list(map(int,input().split()))for _ in range(9)]

# print(a)
n=len(a)
# print(n)
k=45
kk=[i for i in range(1,10)]
# print(kk)

# 행열 검사
def hy(n):

    for i in range(n):
        # 행열검사
        # sum1 = 0
        # sum2 = 0
        for j in range(n):
            # 행 합
            # sum1 = sum1 + a[i][j]

            if a[i][j] in kk:
                kk.remove(a[i][j])

            if a[j][i] in kk:
                kk.remove(a[j][i])

        if len(kk) >=1:
            # print("False")
            return False

    else :
        return True


def gcheck(s,e,kk):
    # print("asdf")
    # sum1 = 0
    # sum2 = 0
    # sum3 = 0


    # print("s,e", s, e)
    ss, ee = 0, 3

    for _ in range(3):
        kk = [i for i in range(1, 10)]
        # 한칸 지우기
        for i in range(s, e):
            # print("ss,ee", ss, ee)
            for j in range(ss, ee):

                # 만약 지울려는 수가 있으면 지우고

                # print(a[i][j])
                if a[i][j] in kk:
                    kk.remove(a[i][j])

                # 지울라는 수가 없으면 False
                else :
                    return False

        # if ss==6 and ee==9:
        #     break

        # print("kk", kk)

        if len(kk) >= 1:
            return False

        ss += 3
        ee += 3


    else :
        # print("test")
        return True



pan=hy(n)
if pan:
    # 격자 검사, 3번 검사
    s,e=0,3

    for i in range(3):


        pan2=gcheck(s,e,kk)
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


