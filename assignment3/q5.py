def fun0(cname, credits, assessments, policy):
    d={}
    d['name']=cname
    d['credits']=credits
    d['assessments']=assessments
    d['policy']=policy
    return d

def uploadmarks():
        with open('marks.txt','r') as f:
            d=f.readlines()
        d1={}
        for i in d:
            x=i.strip().split(',')
            total=0
            for j in x[1:]:
                total+=float(j)
            total=round(total,1)
            d1[x[0]]=[x[1:],total]
        return d1

def cutoffs(l,policy):
    r=[]
    for i in policy:
        r.append((i+2,i-2))
    co=[]
    for i in r:
        x=[]
        for j in l:
            if i[0]>=j[1] and i[1]<=j[1]:
                x.append(j[1])
        x.sort(reverse=True)
        co.append(x)
    final=[]
    for i in co:
        if len(i)!=0:
            x,c=0,0
            for j in range(1,len(i)):
                y=i[j-1]-i[j]
                if y>=x:
                    x=y
                    c=j
            final.append((i[c]+i[c-1])/2)
        else:
            final.append(policy[co.index(i)])
    return final

def dograding(x,l):
    d={0:'A',1:'B',2:'C',3:'D'}
    if x<l[-1]:
        grade='F'
    else:
        for i in range(len(l)):
            if x>=l[i]:
                grade=d.get(i)
                break
    return grade


cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)] 
policy = [80, 65, 50, 40]
course=fun0(cname, credits, assessments, policy)
student=uploadmarks()
cutoff=cutoffs(student.values(),policy)
print(cutoff)
A,B,C,D,F=0,0,0,0,0
for i in student:
    z=student.get(i)
    g=dograding(z[1],cutoff)
    z.append(g)
    student[i]=z
    if g=='A':
        A+=1
    elif g=='B':
        B+=1
    elif g=='C':
        C+=1
    elif g=='D':
        D+=1
    elif g=='F':
        F+=1


while(1):
    n=input('enter choice: ')
    if not n:
        break
    elif n=='1':
        print(f'Course Name: {course["name"]}\nCredits: {course["credits"]}\nAssessments: {course["assessments"]}\nCutoffs: {cutoff}\nGrading summary: A:{A}, B:{B}, C:{C}, D:{D}, F:{F}')
    elif n=='2':
        f6=open('q5p2.txt','w')
        for i in student.items():
            f6.write(f'{i[0]}, {i[1][1]}, {i[1][2]}\n')
        f6.close()
        print('output file named q5p2.txt created successfully')
    elif n=='3':
        r=input('enter rollno: ')
        i=student[r]
        print(f'{i[0]}, {i[1]}, {i[2]}')
    else:
        print('invalid input')