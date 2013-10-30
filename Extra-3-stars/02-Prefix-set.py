def solution(A):
    a = [0] * len(A);
    for i in range(len(A)):
        if (a[A[i]] == 0):
            a[A[i]] = 1;
            result = i;
    return result;	