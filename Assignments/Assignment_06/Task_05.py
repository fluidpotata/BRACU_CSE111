# Write your code here
class Employee:
    def __init__(self,n,wp):
        self.name = n
        self.workingPeriod = wp

    @classmethod
    def employeeByJoiningYear(cls,n,y):
        return cls(n,2022-y)

    @staticmethod
    def experienceCheck(wp,s):
        if s=="male":
            op = "He "
        else:
            op = "She "
        if wp<3:
            op += "is not experienced"
        else:
            op += "is experienced"
        return op


employee1 = Employee('Dororo', 3)
employee2 = Employee.employeeByJoiningYear('Harry', 2016)
print(employee1.workingPeriod)
print(employee2.workingPeriod)
print(employee1.name)
print(employee2.name)
print(Employee.experienceCheck(2, "male"))
print(Employee.experienceCheck(3, "female"))