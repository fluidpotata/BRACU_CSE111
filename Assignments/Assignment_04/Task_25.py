class Vaccine:
    def __init__(self,name,coun,day):
        self.name = name
        self.country = coun
        self.cooldown = day

class Person:
    def __init__(self,nam,age,des):
        self.name = nam
        self.age = age
        self.designation = des
        self.vacc = None
        self.dose = 0

    def showDetail(self):
        print(f"Name: {self.name} Age: {self.age} Type: {self.designation}")
        print(f'Vaccine name: {self.vacc}')
        if self.dose == 1:
            print("1st dose given")
            print(f"2nd dose: Please come after {self.vacc.cooldown()}")
        else:
            print('''
            1st dose: Given
            2nd dose: Given''')
    def pushVaccine(self,name,dose="1st dose"):
        if self.age>25 or self.designation=="Student":
            if dose != "1st dose":
                if self.vacc != name:
                    print(f"Sorry {self.name}, you can't take two different vaccines")
                else:
                    self.dose += 1
                    print(f"{dose} done for {self.name}")

            else:
                self.vac = name
                if 
                self.dose += 1
                print(f"{dose} has been done for {self.name}")
        else:
            print(f"Sorry {self.name}, Minimum age for taking vaccines is 25 years now")


# Write your code here

astra = Vaccine("AstraZeneca", "UK", 60)
modr = Vaccine("Moderna", "UK", 30)
sin = Vaccine("Sinopharm", "China", 30)
p1 = Person("Bob", 21, "Student")
print("=================================")
p1.pushVaccine(astra)
print("=================================")
p1.showDetail()
print("=================================")
p1.pushVaccine(sin, "2nd Dose")
print("=================================")
p1.pushVaccine(astra, "2nd Dose")
print("=================================")
p1.showDetail()
print("=================================")
p2 = Person("Carol", 23, "Actor")
print("=================================")
p2.pushVaccine(sin)
print("=================================")
p3 = Person("David", 34)
print("=================================")
p3.pushVaccine(modr)
print("=================================")
p3.showDetail()
print("=================================")
p3.pushVaccine(modr, "2nd Dose")

