# 다익스트라
# 시작정점부터 시작해서 최단거리로 모든 경로를 잇는 방법
# cf : 크루스칼은 모든 섬을 연결하는 방법이라는 점이 차이

# 길이는 3을 넘으면 안됨

import heapq as hq
def solution(n,road,k):


    # 다익스트라 적용하기
    def dijkstra(start):
        # 최단 거리를 구하기 위해 heap에 저장하기
        h=[]
        # 첫번쨰 정점은 0으로 초기화
        distance[start]=0

        # 힙에 저장할때는 (거리, 노드)로 저장하기
        hq.heappush(h,(0,start))

        while h:
            # 힙에서 제일 비용이 작은거 뽑기
            current_distance,current_node=hq.heappop(h)

            # 만약 현재 뽑은 노드의 거리가 기존 거리보다 크다면 더 볼 필요 없기 때문에 continue
            if distance[current_node]<current_distance:
                continue

            # 만약 그렇지 않다면 노드에 인접한 노드와 거리 찾기
            for adj_node, adj_dis in g[current_node]:
                # print("adj_node",adj_node)
                new_distance=current_distance+adj_dis

                # 만약 인접한 정점을 지난 거리가, 현재 거리보다 더 가깝다면 인접한 노드로 가는 거리 갱신하기
                if new_distance<distance[adj_node]:
                    distance[adj_node]=new_distance
                    # 그리고 힙에 저장하기
                    # 힙에 새로운 거리와 인접한 노드 저장하기
                    hq.heappush(h,(new_distance,adj_node))


    # 그래프 그리기 (인접행렬)
    # 0번 노드는 제외하기 때문에 1추가하기
    g=[[] for _ in range(n+1)]

    # 시작정점부터 시작해서 ~ end 정점까지 연결했을때 나오는 거리
    for s,e,v in road:
        g[s].append((e,v))
        # 무방향 그래프이기 때문에 반드시 해주기
        g[e].append((s,v))
    # print(g)

    # 거리를 저장하기 위해 거리 초기화하기, 이때 거리는 무한대값으로 저장
    INF = float("inf")
    distance=[INF]*(n+1)
    # print(distance)

    dijkstra(1)
    # print(distance)
    cnt=0
    for i in range(1,len(distance)):
        if distance[i]<=k:
            cnt+=1

    print(cnt)













solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)