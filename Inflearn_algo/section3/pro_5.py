# 수들의 합
import sys
# sys.stdin=open("input.txt","r")

# 시간 초과 발생하여 강의 보고 진행

n,m=map(int,input().split())

a=list(map(int,input().split()))

result=0
for i in range(n):
    sum=a[i]
    for j in range(i+1,n):

        if sum==m:
            result+=1
            break
        elif sum<m:
            sum = sum + a[j]

            # 여기 중요!!!
            # 반드시 더하고 나서 값을 확인하는 것이 필요


            if sum==m:
                result+=1
                break

        else :
            break
print(result)