# Write Your Code Here
class Student:
    student_num = 0
    cse_dept = 0
    bba_dept = 0

    def __init__(self,name,dept):
        print(f"Creating Student Number: {self.student_num+1}")
        self.name = name
        self.dept = dept
        if dept.lower() == "cse":
            Student.cse_dept += 1
        elif dept.upper() == 'BBA':
            Student.bba_dept += 1
        Student.student_num += 1

    def individualInfo(self):
        print(f"{self.name} is from {self.dept} department.")
        print(f"Serial of {self.name} among all students' is: {self.student_num}")
        if self.dept=="CSE":
            print(f"Serial of {self.name} in CSE department is: {self.cse_dept}")
        else:
            print(f"Serial of {self.name} in CSE department is: {self.bba_dept}")

    @classmethod
    def totalInfo(cls):
        print(f"Total Number of Student: {cls.student_num}")
        print(f"Total Number of CSE Student: {cls.cse_dept}")
        print(f"Total Number of BBA Student: {cls.bba_dept}")




#==============================================
s1 = Student("Naruto", "CSE")
print('----------------------')
s1.individualInfo()
print('#############################')
s1.totalInfo()
print('============================')
s2 = Student("Sakura", "BBA")
print('----------------------')
s2.individualInfo()
print('#############################')
s2.totalInfo()
print('============================')
s3 = Student("Shikamaru", "CSE")
print('----------------------')
s3.individualInfo()
print('#############################')
s3.totalInfo()
print('============================')
s4 = Student("Deidara", "BBA")
print('----------------------')
s4.individualInfo()
print('#############################')
s4.totalInfo()