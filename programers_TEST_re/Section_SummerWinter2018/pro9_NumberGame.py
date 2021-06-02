def solution(A, B):
    A.sort()
    B.sort()
    count = 0

    b = 0
    count = 0
    for i in range(len(A)):
        for j in range(b, len(B)):
            if A[i] < B[j]:
                print("b", b)
                print("j", j)
                print(A[i], B[j])
                count += 1
                b += 1
                break
            elif A[i] >= B[j]:
                b += 1
                continue

    return count