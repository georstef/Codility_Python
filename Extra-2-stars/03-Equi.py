def solution(A):
    a = [0] * (len(A)+1)
    for i in range(len(A)):
        a[i+1] = a[i] + A[i]
        
    for i in range(len(A)):
        lower = a[i] - a[0]
        upper = a[-1] - a[i+1]
        if lower == upper:
            return i
    return -1