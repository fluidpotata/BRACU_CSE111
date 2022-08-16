# Write your code here
class Cat:
    Number_of_cats = 0

    def __init__(self,clr,d):
        self.clr = clr
        self.doin = d
        Cat.Number_of_cats += 1


    @classmethod
    def no_parameter(cls):
        return cls("White","sitting")

    @classmethod
    def first_parameter(cls,p1):
        return cls(p1,"sitting")

    @classmethod
    def second_parameter(cls,p2):
        return cls("Grey",p2)

    def printCat(self):
        print(f"{self.clr} cat is {self.doin}")

    def changeColor(self,clr):
        self.clr = clr
#=======================================================


print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)
