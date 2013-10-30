def solution(A):
    a = [0] * len(A)
    for i in range(len(A)):
        a[i] = a[i-1] + A[i]
        
    result = 0
    for i in range(len(A)-1):
        if A[i] == 0:
            result += (a[-1] - a[i])
            
    if result > 1000000000:
        return -1
    return result