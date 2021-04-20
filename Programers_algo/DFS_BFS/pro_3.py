# 단어 변환


def solution(begin, target, words):
    # print("test")

    if begin not in words:
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


    def dfs(begin,index,visitied):
        # print("test")

        # 방문 처리
        visitied[begin]=1

        # 다음 노드 찾기
        result=[]
        for i in words:
            if find(begin,i):
                # result.append(i)
                index+=1
                # print(begin,i)

                if visitied[i]==0:
                    dfs(i,index,visitied)

            if target==i:
                return index+1
                break


        # print(result)
        # dfs()

    visitied=dict()
    for i in words:
        visitied[i]=0

    # print(visitied)

    # print(dfs(begin,0,visitied))

    answer = dfs(begin,0,visitied)
    return answer


print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))