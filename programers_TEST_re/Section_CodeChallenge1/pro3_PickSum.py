def solution(numbers):
    # DFS로 Combination 만들기
    ch = [0] * 2

    answer = set()

    def dfs(l, s):
        if l == 2:
            hap = 0
            for i in range(2):
                hap += ch[i]

            answer.add(hap)


        else:
            for i in range(s, len(numbers)):
                ch[l] = numbers[i]
                dfs(l + 1, i + 1)


    dfs(0, 0)
    print(answer)

    return answer

solution([2,1,3,4,1])