class Student:
    count=0
    totalgpa=0
    students=[]
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1
        Student.totalgpa+=gpa
        print(f"{self.get_details()}")
        Student.students.append(self)

    
    def get_details(self):
        return f"{self.name},{self.gpa}"
    @classmethod
    def getcount(cls):
        return f"total Students:{cls.count}"
    @classmethod
    def getavg(cs):
        if cs.count==0:
            return 0
        else:
            return f"total average of class:{cs.totalgpa / cs.count:.2f}"
    # @classmethod
    # def getdetails(cs):
    #     return f"{cs.name}"
    @classmethod
    def detailsofstud(cls):
        return "\n".join([student.get_details() for student in cls.students])

student1=Student("arun",3.2)
student2=Student("joyal",4.0)

print(Student.getcount())
print(Student.getavg())
# print(Student.getdetails())
print(Student.detailsofstud())
    