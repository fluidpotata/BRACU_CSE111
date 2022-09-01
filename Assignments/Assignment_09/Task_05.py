# Write your codes here.
class Smartphone:
    def __init__(self,name=None):
        self.name = name
        self.features = {}

    def addFeature(self,f,d):
        if self.name!=None:
            if f in self.features.keys():
                self.features[f].append(d)
            else:
                self.features[f] = [d]
        else:
            print('Feature can not be added without phone name')

    def setName(self,name):
        self.name = name

    def printDetail(self):
        print('Phone name:', self.name)
        for i in self.features.keys():
            print(f"{i}: {', '.join(self.features[i])}")



# Do not change the following lines of code.
s1 = Smartphone()
print("=================================")
s1.addFeature('Display', '6.1 inch')
print("=================================")
s1.setName('Samsung Note 20')
s1.addFeature('Display', '6.1 inch')
s1.printDetail()
print("=================================")
s2 = Smartphone('Iphone 12 Pro')
s2.addFeature('Display', '6.2 inch')
s2.addFeature('Ram', '6 GB')
print("=================================")
s2.printDetail()
s2.addFeature('Display', 'Amoled panel')
s2.addFeature('Ram', 'DDR5')
print("=================================")
s2.printDetail()
print("=================================")