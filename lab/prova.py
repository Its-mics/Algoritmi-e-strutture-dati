import math
import numpy as np
#definisco sqrt come radice quadrata
sqrt = math.sqrt

#input
m = int(input("Inserisci il primo numero: "))
n = int(input("Inserisci il secondo numero: "))

def MCD(m,n):
    mcd = 0
    for i in range(1, sqrt(n)):
        if i | n:
            if n//i | m:
                return n//i
        elif i | m:  
            mcd = i
    return m

print("Il massimo comune divisore tra", m, "e", n, "è:", MCD(m,n))