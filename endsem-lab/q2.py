def fun(l):
    l.sort()
    x=len(l)
    if x%2!=0:
        m=x//2
        median=l[m]
        b_m=sum(l[:m])/len(l[:m])
        a_m=sum(l[m:])/len(l[m:])
        return median,b_m,a_m
    else:
        m=int(x/2)
        median=(l[m-1]+l[m])/2
        b_m=sum(l[:m])/len(l[:m])
        a_m=sum(l[m:])/len(l[m:])
        return median,b_m,a_m

l=[23,34,45,56,25,20,37,35]
med,b_m,a_m=fun(l)
print('median:',med)
print('avg below median:',b_m)
print('avg above median:',a_m)