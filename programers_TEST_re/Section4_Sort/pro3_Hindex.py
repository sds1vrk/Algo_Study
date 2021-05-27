def solution(citations):
    max_value = max(citations)
    # max_value=len(citations)
    # min_value=min(citations)

    if max_value == 0:
        return 0

    for i in range(max_value, 1, -1):
        count = 0
        na_count = 0

        for j in citations:
            if i <= j:
                count += 1
        na_count = len(citations) - count

        if count >= i and na_count <= i:
            return i