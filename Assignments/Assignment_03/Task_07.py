# Write your code here
class Student:
    def __init__(self,name,id,dept,grades):
        self.name = name
        self.id = id
        self.dept = dept
        self.grades = grades

    def calculate_CGPA(self):
        sum = 0
        for i in self.grades:
            sum += i*3
        self.cgpa = sum / (len(self.grades)*3)
        if self.cgpa > 3.8:
            self.cmnt = "Your academic standing is 'Highest Distinction'"
        elif self.cgpa > 3.65:
            self.cmnt = "Your academic standing is 'High Distinction'"
        elif self.cgpa > 3.5:
            self.cmnt = "Your academic standing is  'Distinction'"
        elif self.cgpa> 2.00:
            self.cmnt = "Your academic standing is  'Satisfactory'"
        else:
            self.cmnt = "Sorry, you cannot Graduate"

    def print_details(self):
        print(f"Name: {self.name}, ID: {self.id} \nDepartment: {self.dept} \nCGPA: {self.cgpa} \n{self.cmnt}")
#==================================================

s1 = Student('Dora', '15995599','CSE', [4,3.7,3.7,4])
s1.calculate_CGPA()
print("==========================")
s1.print_details()
print("==========================")
s2 = Student('Pingu', '12312322', 'EEE', [1.7,1.3,1.3,1.3,1])
s2.calculate_CGPA()
print("==========================")
s2.print_details()
print("==========================")
s3 = Student('Bob', '13311331', 'CSE', [2,3,3,3.7,2.7,2.7])
s3.calculate_CGPA()
print("==========================")
s3.print_details()