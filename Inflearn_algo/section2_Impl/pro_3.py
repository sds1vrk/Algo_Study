# K 번쨰 큰수 구하기 (2)
import sys
sys.stdin=open("../section1/3190.txt", "rt")

n,k=map(int,input().split())
result=[]

array = list(map(int, input().split()))
array.sort(reverse=True)
print("역순 출력",array)

first=array[0]
result.append(first)
# 수 합치기, k-1까지만 // 구할려는 수 전까지만
for i in range(1,n):
    if first>array[i]:
        result.append(array[i])
        first=array[i]

    if len(result) == k - 1:
        break

# print(result)

# 마지막 인덱스 더하기
# 지금까지 구한 수의 마지막
su=result[len(result)-1]
final_index=array.index(su)

# 인덱스로 마지막 값이 무엇인지 찾기
final_value=array[final_index]
# print("fianl_index",final_index)
# print("fianl_value",final_value)
cnt=0
for i in range(final_index,n):
    if final_value>array[i]:
        cnt+=1
        final_value=array[i]

    if cnt == k:
        result.append(final_value)
        break

# print("result",result)
# print("sum",sum(result))
print(sum(result))











