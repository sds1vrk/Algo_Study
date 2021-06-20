# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    ans = ""
    while N >= 1:
        k = N % 2
        ans += str(k)
        N //= 2

    # print(ans[::-1])
    ans=ans[::-1]

    max_len=0
    a=1
    b=0
    # print(len(ans))
    for i in range(1,len(ans)):
        if ans[i]=="1":

            b=i+1

            if abs(b-a)>max_len:
                max_len=abs(b-a)-1
                a=b+1

            a=b





            # if a==0:
            #     a=i+1
            # else :
            #     b=i
            #
            #
            #     if abs(b-a)>max_len:
            #         max_len=b-a
            #         a=b



    return max_len


# print(solution(561892),3)
#
# print(solution(74901729),4)
#
# print(solution(1376796946),5)

# print(solution(1041)

# print(solution(15))