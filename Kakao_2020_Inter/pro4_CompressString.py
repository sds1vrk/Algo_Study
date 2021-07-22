# 문자열 압축


def solution(s):
    answer = len(s)




    def comress(s,n):
        a=[]
        size=len(s)
        i=0

        while i<size:
            k=s[i:i+n]
            a.append(k)
            i+=n
            # n+=1

        # print(a)

        # 만약 쪼개진 a가 뒤에랑 같다면 숫자 증가

        idx=1
        size=len(a)
        # print(size)

        fi=a[0]

        new_ans=""
        j = 1
        while idx<size:

            if fi==a[idx]:
                j+=1

                # 마지막 인덱스면 증가
                # if idx==size-1:
                #     k=str(j)+fi
                #     new_ans+=k

            else :


                if j>1:
                    k=str(j)+fi

                    new_ans+=k

                else :
                    new_ans+=fi

                fi = a[idx]
                j=1


            idx+=1


            # 마지막 인덱스면 증가
            if idx == size :

                if j>1:
                    k=str(j)+fi

                    new_ans+=k

                else :
                    new_ans+=fi

        # print(new_ans)


        return len(new_ans)



        # return 0

    # comress(s,1)
    # comress(s,2)
    # comress(s,8)
    # comress(s,4)




    for i in range(1,len(s)):
        ans=comress(s,i)
        if answer>ans:
            answer=ans
    # print(answer)
    # return answer


solution("aabbaccc")
# solution("ababcdcdababcdcd")
solution("abcabcabcabcdededededede")