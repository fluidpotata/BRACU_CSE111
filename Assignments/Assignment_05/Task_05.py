# Write your code here for subtasks 1-5
class Circle:
    def __init__(self,r):
        self.__radius = r
        self.__area = 3.1416*r**2

    def getRadius(self):
        return self.__radius

    def setRadius(self,r):
        self.__radius = r

    def area(self):
        return self.__area

    def __add__(self, other):
        temp = self.__radius+other.__radius
        return Circle(temp)

#===============================================
c1 = Circle(4)
print("First circle radius:", c1.getRadius())
print("First circle area:", c1.area())

c2 = Circle(5)
print("Second circle radius:", c2.getRadius())
print("Second circle area:", c2.area())

c3 = c1 + c2
print("Third circle radius:", c3.getRadius())
print("Third circle area:", c3.area())
