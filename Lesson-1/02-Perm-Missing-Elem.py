def solution(A):
    should_be = ((len(A)+1) * (len(A)+2)) / 2
    is_now = sum(A)
    return should_be - is_now