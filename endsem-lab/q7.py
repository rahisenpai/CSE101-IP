l = [1, 1, 2, 2, 1, 3, 2, 4, 5, 2, 6,7,8,9]
e = int(input('enter elt: '))
d={}
for i in range(len(l)):
    if l[i]==e:
        x=d.get(e,[])
        x.append(i)
        d[e]=x
for i in d:
    y=d.get(i)
    print(f'frequency is {len(y)} and indices are',end=' ')
    for j in y:
        print(j,end=',')