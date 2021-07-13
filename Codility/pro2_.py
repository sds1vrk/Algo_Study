#

def solution(S,C):

    email_list=[]

    a=S.split(";")

    def makeEmail(last,first):
        # 첫짜리 소문자로 변경
        # first=first[0].lower()+first[1:]
        first=first.lower()

        # print(first)
        # last=last[0].lower()+last[1:]
        last=last.lower()
        # print(last)

        ema=first+"_"+last+"@"+C.lower()+".com"
        # print(ema)

        email_list.append(ema)

        cnt=email_list.count(ema)

        if cnt==1:
            return "<"+ema+">"

        else :
            ema=first+"_"+last+str(cnt)+"@"+C.lower()+".com"
            return "<"+ema+">"


    # print(a[0])
    ans=""

    for i in a:
        data=i.split()
        # print(data)
        size=len(data)-1


        # print(data[size])

        if "-" in data[size]:
            data[size]=data[size].replace("-","")

        # print(data[size])

        ans+=i+" "+makeEmail(data[0],data[size])+";"



        # size=len(data)


    # ans[-1]="."
    # ans[len(ans)-1]="."
    # print(ans[-1])

    ans=ans[:-1]
    print(ans)

    # print(makeEmail("Jone","Doe"))
    # print(makeEmail("Jone","Doe"))
    # print(makeEmail("Jone", "Doe"))


    return ans




solution("John Doe; Peter Benjamin Parker; Mary Jane Watson-Parker; John Elvis Doe; John Evan Doe; Jane Doe; Peter Brian Parker","Example")