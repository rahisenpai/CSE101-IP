grades = {"A+":10, "A":10,  "A-":9, "B":8, "B-":7, "C":6, "C-":5, "D":4, "F":2}
l=[]

def fun1(x):
    check=0
    if x[1] not in '124':
        print("incorrect credit")
        check+=1
    if x[0].isalnum()!=True  or x[0].isupper()!=True or x[0][-2:].isdigit()!=True:
        print('improper course no')
        check+=1
    if x[2] not in grades.keys():
        print("incorrect grade")
        check+=1
    if check==0:
        l.append(x)

def fun2(l):
    sum,cr=0,0
    for i in l:
        print(i[0],':',i[2])
        sum += int(i[1])*grades[i[2]]
        cr += int(i[1])
    if sum==0:
        print('no courses')
    else:
        print('\nSGPA:',round(sum/cr,2))

while(1):
    x = tuple(a for a in input('enter: ').split(' '))
    if len(x)==1:
        break
    fun1(x)
print()
l.sort()
fun2(l)