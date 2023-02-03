class Student:
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
        self.courses={}
    def addcourse(self,x):
        if x not in self.courses:
            self.courses[x]=0
        else:
            raise AssertionError('course already exists')
    def addgrade(self,x,y):
        if x not in self.courses:
            raise AssertionError('course is not in records')
        else:
            self.courses[x]=y
    def average(self):
        z=self.courses.values()
        return (sum(z)/len(z))
    def prints(self):
        a=str(self.rollno)+', '+self.name+', '+str(self.courses)+', '+str(self.average())
        print(a)

s=Student(23001,'stu1')
s.addcourse('cs101')
s.addcourse('M101')
s.addgrade('cs101',9)
s.addgrade('M101',8)
s.prints()