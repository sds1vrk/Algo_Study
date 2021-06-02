# 원형 DP 문제
# 1번 스티커를 고르냐 안고르냐로 판단

def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]

    # 1번 스티커를 고르는 경우
    dp_1 = [0] * len(sticker)
    # print(dp_1)

    dp_1[0] = sticker[0]
    dp_1[1] = sticker[0]
    # 1번 고르는 경우는 마지막 꺼 선택불가
    for i in range(2, len(sticker) - 1):
        dp_1[i] = max(dp_1[i - 2] + sticker[i], dp_1[i - 1])

    # 1번 고르지 않는 경우
    dp_2 = [0] * len(sticker)
    # dp_2[0]=sticker[0]
    dp_2[0] = 0
    dp_2[1] = sticker[1]
    for i in range(2, len(sticker)):
        dp_2[i] = max(dp_2[i - 2] + sticker[i], dp_2[i - 1])

    a = max(dp_1)
    b = max(dp_2)

    return max(a, b)