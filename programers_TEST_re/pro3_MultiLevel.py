# 다단계 문제

# 1. 주어진 매개변수 파악
# enroll - 총 등록되어 있는 판매처
# referral - 소개시켜준 판매처 (부모)
# seller - 실제 물건을 판 사람
# amount - seller의 판 갯수


def solution(enroll, referral, seller, amount):


    #2. Key, Value를 가진 HashMap 생성
    data=dict()
    for i in range(len(enroll)):
        if referral[i]=="-":
            data[enroll[i]]="center",0

        else :
            data[enroll[i]]=referral[i],0

    # print("data:",data)

    #4. 부모가 있는 경우 재귀적으로 호출하여 분배하기
    def distribute_parent(node,cash):
        # 부모에게 돈 주기
        # print("data_keys",data.keys())

        pan=node in data.keys()

        # print("부모가 있는지 판단",pan)

        # 자기자신이 판 금액의 0.9 돈 갖기
        if pan:
            current_money = data[node][1]
            total=cash
            parent_cash=int(total*0.1)
            my_cash=total-parent_cash

            # parent_cash = round(cash * 0.1)
            data[node] = data[node][0], current_money + my_cash
            parent_node=data[node][0]

            if parent_node!="center":
                distribute_parent(parent_node, parent_cash)

        else :
            return





    #3. 물건을 판매한 판매자에 대하여 for문
    for i in range(len(seller)):
        if seller[i] in data.keys():

            # 자기자신이 판 금액의 0.9 돈 갖기
            val = data[seller[i]][0]

            # 만약 부모가 있다면 0.9만 갖기
            # 돈 분배하기
            if val:
                current_money = data[seller[i]][1]

                total=amount[i] * 100
                parent_cash=int(total*0.1)
                my_cash=total-parent_cash

                # cash=int(amount[i] * 100*0.9)
                data[seller[i]] = val, current_money + my_cash
                # parent_cash = (amount[i]*100)-
                distribute_parent(val, parent_cash)

            # else :
            #     current_money = data[seller[i]][1]
            #     data[seller[i]] = val, current_money + (amount[i] * 100)




    # print(data)




    answer = []

    for i in data:
        answer.append(data[i][1])

    # print(answer)


    return answer

solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10])