# Write your code here for subtasks 1-4.
class Panda():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def sleep(self, intgr="Unknown"):
        self.sleep = str(intgr)
        if intgr == "Unknown":
            return f"{self.name}'s duration is unknown thus should have only bamboo leaves"
        elif 3 <= int(intgr) <= 5:
            self.food = "Mixed Veggies"
        elif 6 <= int(intgr) <= 8:
            self.food = "Eggplant and Tofu"
        elif 9 <= int(intgr) <= 11:
            self.food = "Broccoli Chicken"
        return (f"{self.name} sleeps {self.sleep} hours daily and should have {self.food}")


#===================================================
panda1 = Panda("Kunfu", "Male", 5)
panda2 = Panda("Pan Pan", "Female", 3)
panda3 = Panda("Ming Ming", "Female", 8)

print("{} is a {} Panda Bear who is {} years old".format(panda1.name, panda1.gender, panda1.age))

print("{} is a {} Panda Bear who is {} years old".format(panda2.name, panda2.gender, panda2.age))

print("{} is a {} Panda Bear who is {} years old".format(panda3.name, panda3.gender, panda3.age))
print("===========================")
print(panda2.sleep(10))
print(panda1.sleep(4))
print(panda3.sleep())
