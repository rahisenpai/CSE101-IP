class Course:
    def __init__(self, name, credits, assessments, policy):
        self.name=name
        self.credits=credits
        self.assessments=assessments
        self.policy=policy
    
    def uploadmarks(self):
        with open('marks.txt','r') as f:
            d=f.readlines()
        l=[]
        for i in d:
            x=i.strip().split(',')
            l.append(x)
        return l
    
    def cutoffs(self,l):
        self.range=[]
        for i in self.policy:
            self.range.append((i+2,i-2))
        co=[]
        for i in self.range:
            x=[]
            for j in l:
                if i[0]>=j and i[1]<=j:
                    x.append(j)
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
                final.append(self.policy[co.index(i)])
        return final

                                  
class Student:
    def __init__(self, l):
        self.rollno=l[0]
        self.marks=l[1:]
        self.total=0
        self.grade=0
        for i in self.marks:
            self.total+=float(i)
        self.total=round(self.total,1)
        
    def dograding(self,l):
        d={0:'A',1:'B',2:'C',3:'D'}
        if self.total<l[-1]:
            self.grade='F'
        else:
            for i in range(len(l)):
                if self.total>=l[i]:
                    self.grade=d.get(i)
                    break
        return self.grade


cname, credits = "IP", 4
assessments = [("labs", 30), ("midsem", 15), ("assignments", 30), ("endsem", 25)] 
policy = [80, 65, 50, 40]
ip=Course(cname, credits, assessments, policy)
y1=ip.uploadmarks()
tm=[]
for i in y1:
    x=Student(i)
    tm.append(x.total)
cutoff=ip.cutoffs(tm)
a,b,c,d,f1=0,0,0,0,0
final=[]
for i in y1:
    x=Student(i)
    y=x.dograding(cutoff)
    final.append((x.rollno,x.marks,x.total,y))
    if y=='A':
        a+=1
    elif y=='B':
        b+=1
    elif y=='C':
        c+=1
    elif y=='D':
        d+=1
    elif y=='F':
        f1+=1


while(1):
    n=input('enter choice: ')
    if not n:
        break
    elif n=='1':
        print(f'Course Name: {ip.name}\nCredits: {ip.credits}\nAssessments: {ip.assessments}\nCutoffs: {cutoff}\nGrading summary: A:{a}, B:{b}, C:{c}, D:{d}, F:{f1}')
    elif n=='2':
        f6=open('q4p2.txt','w')
        for i in final:
            f6.write(f'{i[0]}, {i[2]}, {i[3]}\n')
        f6.close()
        print('output file named q4p2.txt created successfully')
    elif n=='3':
        r=input('enter rollno: ')
        for i in final:
            if i[0]==r:
                print(f'{i[1]}, {i[2]}, {i[3]}')
                break
    else:
        print('invalid input')