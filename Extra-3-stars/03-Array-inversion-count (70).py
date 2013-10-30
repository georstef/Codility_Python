def solution(A):
    l = len(A)
    result = 0
    for i in range(l):
        #print([j for j in A[i+1:] if j < A[i]])
        result += len([j for j in A[i+1:] if j < A[i]])
    return result
------------------------
def solution(A):
	result = 0
	for i in range(len(A)):
		for item in A[i+1:]:
			if item < A[i]:
				result += 1
	return result
------------------------
def solution(A):
	result = 0
	for i in range(len(A)):
		for item in A[i+1:]:
			if item < A[i]:
				result += 1
                if result > 1000000000:
                    return -1
	return result
-------------------------
def solution(A):
    l = len(A)
    a = []
    for i in range(l):
        a += [j for j in A[i+1:] if j < A[i]]
    result = len(a)
    if result > 1000000000:
        return -1
    return result