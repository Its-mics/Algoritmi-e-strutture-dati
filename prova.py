def MCD(m,n):
    mcd = 0
    for i=1 to floor(sqrt(n)):
        if i | n:
            if n//i | m:
                return n//i
        else if i | m
            mcd = i
    return m