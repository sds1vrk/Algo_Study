def solution(brown, yellow):
    for i in range(brown, 0, -1):
        for j in range(0, brown + 1, 1):
            if i >= j and (i * 2) + (j + 2) * 2 == brown:
                yellow_row = i
                yellow_col = j

                if yellow_row * yellow_col == yellow:
                    return [yellow_row + 2, yellow_col + 2]

