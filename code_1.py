class Student:

    def __init__(self,name,rollno,m1,m2):   #constructor
        self.name =name
        self.rollno=rollno
        self.m1=m1
        self.m2=m2
    
    def accept(self, Name, Rollno, marks1, marks2):
        ob = Student(Name, Rollno, marks1, marks2)
        ls.append(ob)
    