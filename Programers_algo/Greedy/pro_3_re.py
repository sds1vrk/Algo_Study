# 큰수 만들기


def solution(number, k):

    # print(number[:-2])
    # print(number[2:])

    prime=0
    while True:

        if prime==k:
            break
        # jj=-k+prime+1
        # print("jj",jj)
        # -2+0+1 -1의 그 전은
        print("k-prime",k-prime)
        max_value=number[:k-prime]
        print("max_val",max_value)
        aa=max(max_value)
        na_value=number[k-prime:]
        print("na_value",na_value)

        num=0
        for i in range(len(max_value)):
            if max_value[i]==aa:
                num=i+1

                print("num",num)
                break

        prime=prime+num

        number=max_value[prime:]+na_value
        print("change number",number,"prime",prime)

    print("number"+number)

solution("1924",2)
# solution("1231234", 3)