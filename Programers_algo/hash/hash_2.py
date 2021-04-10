# 전화번호부 접두어 찾기

# 전화번호의 일부면 False 그렇지 않으면 True

def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    print(phone_book)

    for i in range(len(phone_book)):

        for j in range(i+1,len(phone_book),1):
            if phone_book[i] in phone_book[j]:
                return False

    return True

solution(["119", "97674223", "1195524421"])
# solution(["123","456","789"])
#solution(["12","123","1235","567","88"])