"""https://programmers.co.kr/learn/courses/30/lessons/12978"""

import heapq

INF = float("inf")


def dijkstra(N, graph):
    distances = [INF] * N
    start_node = 0
    distances[start_node] = 0

    queue = []
    heapq.heappush(queue, (0, start_node))
    while queue:
        distance, current_node = heapq.heappop(queue)
        if distances[current_node] < distance:
            continue
        for adj_node, adj_distance in graph[current_node]:
            print("ad_node",adj_node)
            new_distance = distance + adj_distance
            if new_distance < distances[adj_node]:
                distances[adj_node] = new_distance
                heapq.heappush(queue, (new_distance, adj_node))

    return distances


def solution(N, road, K):
    graph = [[] for _ in range(N)]
    for a, b, c in road:
        graph[a - 1].append((b - 1, c))
        graph[b - 1].append((a - 1, c))

    print(graph)
    distances = dijkstra(N, graph)
    print(distances)

    return len([x for x in distances if x <= K])


if __name__ == "__main__":
    assert (
        solution(
            N=5,
            road=[
                [1, 2, 1],
                [2, 3, 3],
                [5, 2, 2],
                [1, 4, 2],
                [5, 3, 1],
                [5, 4, 2],
            ],
            K=3,
        )
        == 4
    )


# solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)