# Write your code here.
class Programmer:
  def __init__(self,name,lang,exp):
    print('Horray! A new programmer is born')
    self.name = name
    self.language = lang
    self.experience = exp

  def addExp(self,new):
    print("Updating experience of",self.name)
    self.experience += new

  def printDetails(self):
    print(f"Name: {self.name} \nLanguage: {self.language} \nExperience: {self.experience}")


#========================================#

p1 = Programmer("Ethen Hunt", "Java", 10)
p1.printDetails()
print('--------------------------')
p2 = Programmer("James Bond", "C++", 7)
p2.printDetails()
print('--------------------------')
p3 = Programmer("Jon Snow", "Python", 4)
p3.printDetails()
p3.addExp(5)
p3.printDetails()
