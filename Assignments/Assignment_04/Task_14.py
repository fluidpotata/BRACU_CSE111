# Write your code here
class StudentDatabase:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.cgpa = {}

    def calculateCGPA(self,cgpa,course):
        for i in cgpa:
            self.cgpa[0:5] = cgpa[-3:]
        self.course = course
        
        

    def printDetails(self):
        print('MaishaxTamim')1


# Do not change the following lines of code.

s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'], 'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('------------------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'], 'Summer2022')
print('------------------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('------------------------------------------------------')
s2.printDetails()
