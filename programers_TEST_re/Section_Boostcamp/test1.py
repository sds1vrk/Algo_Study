from collections import defaultdict


def solution(priorities, location):
    answer = 0
    tmp_loc = 0
    tmp_arr = []

    tmp = defaultdict(list)
    for idx, job in enumerate(priorities):
        tmp[job].append(idx)
    sorted_priorities = dict(sorted(tmp.items(), reverse=True))

    print(sorted_priorities)
    for priority in sorted_priorities:
        if priorities[location] is not priority:

            answer += len(sorted_priorities[priority])
            tmp_loc = max(sorted_priorities[priority])
        else:
            print("here")
            matched_list = sorted_priorities[priority][tmp_loc:] + sorted_priorities[priority][:tmp_loc]
            print(matched_list)
            for loc in matched_list:
                if loc == location:

                    return answer + 1

                answer += 1


solution([2,1,3,2],2)
print(solution([1,1,9,1,1],0))