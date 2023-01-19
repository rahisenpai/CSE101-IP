f=open(r'D:\Python\new\assignment 2\pages.txt')
d1=f.readlines()
d={}
for i in d1:
    l=[]
    x=i.split(':')
    y=x[0].split(',')
    for j in range(0,len(x[1])):
        if x[1][j:j+3]=='URL' and x[1][j+3:j+5].isdigit():
            if x[1][j:j+5] not in l:
                l.append(x[1][j:j+5])
    d[y[0]]=[float(y[1]),l]

n=int(input('enter n: '))
for i in d:
    ab = d.get(i)
    ov_im=ab[0]
    for j in d.values():
        if i in j[1]:
            ac = d.get(i)
            ov_im+=ac[0]/len(ac[1])
    ab.append(ov_im)
    d[i]=ab

abc={}
for i in d.items():
    abc[i[0]]=i[1][2]
ke=list(abc.keys())
ke.sort()
final={i: abc[i] for i in ke}

check=0
for i in final.items():
    print(i)
    check+=1
    if check>=n:
        break