# 피자 배달 거리
# 해결 방법
# 1. 맵을 확인하여 피자집이 있는 좌표(x,y) 좌표 구하기
# 2. 구한 좌표로 피자집을 m개를 선택하는 모든 경우의 수 구하기
# 3. 경우의 수를 하나씩 대입하여 현재 피자집부터~ 집까지의 거리 구하기
#   - 이떄 ch를 사용, ch는 2중 배열로 집과 피자집의 거리를 체크하기 위해 사용
# 4. 만약 집과 피자집보다 거리가 기존꺼보다 가깝다면 ch 집의 거리를 갱신하기
# 5. 피자집을 제외한 모든 집의 경우의 수중 가장 작은 것을 출력

import sys
from itertools import combinations
sys.stdin=open("input.txt","r")

n,m=map(int,input().split())

a=[list(map(int,input().split())) for _ in range(n)]

# print(a)

# 맵 확인하여 피자집 개수 확인
pizza_map=[]

for i in range(n):
    for j in range(n):
        if a[i][j]==2:
            pizza_map.append((i,j))

# print(pizza_map)

# 피자집 선택하기
pizz_list=list(combinations(pizza_map,m))
# print(pizz_list[0])


# 근처 피자집이 있으면 종료
# 피자 집이 있는 맵 선택 -> 15가지

def dfs(x,y):
    for i in range(n):
        for j in range(n):
            if a[i][j]==1 and ch[i][j]<=500:
                dis=abs(x-i)+abs(y-j)
                # ch[i][j]=1
                if dis<ch[i][j]:
                    ch[i][j]=dis

                # dfs(i,j)

def hap_list(ch):
    res=0
    for i in range(n):
        for j in range(n):
            if ch[i][j]!=500:
                res+=ch[i][j]
    return res

result=[]

# print("len",len(pizz_list))

for i in pizz_list:
    ch = [[500] * n for _ in range(n)]
    # 피자 집이 있는 곳은 2로 처리
    for x,y in i:
        print("x,y",x,y)
        # ch[x][y]=2

        # print("ch",ch)
        # 이 맵을 DFS에 넘겨줌
        dfs(x,y)

    # res=0

    res=hap_list(ch)

    result.append(res)

    print("ch",ch)
print(min(result))














