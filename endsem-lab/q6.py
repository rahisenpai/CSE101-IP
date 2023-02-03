with open('in.txt','r') as f1:
    d=f1.readlines()
l=[]
for i in d:
    x=[int(n) for n in i.split()]
    l.append(x)

with open('out.txt','w') as f:
    for i in l:
        x=''
        for j in i:
            y=j*j
            x+=str(y)+' '
        x+='\n'
        f.write(x)