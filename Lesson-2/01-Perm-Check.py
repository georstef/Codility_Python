def solution(A):
    if (min(A) == 1) and (max(A) == len(A)):
      s = set(A)
      if len(s) == len(A):
          return 1
      else:
          return 0
    else:
        return 0
