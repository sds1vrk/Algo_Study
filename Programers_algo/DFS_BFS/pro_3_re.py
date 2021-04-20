# 단어 변환
# 해결 방법
# BFS로 한 이유 : 최단 경로를 찾기 때문에 계층이 짧아야 됨, 따라서 BFS를 사용
# 1. visitied 방문 정보를 "단어"를 키값으로 하기
# 2. 1개 단어가 차이 나는것들 함수 처리
# 3. bfs로 해당 단어가 방문한지 아닌지 반복하며 queue에 넣기

from collections import deque

def solution(begin, target, words):

    # 해당 단어가 없으면 바로 return
    if target not in words:
        return 0

    # 1개 차이나는 것 찾기
    def find(begin,word):
        k=0
        for i in range(len(word)):
            if begin[i]!=word[i]:
                k+=1
        if k==1:
            return True
        else :
            return False


    def bfs(begin,index,visitied):
        queue = deque()
        queue.append([index,begin])
        while queue:
            index,k=queue.popleft()
            # 방문처리
            visitied[k]=1
            index+=1

            # 만약 해당 단어들이 이미 방문한 단어라면 거르기
            new_words=[i for i in words if visitied[i]==0]
            # print(new_words)
            for i in new_words:
                if find(k, i):
                    queue.append([index, i])
                    if i == target:
                        return index

    # 방문 정보를 key값으로 하여 저장
    visitied=dict()
    for i in words:
        visitied[i]=0

    answer = bfs(begin,0,visitied)
    return answer

# solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])
# solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"])