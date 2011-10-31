import math
def giaithua(x):
    i=0
    if x==0:
            return 1
    tam=1
    for i in range(1,x+1):
        tam=tam*i
    return tam
    
print giaithua(1000)