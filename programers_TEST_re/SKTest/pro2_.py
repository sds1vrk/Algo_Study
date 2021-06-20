# 내구성이 가장 큰 대포를 쏴서 최후에 남는 대포를 찾는 문제

import heapq as hq

def solution(tanks):
    # 탱크 내구도 부수기 문제
    stack=tanks
    size=len(tanks)

    # 우선순위가 가장 높은것을 부수기 위해 -부호를 붙여 넣는다
    h=[]
    for idx,i in enumerate(tanks):
        hq.heappush(h,(-i,i,idx))

    idx=0

    def stack_check(stack):
        kk = 0
        for i in stack:
            if i < 0:
                kk += 1

        if kk == size - 1:
            # print("stack", stack)
            return True

    def attack_check(attack):
        for i in range(idx+1,size):
            if stack[i]<=0:
                continue

            else :
                return stack[i],idx

    while h:
        # 0부터 시작
        attack=stack[idx]

        # if attack<0:
        #     attack=stack[idx+1]

        if attack<=0:
            attack,idx=attack_check(attack)


        # 힙큐에서 가장 높은것을 뽑는다
        # 이떄 자기자신을 제외
        max_val=hq.heappop(h)
        if max_val[2]==idx:
            # 이건 뽑으면 안되므로 다른 것을 뽑는다
            new_max_val=hq.heappop(h)
            # 그리고 앞에서 뽑은것은 다시 집어 넣는다.
            hq.heappush(h,max_val)

            # 아니라면 그냥 진행
            new_idx = new_max_val[2]
            new_energy = new_max_val[1] - attack * 2
            # 스택 갱신
            stack[new_idx] = new_energy

            # 그리고 새로운 에너지를 힙에 다시 넣기
            # 만약 새로운 에너지가 음수라면 다시 넣지 않기
            if new_energy > 0:
                hq.heappush(h, (-new_energy, new_energy, new_idx))


        else :
            # 아니라면 그냥 진행
            new_idx=max_val[2]
            new_energy=max_val[1]-attack*2
            # 스택 갱신
            stack[new_idx] = new_energy

            # 그리고 새로운 에너지를 힙에 다시 넣기
            # 만약 새로운 에너지가 음수라면 다시 넣지 않기
            if new_energy>0:
                hq.heappush(h,(-new_energy,new_energy,new_idx))


        idx+=1

        if idx==size:
            idx=0

        # 스택 검사 만약 스택의 수 중 하나만 음수라면
        res=stack_check(stack)

        if res:
            print(stack)
            # 양수 인 스택 찾기
            for i in range(len(stack)):
                if stack[i]>0:
                    return i+1


print(solution([9,20,7,3]))
print(solution([9,9,2,3]))