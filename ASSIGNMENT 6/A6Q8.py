def get_factor(n,k):
    factor=[]
    for i in range(1,n+1):
        if(n%i==0):
            factor.append(i)
    if(k<=len(factor) and k>0):
        return factor[k-1]
    else:
        return "INVALID"
print(get_factor(12,4))