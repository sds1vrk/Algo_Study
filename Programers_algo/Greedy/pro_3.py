# 큰수 만들기



def solution(number, k):

    # print(number[:-k])

    max_value=number[:-k]
    na_value=number[k+1:]
    print(na_value)
    aa=max(max_value)
    # print(aa)
    array=[max_value, na_value]
    print(array)

    new_array=[]
    k=0
    for i in range(len(max_value)):
       # if i<=aa:
       #     k+=1
        if max_value[i]==aa:
            k=i
            break

    print("k:",k)

    max_value=max_value[k:]
    print("max:",max_value)
    bb=max_value+na_value
    print(bb)

    # k를 제외한 뒤 자리 2개를 빼고




    # for i in max_value:
    #     if i<aa:


    answer = ''
    return answer



# solution("1924",2)

solution("1231234",3)