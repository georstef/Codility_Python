def solution(A):
    B = {}
    cnt = 0
    try:
        dominator = A[0]
    else:
        dominator = 0
    for i in range(len(A)):
        try:
            B[A[i]].append(i) 
        except:
            B[A[i]] = [i]
        if len(B[A[i]]) > cnt:
            dominator = A[i]
            cnt = len(B[A[i]])
            
    if cnt > (len(A) // 2):
        return B[dominator][0]
    else:
        return -1
            
