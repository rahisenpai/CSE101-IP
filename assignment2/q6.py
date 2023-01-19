wts = [(10, 5), (20, 5), (100, 10), (40, 10), (50, 10), (60, 10), (70, 10), (80, 10), (90, 10), (100, 20)]
def fun1(l):
    sum=0
    for i in range(1,len(l)):
        sum+= int(l[i])/(wts[i-1][0]/wts[i-1][1])
    return round(sum,2)
def fun2(n):
    if n>=80:
        return 'A'
    elif n>=70:
        return 'A-'
    elif n>=60:
        return 'B'
    elif n>=50:
        return 'B-'
    elif n>=40:
        return 'C'
    elif n>=35:
        return 'C-'
    elif n>=30:
        return 'D'
    else:
        return 'F'

f1=open(r"D:\Python\new\assignment 2\IPmarks.txt")
d=f1.readlines()
l,result=[],[]
for i in d:
    l.append(i.split(','))
for i in l:
    result.append(fun1(i))
f=open(r'D:\Python\new\assignment 2\IPgrades.txt','w')
for i in range(len(l)):
    t=l[i][0]+','+ str(result[i])+',' +fun2(result[i])
    f.write(t+'\n')
f.close()