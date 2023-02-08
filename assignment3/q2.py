#in the special cases of 2 consecutive exits and entries, only valid data is considered in the program
#for part 1 if a person has no records before specified time then the first record will be used to tell the status

with open(r'D:\Python\new\assignmet 3\sorted_data.txt','r') as f:
    d=f.readlines()

l=[]
for i in d[1:]:
    x=i.split(',')
    for j in range(len(x)):
        x[j]=x[j].strip()
    l.append(x)
l.sort(key= lambda x:x[3])

d={}
for i in l:
    x=d.get(i[0],[])
    if x!=[]:
        if x[-1][1]=='EXIT' and i[1]=='EXIT':
            x.pop()
            x.append((i[2],i[1],i[3]))
        elif x[-1][1]=='ENTER' and i[1]=='ENTER':
            pass
        else:
            x.append((i[2],i[1],i[3]))
    else:
        x.append((i[2],i[1],i[3]))
    d[i[0]]=x


def fun1(s,t):
    x=d.get(s)
    f1=open('q2p1.txt','w')
    for i in x:
        f1.write(str(i)+'\n')
    f1.close()
    for i in range(len(x)):
        if x[i][2]>t:
            if i==0:
                y=x[i]
                if y[1]=='EXIT':
                    print('Currently in campus')
                else:
                    print('Currently not in campus')
            else:
                y=x[i-1]
                if y[1]=='EXIT':
                    print('Currently not in campus')
                else:
                    print('Currently in campus')
            break
    return True

def fun2(s,e):
    f1=open('q2p2.txt','w')
    for i in l:
        if i[3]>=s and i[3]<=e:
            f1.write(i[0]+', '+i[1]+', '+i[2]+', '+i[3]+'\n')
    f1.close
    return True

def fun3(s):
    en,ex=0,0
    for i in d.values():
        for j in i:
            if s in j:
                if 'EXIT' in j:
                    ex+=1
                if 'ENTER' in j:
                    en+=1
    return en,ex


while(1):
    n=input('enter choice: ')
    if not n:
        break
    elif n=='1':
        s=input("enter student's name: ")
        t=input("enter time(hh:mm:ss): ")
        z=fun1(s,t)
        if z:
            print('output file named q2p1.txt created successfully')
    elif n=='2':
        st=input("enter start time(hh:mm:ss): ")
        et=input("enter end time(hh:mm:ss): ")
        y=fun2(st,et)
        if y:
            print('output file named q2p2.txt created successfully')
    elif n=='3':
        g=input("enter gate no.: ")
        a,b=fun3(g)
        print(f'entries: {a}, exits: {b}')
    else:
        print('invalid input')