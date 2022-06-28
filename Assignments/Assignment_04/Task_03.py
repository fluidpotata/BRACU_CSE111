# Write your code here
class Cat:
    def __init__(self,colour="White",activity="sitting"):
        self.color = colour
        self.activity = activity

    def printCat(self):
        print(f'{self.color} cat is {self.activity}')

    def changeColor(self,newclr):
        self.color = newclr


#=======================================
c1 = Cat()
c2 = Cat("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
