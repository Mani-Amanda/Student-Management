class Student:

    def __init__(self,name,rollno,m1,m2):   #constructor
        self.name =name
        self.rollno=rollno
        self.m1=m1
        self.m2=m2
    
    def accept(self, Name, Rollno, marks1, marks2): #create new student
        ob = Student(Name, Rollno, marks1, marks2)
        ls.append(ob)

    def display(self, ob):  #display student details
        print("Name : ", ob.name)
        print("RollNo : ", ob.rollno)
        print("Marks1 : ", ob.m1)
        print("Marks2 : ", ob.m2)
        print("\n") 
    
    def search(self, rn):   #Search student
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i
    
    def delete(self, rn):   #Delete student
        i = obj.search(rn)
        del ls[i]