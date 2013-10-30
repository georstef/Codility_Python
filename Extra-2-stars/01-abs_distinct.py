def solution(A):
    s = set([abs(i) for i in A])
    return len(s)
