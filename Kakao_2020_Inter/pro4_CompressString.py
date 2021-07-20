# 문자열 압축


def solution(s):
    answer = 0




    def comress(s,n):
        a=[]
        size=len(s)
        i=0

        while i<size:
            k=s[i:n]
            a.append(k)
            i+=1
            n+=1

        print(a)

        # 만약 쪼개진 a가 뒤에랑 같다면 숫자 증가

        idx=1
        size=len(a)

        fi=a[0]

        new_ans=""
        j = 1
        while idx<size:

            if fi==a[idx]:
                j+=1

            else :

                fi = a[idx]

                if j>1:
                    k=str(j)+fi
                    new_ans+=k

                else :
                    new_ans+=a[idx]
                j=1


            idx+=1

        print(new_ans)



        return 0

    comress(s,1)




    # for i in range(len(s)):
    #     ans=comress(s,i)

        # if answer<ans:
        #     answer=ans


    return answer


solution("aabbaccc")