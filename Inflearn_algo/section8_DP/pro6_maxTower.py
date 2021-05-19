# 가장 높은 탑 쌓기
# 조건에 따라 가장 높은 탑 쌓기

# 조건
# 1. 밑면 넓이, 무게 또한 다르다
# 2. 높이는 같을 수 있다.
# 3. 밑에 밑면이 가장 크고 ==> 그 위는 작은것을 쌓는다
# 4. 무거운 벽돌을 먼저 쌓고 ==> 그 위는 무게가 작은것을쌓는다

# 주어진 조건은 밑면 넓이, 높이, 무게가 주어짐

# 출력은 가장 높이 쌓을 수 있는 탑의 높이 출력
# 넓이를 기준으로 내림차순 ==> 가장 넓이가 큰 것부터 차례로 뽑고 조건에 걸음
# DP에 들어갈 값은 높이

import sys
sys.stdin=open("input.txt","r")
n=int(input())
a=[]

for i in range(n):
    a.append((list(map(int,input().split()))))

a.sort(reverse=True)
print(a)
# 0번부터 시작하기 때문에 n까지만 한다

# dp에는 각 벽돌이 제일 위에 있을때 높이를 쌓는다.
dp=[0]*(n)
# 첫번째 쌓을수 있는 것은 첫번쨰 벽돌밖에 없기 때문에 고정적으로 들어감
dp[0]=a[0][1]
# S 25 16 9 4 1
# H 3  2  2 4 5
# W 4 5   3 6 2

for i in range(1,n):
    max_val=0
    for j in range(i-1,-1,-1):
        # 자기보다 무게가 큰 것만 들어갈 수 있음
        if a[i][2]<a[j][2] and max_val<dp[j]:
            max_val=dp[j]

    dp[i]=a[i][1]+max_val

print(max(dp))








