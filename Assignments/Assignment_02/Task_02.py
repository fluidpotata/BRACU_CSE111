class Flower:
    def __init__(self,name = None,color = None,num = None):
#         self.name = name
#         self.color = color
#         self.num_of_petal = num
          pass
        


flower1 = Flower()
flower1.name="Rose"
flower1.color="Red"
flower1.num_of_petal=6
print("Name of this flower:", flower1.name)
print("Color of this flower:",flower1.color)
print("Number of petal:",flower1.num_of_petal)
print("=====================")
flower2 = Flower()
flower2.name="Orchid"
flower2.color="Purple"
flower2.num_of_petal=4
print("Name of this flower:",flower2.name)
print("Color of this flower:",flower2.color)
print ("Number of petal:",flower2. num_of_petal)


print(hex(id(flower1)))
print(hex(id(flower2)))
if flower1 == flower2:
    print("They are the same")
else:
    print("They are different")
