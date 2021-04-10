def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    print(phoneBook)

    # list(zip)을 이용하면 key,value로 값을 만들어줄수있음
    print(list(zip(phoneBook,phoneBook[1:])))

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True


solution(["119", "97674223", "1195524421"])