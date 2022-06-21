# Write your code here
class Shape:
    def __init__(self,shape,arg1,arg2):
        self.shape = shape.lower()
        if shape.lower() == "triangle":
            self.base = arg1
            self.height = arg2
        elif shape.lower()=="rhombus":
            self.diag1 = arg1
            self.diag2 = arg2
        elif shape.lower()=="square" or shape.lower()=="rectangle":
            self.side1 = arg1
            self.side2 = arg2

    def area(self):
        if self.shape == "triangle":
            print(f"Area: {.5*self.base*self.height}")
        elif self.shape == "rhombus":
            print(f"Area: {(self.diag1*self.diag2)/2}")
        elif self.shape == "square" or self.shape== "rectangle":
            print(f"Area: {self.side1*self.side2}")
        else:
            print("Shape Unknown")


#================================

triangle = Shape("Triangle",10,25)
triangle.area()
print("==========================")
square = Shape("Square",10,10)
square.area()
print("==========================")
rhombus = Shape("Rhombus",18,25)
rhombus.area()
print("==========================")
rectangle = Shape("Rectangle",15,30)
rectangle.area()
print("==========================")
trapezium = Shape("Trapezium",15,30)
trapezium.area()