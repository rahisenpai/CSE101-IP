def fun(l):
    yearbook={}
    for i in l:
        if ':' in i:
            d,record = {},''
            record = i[:-2]
            yearbook[record]=d
        elif ',' in i:
            x=i.split(',')
            d[x[0]]=int(x[1])
    return(yearbook)

f=open(r'D:\Python\new\assignment 2\03_file.txt')
l=f.readlines()
yearbook=fun(l)
l1=[]
for i in yearbook.items():
    l1.append((sum(i[1].values()),i[0]))
l1.sort()

print('min signatures:',end=' ')
for i  in range(0,len(l1)):
    print(l1[i][1],end=', ')
    if l1[i+1][0]>l1[i][0]:
        break
print('\nmax signatures:',end=' ')
for i  in range(-1,-len(l)-1,-1):
    print(l1[i][1],end=', ')
    if l1[i-1][0]<l1[i][0]:
        break