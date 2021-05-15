arr=[23,11,45,36,15,67,33,21]
# 후위 순위 방식
# 왼쪽 자식일과 오른쪽 자식의 일을 다 하고 나서 본연의 일을 진행

def Dsort(lt,rt):
    if lt<rt:
        mid=(lt+rt)//2
        Dsort(lt,mid)
        Dsort(mid+1,rt)
        # 정렬된것 합치기
        p1=lt
        p2=mid+1
        tmp=[]
        while p1<=mid and p2<=rt:
            if arr[p1]<arr[p2]:
                tmp.append(arr[p1])
                p1+=1

            else :
                tmp.append(arr[p2])
                p2+=1

        # p1에 값이 남아 있는 경우 (p2에 있는것디 다 채워져서 더이상 while문이 안돌음)
        if p1<=mid:
            tmp=tmp+arr[p1:mid+1]

        # p2에 값이 남아 있는 경우
        if p2<=rt:
            tmp=tmp+arr[p2:rt+1]

        # arr에 넣기
        for i in range(len(tmp)) :
            arr[lt+i]=tmp[i]




print("before sort: ",end=" ")
print(arr)
Dsort(0,7)
print()
print("After sort: ",end=" ")
print(arr)
