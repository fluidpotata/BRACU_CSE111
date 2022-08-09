#Write your code here for subtasks 1-6.
class Student:
    ID = 0

    def __init__(self, name, department, age, cgpa):
        self.name = name
        self.department = department
        self.age = age
        self.cgpa = cgpa
        Student.ID += 1

    def get_details(self):
        print(f"ID: {self.ID}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Age: {self.age}")
        print(f"CGPA: {self.cgpa}")

    @classmethod
    def from_String(cls,strng):
        temp = strng.split("-")
        return cls(temp[0],temp[1],temp[2],temp[3])



s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()


# Write the answer of subtask 5 here

# Write the answer of subtask 6 here
