# compare sort
#입력 : [(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]
#출력 : [(1, -1), (1, 2), (2, 2), (3, 3), (0, 4)] 으로 정렬
# y좌표 오름차순, x좌표 오름 차순

data=[(0, 4), (1, 2), (1, -1), (2, 2), (3, 3)]

# 람다를 이용한 정렬 방법
sorted_a=sorted(data,key=lambda x:(x[1],x[0]))
print("sorted_a",sorted_a)

# compare을 이용한 정렬 방법
import functools

def compare(n1,n2):
    # return 1은 n1을 기준으로 오른쪽으로 이동
    # return 0은 그대로 둠
    # return -1은 왼쪽으로 이동
    if n1[1]>n2[1]:
        return 1

    elif n1[1]==n2[1]:

        if n1[0]>n2[0]:
            return 1

        elif n1[0]==n2[0]:
            return 0

        else :
            return -1

    else :
        return -1

result=sorted(data,key=functools.cmp_to_key(compare))
print("result",result)




