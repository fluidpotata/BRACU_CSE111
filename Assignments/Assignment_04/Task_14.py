# Write your code here
class StudentDatabase:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = {}

    def calculateGPA(self, cgpa, semester):
        new = []
        totalcgpa = 0
        totalcourse = 0
        for i in cgpa:
            a = i.split(': ')
            new.append(a[0])
            totalcgpa += float(a[1])
            totalcourse += 1
        finalcgpa = round((totalcgpa/totalcourse),2)
        self.grades[semester] = {tuple(new):finalcgpa}

    def printDetails(self):
        print(f'Name: {self.name} \nID: {self.id}')
        for i in self.grades.keys():
            print(f"Courses taken in {i}:")
            for j,v in self.grades[i].items():
                for k in j:
                    print(k)
                print("GPA:",v)






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