l1=[1,2,3,4,5,6,7,8,9]
l=l1.copy()
for i in range(-2,-len(l)-1,-1):
    l.append(l1[i])
print('original list: ',l1)
print('output list: ',l)