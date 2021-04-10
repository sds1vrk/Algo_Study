# 다단계 문제
# enroll은 다단계에 Center를 제외하고 가입한 사람
# referral은 각 부모 노드를 가리킴
# seller는 물건을 판매한 사람, 이때 부모 노드에게 각 10%씩 전달해야함
# amount는 seller가 물건을 판매한 개수 *100을 해서 계산
# Return은 Center를 제외하고 트리에 연결된 이익금 구하기
def solution(enroll, referral, seller, amount):
    # 자식 노드
    print(enroll,len(enroll))
    # 부모 노드
    print(referral,len(referral))

    # 비용 계산
    costs=[0]*len(enroll)

    for i in range(len(enroll)):
        for j in range(len(seller)):
            if enroll[i]==seller[j]:
                costs[i]=amount[j]*100

    print(costs)

    # 부모 인덱스 찾기
    def find_parent(node):
        for i in range(len(enroll)):
            if node==enroll[i]:
                return i



    # 부모 노드가 있다면 값 갱신
    for i in range(len(enroll)):
        costs[i]=costs[i]*0.9

        # 부모가 있으면, 부모를 찾고 부모에게 돈 주기
        if referral[i]!="-":
           index=find_parent(referral[i])
           costs[index]=costs[index]+costs[i]*0.1


    print(costs)
    sum=0
    for i in costs:
        sum+=i
    print("sum",sum)


    answer = []
    return answer


solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 1])
# 출력은 Center를 제외하고 판매한 금액 출력