# Write your code here.
class Student:
    def __init__(self,name,id,dept="CSE"):
        self.name = name
        self.id = id
        self.dept = dept

    def dailyEffort(self,eff):
        self.effort = eff
        if eff<=2:
            self.sugg = "Suggestion: Should give more effort!"
        elif eff<=4:
            self.sugg = 'Suggestion: Keep up the good work!'
        else:
            self.sugg = 'Suggestion: Excellent! Now motivate others.'

    def printDetails(self):
        print(f"Name: {self.name} \nID: {self.id} \nDepartment: {self.dept} \nDaily Effort: {self.effort} hour(s) \n{self.sugg}")
#===========================================
harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()
