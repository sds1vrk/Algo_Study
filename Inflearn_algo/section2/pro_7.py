# 에라토스테네스의 체
# n까지 소수 구하기
# 소수의 개수가 많을떄 가장 빨리 구할수 있음
# n제곱근까지만 이용하여 소수 판별
import sys
import math
sys.stdin=open("input.txt","r")
n=int(input())

# 소수의 개수를 출력
# 에라토스테네스의 체는 메모리를 이용하여 할당
# 자기 자신을 제외한 모든 수를 지우기
# 이때 핵심은 i는 제곱근까지 한다. 이유는 어차피 i*j가 n이 나오기 때문에 i의 범위를 제곱근까지 하여 줄여준다.
a=[0]*(n+1)
for i in range(2,int(math.sqrt(n))):
    j=2
    while i*j<=n:
        a[i*j]=1
        j+=1
cnt=0
for i in range(2,n):
    if a[i]==0:
        print("i",i)
        cnt+=1

print(cnt)
# 방법 2
cnt=0
for i in range(2,n+1):
    if a[i]==0:
        cnt+=1
        for j in range(i,n+1,i):
            a[j]=1

            