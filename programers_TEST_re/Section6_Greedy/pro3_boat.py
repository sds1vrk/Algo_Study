def solution(people, limit):
    cnt = 0
    people.sort()
    while people:
        k = people.pop()
        if people and k + people[0] <= limit:
            people.remove(people[0])

        cnt += 1

    return cnt


print(solution([70, 50, 80, 50],100),3)
print(solution([70, 80, 50],100),3)