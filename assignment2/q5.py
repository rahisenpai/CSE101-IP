def product(a,b):
    pro=[]
    for i in range(len(a)):
        x=[]
        for j in range(3):
            sum=0
            for k in range(3):
                sum += a[i][k]*b[k][j]
            x.append(sum)
        pro.append(x)
    return pro

mat=[]
n=int(input('enter number of coordinates: '))
for i in range(n):
    y=[int(num) for num in input('enter space separated coordinates: ').split()]
    y.append(1)
    mat.append(y)
cx=int(input('enter cx: '))
cy=int(input('enter cy: '))
sc_mat=[[cx,0,0],[0,cy,0],[0,0,1]]

result=product(mat, sc_mat)
print('\nthe coordinates are',end=' ')
for i in result:
    print((i[0],i[1]),end=' ')