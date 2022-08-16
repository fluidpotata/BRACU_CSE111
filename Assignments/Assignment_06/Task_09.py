# Write your code here
class Student:
    total = 0
    bracu = 0
    other = 0

    def __init__(self,n,d,u="BRAC University"):
        self.name = n
        self.dept = d
        self.uni = u
        Student.total += 1
        if u=="BRAC University":
            Student.bracu += 1
        else:
            Student.other += 1

    @classmethod
    def createStudent(cls,n,d,u="BRAC University"):
        return cls(n,d,u)

    def individualDetail(self):
        print(f"Name: {self.name} \nDepartment: {self.dept} \nInstitution: {self.uni}")

    @classmethod
    def printDetails(cls):
        print(f"Total Student(s): {cls.total} \nBRAC University Student(s): {cls.bracu} \nOther Institution Student(s): {cls.other}")


Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()
