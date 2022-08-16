# Write your code here
import math
class Cylinder:
    radius = 5
    height = 18

    def __init__(self,r,h):
        print(f"Default radius={Cylinder.radius} and height={Cylinder.height}.")
        Cylinder.radius = r
        Cylinder.height = h
        print(f"Updated: radius={self.radius} and height={self.height}.")

    @classmethod
    def swap(cls,h,r):
        return cls(r,h)

    @classmethod
    def changeFormat(cls,strng):
        temp = strng.split("-")
        return cls(int(temp[0]),int(temp[1]))

    @staticmethod
    def area(r,h):
        area = (2*(math.pi)*(r**2)) + (2*math.pi*r*h)
        print("Area: ",area)

    @staticmethod
    def volume(r,h):
        volume = math.pi*(r**2)*h
        print("Volume: ",volume)



c1 = Cylinder(0, 0)
Cylinder.area(c1.radius, c1.height)
Cylinder.volume(c1.radius, c1.height)
print("===============================")
c2 = Cylinder.swap(8, 3)
c2.area(c2.radius, c2.height)
c2.volume(c2.radius, c2.height)
print("===============================")
c3 = Cylinder.changeFormat("7-13")
c3.area(c3.radius, c3.height)
c3.volume(c3.radius, c3.height)
print("===============================")
Cylinder(0.3, 5.56).area(Cylinder.radius, Cylinder.height)
print("===============================")
Cylinder(3, 5).volume(Cylinder.radius, Cylinder.height)

