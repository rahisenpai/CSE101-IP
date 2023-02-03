def fun(l1,l2):
    if len(l1)<=0 or len(l2)<=0:
        return []
    else:
        return [(l1[0], l2[0])] + fun(l1[1:],l2[1:])

l1=[int(n) for n in input('enter space separated elements: ').split()]
l2=[int(n) for n in input('enter space separated elements: ').split()]
print(fun(l1,l2))