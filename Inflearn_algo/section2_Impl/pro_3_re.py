import sys
# sys.stdin=open("3190.txt","rt")
# 이 문제는 반례가 존재
# 가장 큰 수부터 더하게 되면 반례가 존재하기 때문에 3중 for문으로 전체 합을 다 계산 한 후에 이를 정렬
# 이떄 중복을 제거하기 위해서 set을 사용

# 반례는 54+52+46 > 54 + 53 + 40 큰 수 존재

n,k=map(int,input().split())
a=list(map(int,input().split()))
res=set()
a.sort(reverse=True)
# print("a",a)

for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            res.add(a[i]+a[j]+a[m])

res=list(res)
res.sort(reverse=True)
print(res[k-1])