def solution(X, A):
    a = [-1] * (X)
    for i in range(len(A)):
        if a[A[i]-1] < 0:
            a[A[i]-1] = i
    if -1 in a:
        return -1
    return max(a)
