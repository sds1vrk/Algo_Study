# 진법 변환




def solution(n, t, m, p):


    i=0
    answer = ''

    # def check(k):
    #     ans=""
    #     while k>=1:
    #
    #         if n>10:
    #
    #
    #
    #         ans+=str(k%n)
    #         k//=n
    #
    #     ans=ans[::-1]
    #
    #     print(ans)

    # def convert(k):
    #     T = "0123456789ABCDEF"
    #     q, r = divmod(n, base)
    #     if q == 0:
    #         return T[r]
    #     else:
    #         return convert(q, base) + T[r]


    # check(13)

    def convert(num, base):
        assert base > 1 and base < 17
        digits = "0123456789ABCDEF"
        s = []
        while num > 0:
            s.append(digits[num % base])
            num = num // base
        return "".join(s[::-1])


    # convert(print(254, 16)
    k=convert(255,16)
    print("k:",k)






    i=1
    m1=0


    while True:

        if len(answer)==t:
            break

        # k=check(i)
        k_len=len(k)

        a=0
        while a<k_len:
            m1+=1

            if m1==p:
                answer+=str(k[a])


            if m1==m:
                m1=0

            a += 1


        i+=1



    print(answer)
    return answer


solution(12,4,2,1)