# 퀵 정렬
# 전위 순위 방식 - 파티션(피봇을 기준으로 왼쪽으로 피봇보다 작은값, 오른쪽은 피봇보다 큰값으로 정렬)하고 분할
# 해당 퀵 소트에서는 피봇을 가장 마지막으로 잡음
# Pos는 피봇이 들어갈 곳


def Qsort(lt,rt):
    if lt<rt:
        # 파티션 작업
        pos=lt
        # 피봇값은 마지막 값
        pivot=arr[rt]

        # 파티션 작업 완료
        # 피보값을 중심으로 왼쪽은 피봇값보다 작은 값이, 오른족으로 피봇값보다 큰 값이 정렬 됨 (16줄~24줄)
        for i in range(lt,rt):
            if arr[i]<=pivot:
                #Swap
                arr[i],arr[pos]=arr[pos],arr[i]
                # 스왑 후 pos 증가
                # Pos는 마지막에 피봇이 들어갈 공간을 의미
                pos+=1
        # postion 값과 rt값(피봇값) 교환
        arr[pos], arr[rt] = arr[rt], arr[pos]

        # 분할
        Qsort(lt,pos-1)
        Qsort(pos+1,rt)












arr=[45,21,23,36,15,67,11,60,20,33]
print("Before Sort",end=" ")
print(arr)
Qsort(0,9)
print("After Sort",end=" ")
print(arr)