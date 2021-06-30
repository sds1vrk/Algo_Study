# 파일 입출력, read text
# 약수 구하기
import sys
# sys.stdin=open("3190.txt","rt")
n,k=map(int,input().split())
# print(n,k)

# 1. 약수 찾기
array=[]
for i in range(1,n+1):
    if n%i==0:
        array.append(i)

# print(array)
# 2. k번쨰 수 고르기
# 만약 범위를 벗어난다면 -1

leng=len(array)

if leng<k or leng<=0:
    print("-1")
else :
    print(array[k-1])

# 프로그래밍 강의
# for ~else 를 사용, for ~else는 for문이 정상적으로 동작 후에 break에 걸리지 않으면 출력
# cnt=0
# for i in range(1,n+1):
#     if n%i==0:
#         cnt+=1
#
#     if cnt==k:
#         print(i)
#         break
# else :
#     print(-1)