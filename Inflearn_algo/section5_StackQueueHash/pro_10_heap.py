# 부모 노드가 자식노드보다 작다
# 사용방법은 import heapq as hq
# 리스트를 만들고 a=[]
# 값을 넣을때는 hq.push(a,n) # a라는 리스트에 n을 만들고 이를 heapq로 만든다
# 값을 뺄때는 hq.pop(a) # a라는 리스트에서 빼는데 이때 빼지는 값은 루트인 가장 작은 값이다.


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
            print(hq.heappop(a))

    else :
        # a라는 리스트에 n값을 넣어주면 알아서 heap 자료구조가 만들어줌
        hq.heappush(a,n)


