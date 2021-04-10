# 해시 위장 문제
# 옷 고르는 문제
# dict로 구함

from itertools import combinations

def solution(clothes):

    # data=dict()

    # print(clothes)

    # print(data.get(clothes[0][1]))
    # if data.get(data[0][1]) is not:

    # data={"headgear":[],"eyewear":[]}
    #print(data)
    key_dict=[]
    value_dict=[]
    #data=dict()

    # 키값이 있는 빈 dict 만들기
    temp=[]
    for i in clothes:
        temp.append(i[1])

    print("temp",temp)
    print("set",set(temp),len(set(temp)))

    temp=list(set(temp))
    data={}
    strr=""
    for k in range(len(temp)):
        test={temp[k]:[]}
        print("test",test)
        data.update(test)

    print(data)

    for i in clothes:

        #print(i[1],i[0])
        data[i[1]].append(i[0])

    #my_dict = {"Name": [], "Address": [], "Age": []}
    #my_dict["Name"].append("Guru")


    print(data)


    # 키 갯수 세기
    data_key=data.keys()

    # 키 조합 경우의 수



    # print("array",array)




    # for i in range(1,len(data_key)+1):

        # for j in range(i,) :
        #     if data[]

    def NChooseK_fast(n, k):
        numerator = 1
        denominator = 1
        k = min(n - k, k)  # 조합의 대칭성을 이용하여 더 적은 수의 연산을 하기 위해서입니다.
        for i in range(1, k + 1):
            denominator *= i
            numerator *= n + 1 - i
        return int(numerator / denominator)


    print(NChooseK_fast(4,2))


    value=0
    for i in range(1,len(data_key)+1):
        count = NChooseK_fast(len(data_key), i)
        print("count",count)

        vv=0
        for key in range(count):

            # vv=len(data[key])
            # print("key",key,"len",vv)

            # vv+=vv

        value+=vv




    print(value)











        # answer = 0
    # return answer

solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])


