def solution(S, P, Q):
    l = len(S)
    a = [0] * (l+1);
    c = [0] * (l+1);
    g = [0] * (l+1);
    t = [0] * (l+1);

    for i in range(l):
        if S[i]=='A':
            a[i+1] = a[i] + 1
            c[i+1] = c[i]
            g[i+1] = g[i]
            t[i+1] = t[i]
        elif S[i]=='C':
            a[i+1] = a[i]
            c[i+1] = c[i] + 1
            g[i+1] = g[i]
            t[i+1] = t[i]
        elif S[i]=='G':
            a[i+1] = a[i]
            c[i+1] = c[i]
            g[i+1] = g[i] + 1 
            t[i+1] = t[i]
        else:
            a[i+1] = a[i]
            c[i+1] = c[i]
            g[i+1] = g[i]
            t[i+1] = t[i] + 1
        
    result = []
    for i in range(len(P)):
        if a[Q[i]+1] - a[P[i]] > 0:
            to_append = 1
        elif c[Q[i]+1] - c[P[i]] > 0:
            to_append = 2
        elif g[Q[i]+1] - g[P[i]] > 0:
            to_append = 3
        else:
            to_append = 4
        
        result.append(to_append)
    return result