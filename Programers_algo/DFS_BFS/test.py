#인접 행렬

INF=99999999999999999999
'''
    O
 /(7) \(5)
1        2

Node 3개라면 3의 제곱만큼 행렬로 표현
'''

# 2차원 리스트를 이용해 인접 행렬 표현
graph=[
    [0,7,5],
    [7,0,INF],
    [5,INF,0]
]
print(graph)


# 인접 리스트
# 노드의 개수(ROW)만큼 설정하여 2차원 배열 만들기
graph=[[] for _ in range(3)]

# 각 노드랑 연결된 정보만 입력하기 (노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

graph[1].append((0,7))
graph[2].append((0,5))

print(graph)
print(graph[0][1])