# 스택을 이용한 풀이법

def solution(skill, skill_trees):
    # 만약 스킬 트리의 인자를 다 없앨 수 있으면 이건 가능한 스킬트리, 못 없애면 불가능한 스킬트리
    cnt = 0

    for i in skill_trees:
        a = list(i)
        # print("a",a)

        idx = len(skill) - 1
        # for i in range(len(a)-1,-1,-1):
        a_idx = len(a) - 1
        while a:
            # print("a",a[a_idx])
            if a[a_idx] in skill and skill:
                if a[a_idx] == skill[idx]:
                    # print("here")
                    a.pop()
                    idx -= 1
                else:
                    break
            else:
                a.pop()

            a_idx -= 1

        if len(a) == 0:
            cnt += 1

    return cnt