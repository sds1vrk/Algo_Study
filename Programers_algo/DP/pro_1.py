# N으로 표현
# 한가지 숫자만 사용하여 number 만들기
# 만들수 있는 가짓수중에서 최솟값 구하기
# 최솟값이 8보다 크면 -1을 return

def solution(N, number):
    # 메모제이션
    d=[0]*32001
    if N==number:
        return 1
    # 1을 제외하고는 자기 자신으로 나누는 것밖에 없음 5/5
    if N==1:
        d[1]=1
    else :
        d[1] = 2

    for i in range(2,N+1):
        # f(11)+1
        d[i]=d[i-1]+d[1]

        # 현재의 수가 2로 나누어 떨어지는 경우
        if i%2==0:
            







    answer = 0
    return answer


solution(5,12)
