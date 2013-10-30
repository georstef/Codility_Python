def solution(A):
    left_part = A[0]
    sum_all = sum(A)
    min_diff = abs((2*left_part) - sum_all)
    for i in range(1,len(A)-1):
        left_part += A[i]
        min_diff = min(min_diff, abs((2*left_part) - sum_all))
    return min_diff
