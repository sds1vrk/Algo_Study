# 최대 힙
# 부모 노드가 항상 크다
# 일반적으로 heap는 최소힙으로 구성
# 따라서 최대 힙은 값을 넣을때 음수처리하여 넣어주면 끝
# 구할려는 값을 구할때는 다시 -- +로(원래부호) 바꿔주면됨

import sys
import heapq as hq

# sys.stdin=open("input.txt","r")

a=[]

while True:
    n=int(input())

    if n==-1:
        break
    if n==0:
        # 아무것도 없을수도 있음
        if len(a)==0:
            print(-1)
        else :
            # 루트 노드를 빼준다
            print(-(hq.heappop(a)))

    else :
        # a라는 리스트에 n값을 넣어주면 알아서 heap 자료구조가 만들어줌
        hq.heappush(a,-n)



