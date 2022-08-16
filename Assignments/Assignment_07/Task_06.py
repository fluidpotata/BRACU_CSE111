class Shape:

  def __init__(self, name='Default', height=0, base=0):
    self.area = 0
    self.name = name
    self.height = height
    self.base = base

  def get_height_base(self):
    return "Height: "+str(self.height)+",Base: "+str(self.base)

#write your code here
class triangle(Shape):
  def __init__(self,n='Default', h=0, b=0):
    super().__init__(n,h,b)

  def calcArea(self):
    self.area = .5 * self.base * self.height

  def printDetail(self):
    tmp = f"Shape Name: {self.name}\n" + super().get_height_base() + f"\nArea: {self.area}"
    return tmp

class trapezoid(Shape):
  def __init__(self,n='Default',h=0, b=0, s=0):
    super().__init__(n, h, b)
    self.sidea = s

  def calcArea(self):
    self.area = ((self.sidea+self.base)/2)*self.height

  def printDetail(self):
    tmp = f"Shape Name: {self.name}\n" + super().get_height_base() + f", Side A: {self.sidea}\nArea: {self.area}"
    return tmp




tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())
