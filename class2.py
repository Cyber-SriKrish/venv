class Student:
    @classmethod
    def getcrs():
        Student.crs="Python"
        Student.univ="Klu"
    @classmethod
    def getplace():
        Student.place="PMD"
    def getstuddet(self):
        print("id of self--current implicit object=",id(self))
        self.sno=int(input("enter st no:"))
        self.sname=input("Enter Name:")
        self.smarks=float(input("enter marks:"))
    def dispstuddet(self):
        print("Student Number=",self.sno)
        print("Student Name=",self.sname)
        print("Student Marks=",self.smarks)
        print("Student course=",Student.crs)
        print("Student university=",Student.univ)
        print("Student place=",Student.place)
print("STUDENT 1st st DETAILS")
s1=Student()
print("id",id(s1))
s1.getstuddet()
print("STUDENT 2nd st DETAILS")
s2=Student()
print("id",id(s2))
s2.getstuddet()
print("STUDENT 1st st DETAILS")
s1.dispstuddet()
print("STUDENT 2nd st DETAILS")
s2.dispstuddet()

