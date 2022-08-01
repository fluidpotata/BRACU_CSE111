# Write your code here for subtasks 1-5
class Triangle:
    def __init__(self,b,h):
        self.__base = b
        self.__height = h


t1 = Triangle(10, 5)
print("First Triangle Base:", t1.getBase())
print("First Triangle Height:", t1.getHeight())
print("First Triangle area:", t1.area())

t2 = Triangle(5, 3)
print("Second Triangle Base:", t2.getBase())
print("Second Triangle Height:", t2.getHeight())
print("Second Triangle area:", t2.area())

t3 = t1 - t2
print("Third Triangle Base:", t3.getBase())
print("Third Triangle Height:", t3.getHeight())
print("Third Triangle area:", t3.area())
