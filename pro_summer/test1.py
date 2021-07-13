def solution(code, day, data):

    # print(data)
    val=dict()
    result=[]
    # print("code",code)
    # print("day",day)

    for i in range(len(data)):
        k=data[i]
        # k.split("code")
        idx=k.find("code")
        cc=k[idx+5:idx+12].rstrip()
        # print("cc",cc)


        idx2=k.find("price")
        # print("idx2",idx2)
        pp=k[idx2+6:idx-1].rstrip()
        # print("pp",pp)

        time=k[idx+17:]
        tt=k[idx+17:idx+25]

        # print("tt",tt)

        # val[cc]=pp,tt

        if cc==code and day==tt:
            kk=int(pp),int(time)
            result.append(kk)

    data = sorted(result, key=lambda x: (x[1]))

    # print("data",data)
    answer=[]
    for i in data:
        answer.append(i[0])

    # print(answer)

    # answer=list(map(int,result))
    # print(answer)





    return answer

solution("012345","20190620",["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"])