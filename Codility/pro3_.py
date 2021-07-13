def solution(A):
    # write your code in Python 3.6
    # pass
    # a_set=set(A)
    # print(a_set)

    data=dict()
    n=len(A)

    s=0
    e=0

    max_value=2
    while s<n:
        if len(data)<3:
            s+=1
            data[A[s]]=s
            # s+=1

        if len(data)==3:
            mina_value=min(data.keys(),key=(lambda  k:data[k]))
            data.pop(mina_value)
            s+=1

        max_value=max(max_value,e-s)

    return max_value






solution([4,2,2,4,2])