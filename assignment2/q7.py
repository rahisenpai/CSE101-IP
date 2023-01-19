def add_entry():
    f1 = open(r'D:\Python\new\assignment 2\addrbook.txt','r')
    d=f1.read()
    f = open(r'D:\Python\new\assignment 2\addrbook.txt','w')
    if len(d)!=0:
        d=eval(d)
    else:
        d={}
    n=input('enter name: ')
    a=input('enter address: ')
    p=input('enter phone: ')
    e=input('enter email: ')
    x={'address':a, 'phone':p, 'email':e}
    y=d.get(n,[])
    y.append(x)
    d[n]=y
    f.write(str(d))
    f.close()
    print('\nadded successfully')

def del_entry():
    f1 = open(r'D:\Python\new\assignment 2\addrbook.txt','r')
    d=f1.read()
    f = open(r'D:\Python\new\assignment 2\addrbook.txt','w')
    if len(d)==0:
        print('nothing to delete, address book is empty')
        return
    else:
        d=eval(d)
    n=input('enter name: ')
    p=input('enter phone: ')
    y=d.get(n)
    for i in range(0,len(y)):
        if p in y[i].values():
            del y[i]
    f.write(str(d))
    f.close()
    print('\ndeleted successfully')

def find():
    f1 = open(r'D:\Python\new\assignment 2\addrbook.txt','r')
    d=f1.read()
    if len(d)==0:
        print('nothing to find, address book is empty')
        return
    else:
        d=eval(d)
    x=input('enter phone/email: ')
    for i in d.items():
        for j in i[1]:
            if x in j.values():
                print(i[0],':',j)

def search():
    f1 = open(r'D:\Python\new\assignment 2\addrbook.txt','r')
    d=f1.read()
    if len(d)==0:
        print('nothing to search, address book is empty')
        return
    else:
        d=eval(d)
    x=input('enter name: ')
    for i in d:
        if x in i:
            print(i,':',d.get(i))
   

while(1):
    print('\n\tMENU')
    print('1. insert an entry')
    print('2. delete an entry')
    print('3. search matching entries with a partial name')
    print('4. find entry with phone number or email')
    print('5. exit')
    a = int(input('enter you choice: '))
    print()
    if a==1:
        add_entry()
    if a==2:
        del_entry()
    if a==3:
        search()
    if a==4:
        find()
    if a==5:
        break