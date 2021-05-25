# 해시
# 전화번호 목록
# 2중 for문을 사용하면 시간 초과 발생
# 해결방법
# for문 1개만 써서 해결
# 문자로 정렬하면 숫자가 작은 1같은것이 먼저 앞에 나옴
# 따라서 정렬을 하면 바로 뒤의 숫자가 앞 숫자의 접두어가 안되면 그 뒤는 확인할 필요가 없음 (문자열 정렬이기 떄문에 가능)

def solution(phone_book):
    phone_book.sort()

    print("sort",phone_book)
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False


    else:
        return True

    # for i in range(len(phone_book)-1):
    #     for j in range(i + 1, len(phone_book)):
    #         if phone_book[j].startswith(phone_book[i]):
    #             return False
    # else:
    #     return True

solution(["123","456","789"])
print(solution(["119", "97674223", "1195524421"]))