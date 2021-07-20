# 뉴스 클러스터링

def solution(str1, str2):
    answer = 0

    ch1 = []
    ch2 = []

    n1=len(str1)
    n2=len(str2)


    # 1. 부분집합 구하기
    for i in range(0, n1-1):
        k = str1[i] + str1[i + 1]

        if k.isalpha():
            k=k.lower()
            ch1.append(k)


    for i in range(0, n2-1):
        k = str2[i] + str2[i + 1]

        if k.isalpha():
            k=k.lower()
            ch2.append(k)



    # 2. 전체 부분 집합의 리스트 구하기
    tList=set(ch1+ch2)

    # 2-1. 교집합 kList
    kList=[]
    # 2-2. 합집합 hList
    hList=[]

    print("tList",tList)

    for i in tList:
        t1=ch1.count(i)
        t2=ch2.count(i)

        # 둘다 공통된게 있으면 kList에 더해주기
        # 이떄 최소값만큼 반복하기
        if i in ch1 and i in ch2:
            if t1<=t2:
                for _ in range(t1):
                    kList.append(i)

            else :
                for _ in range(t2):
                    kList.append(i)

        # hList에 더해주기
        # 이떄 최대값만큼 반복하기
        if t1>=t2:
            for _ in range(t1):
                hList.append(i)

        else :
            for _ in range(t2):
                hList.append(i)



    print("kList",kList)
    print("hList",hList)


    # 교집합과 합집합 모두 0 인 것뿐만 아니라, 교집합은 0인데 합집합은 0이 아닐 때 역시 고려해주어야 합니다.
    if len(kList)==0 and len(hList)==0:
        answer = int(1 * 65536)

    elif len(kList)==0:
        answer=0

    else :
        answer=int(len(kList)/len(hList)*65536)

    print(answer)


    return answer


# solution("FRANCE","french")
# solution("handshake","shake hands")
solution("aa1+aa2","AAAA12")
# solution("E=M*C^2","e=m*c^2")
# solution("aaaa+bbb","aaa+bbbb")