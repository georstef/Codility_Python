def solution(N):
    s = bin(N)[2:]
    for i in reversed(range(len(s)-1)):
        if '1'+(i*'0')+'1' in s:
            return i
    return 0
