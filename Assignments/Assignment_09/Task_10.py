class Student:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    def Details(self):
        return "Name: "+self.name+"\n"+"ID: "+self.ID+"\n"
#Write your code here
class CSEStudent(Student):
    def __init__(self,name,id,sem):
        super().__init__(name,id)
        self.sem = sem
        self.course = {}

    def addCourseWithMarks(self,*args):
        tmp = 0.0
        for i in range(0,len(args),2):
            if args[i + 1] >=85:
                tmp = 4.0
            elif args[i+1]>=80:
                tmp = 3.3
            elif args[i+1]>=70:
                tmp = 3.0
            elif args[i+1]>=65:
                tmp = 2.3
            elif args[i+1]>=57:
                tmp = 2.0
            elif args[i+1]>=55:
                tmp = 1.3
            elif args[i+1]>=50:
                tmp = 1.0
            else:
                tmp = 0.0
            self.course[args[i]] = tmp

    def Details(self):
        return super().Details()+f"\nCurrent Semester: {self.sem}"

    def showGPA(self):
        print(f"{self.name} has taken {len(self.course.keys())} courses.")
        for k,v in self.course.items():
            print(f"{k}: {v}")

        self.gpa = sum(self.course.values())/len(self.course.values())
        print(f"GPA of {self.name} is: {round(self.gpa,2)}")


#==================================================
Bob = CSEStudent("Bob","20301018","Fall 2020")
Carol = CSEStudent("Carol","16301814","Fall 2020")
Anny = CSEStudent("Anny","18201234","Fall 2020")
print("#########################")
print(Bob.Details())
print("#########################")
print(Carol.Details())
print("#########################")
print(Anny.Details())
print("#########################")
Bob.addCourseWithMarks("CSE111",83.5,"CSE230",73.0,"CSE260",92.5)
Carol.addCourseWithMarks("CSE470",62.5,"CSE422",69.0,"CSE460",76.5,"CSE461",87.0)
Anny.addCourseWithMarks("CSE340",45.5,"CSE321",95.0,"CSE370",91.0)
print("----------------------------")
Bob.showGPA()
print("----------------------------")
Carol.showGPA()
print("----------------------------")
Anny.showGPA()
#########################
