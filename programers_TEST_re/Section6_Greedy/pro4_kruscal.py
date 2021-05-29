def solution(n, costs):
    # 크루스칼 Union Find
    def find_parent(parent, x):
        # 이미 x가 어딘가에 속해 있다는 뜻으로 어딘가에 속해 있는 부모를 찾는다.
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        # 노드가 큰 것을 찾고, 노드가 큰 부모를 작은 값으로 갱신한다.
        if a < b:
            parent[b] = a

        else:
            parent[a] = b

    # 부모 만들기
    parent = [0] * (n + 1)

    # 부모를 자기 자신으로 초기화
    for i in range(1, n + 1):
        parent[i] = i

    # costs 순으로 오름차순하기 위해 주어진 costs의 3번쨰 인자 부터 넣기
    edges = []

    for i in costs:
        edges.append((i[2], i[0], i[1]))
    edges.sort()

    # 만약 두 노드가 연결되어 있지 않다면 연결하기 (부모를 통해 연결)

    cnt = 0
    for i in edges:
        a = i[1]
        b = i[2]

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            # 연결이 성공했다면 비용 더하기
            cnt += i[0]

    print(cnt)

    answer = 0
    return answer

solution(4,	[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])