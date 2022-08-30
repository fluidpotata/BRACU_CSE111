class Shape3D:

  pi = 3.14159
  def __init__(self, name = 'Default', radius = 0):
    self._area = 0
    self._name = name
    self._height = 'No need'
    self._radius = radius

  def calc_surface_area(self):
    return 2 * Shape3D.pi * self._radius

  def __str__(self):
      return "Radius: "+str(self._radius)
#=================================================
class Sphere(Shape3D):
    def __init__(self,n,r):
      super().__init__(n,r)
      print(f"Shape name: {n}, Area Formula: 4 * pi * r * r")

    def getRadius(self):
      return self._radius

    def getHeight(self):
      return self._height

    def calc_surface_area(self):
      self.area = 4*self.pi*(self.getRadius()**2)

    def __str__(self):
      return (f"Radius: {self.getRadius()}, Height: {self.getHeight()}\nArea: {self.area}")

class Cylinder(Shape3D):
  def __init__(self, name = 'Default', radius = 0,height=0):
    super().__init__(name,radius)
    self._height = height

  def getRadius(self):
    return self._radius

  def getHeight(self):
    return self._height

  def calc_surface_area(self):
    self.area = 2 * self.pi * (self.getRadius()) *(self.getRadius()+self.getHeight())

  def __str__(self):
    return (f"Radius: {self.getRadius()}, Height: {self.getHeight()}\nArea: {self.area}")


#=================================================
sph = Sphere('Sphere', 5)
print('----------------------------------')
sph.calc_surface_area()
print(sph)
print('==================================')
cyl = Cylinder('Cylinder', 5, 10)
print('----------------------------------')
cyl.calc_surface_area()
print(cyl)
