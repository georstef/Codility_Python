def solution(N, A):
    result = [0] * N
    max_counter = 0
    min_value = 0
    for item in A:
        if item <= N:
            result[item-1] = max(result[item-1], min_value)
            result[item-1] += 1
            max_counter = max(max_counter, result[item-1])
        else:
            min_value = max_counter
    
    for i in range(N):
        if result[i] < min_value:
            result[i] = min_value
            
    return result
	
